package moonemail

import (
	"context"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestSendTransport(t *testing.T) {
	calls := 0
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		calls++
		if r.URL.Path != "/emails" || r.Header.Get("Authorization") != "Bearer test_key" || r.Header.Get("Idempotency-Key") != "stable-key" {
			t.Errorf("unexpected request path or headers")
		}
		var body map[string]interface{}
		json.NewDecoder(r.Body).Decode(&body)
		if body["subject"] != "Hello" || body["text"] != "Body" || body["reply_to"] != "reply@example.com" {
			t.Errorf("wrong payload: %v", body)
		}
		if _, exists := body["html"]; exists {
			t.Error("unset field should be omitted")
		}
		w.Header().Set("Content-Type", "application/json")
		io.WriteString(w, `{"id":"email-1"}`)
	}))
	defer server.Close()
	client, err := New("test_key")
	if err != nil {
		t.Fatal(err)
	}
	client.GetConfig().Servers = ServerConfigurations{{URL: server.URL}}
	scalar := "user@example.com"
	array := []string{scalar}
	for _, to := range []SendEmailRequestTo{StringAsSendEmailRequestTo(&scalar), ArrayOfStringAsSendEmailRequestTo(&array)} {
		body := NewSendEmailRequest("sender@example.com", to, "Hello")
		body.SetText("Body")
		reply := "reply@example.com"
		body.SetReplyTo(StringAsSendEmailRequestTo(&reply))
		result, response, err := client.EmailsAPI.SendEmail(context.Background()).SendEmailRequest(*body).IdempotencyKey("stable-key").Execute()
		if err != nil {
			t.Fatal(err)
		}
		response.Body.Close()
		if result.Id != "email-1" {
			t.Fatal(result)
		}
	}
	if calls != 2 {
		t.Fatal(calls)
	}
}

func TestNullableResponseAndNoRetry(t *testing.T) {
	calls := 0
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		calls++
		w.Header().Set("Content-Type", "application/json")
		if r.URL.Path == "/permissions" {
			io.WriteString(w, `{"permission":"full_access","scopes":["emails:send"],"domain_id":null,"expires_at":null,"can_manage_api_keys":true,"billing_requires_owner":true,"future_field":1}`)
			return
		}
		w.Header().Set("Retry-After", "5")
		w.WriteHeader(429)
		io.WriteString(w, `{"statusCode":429,"name":"rate_limit_exceeded","message":"Slow down"}`)
	}))
	defer server.Close()
	client, _ := New("test_key")
	client.GetConfig().Servers = ServerConfigurations{{URL: server.URL}}
	result, response, err := client.PermissionsAPI.GetPermissions(context.Background()).Execute()
	if err != nil {
		t.Fatal(err)
	}
	response.Body.Close()
	if result.DomainId.Get() != nil || !result.DomainId.IsSet() || result.AdditionalProperties["future_field"] != float64(1) {
		t.Fatal(result)
	}
	_, response, err = client.EmailsAPI.GetEmail(context.Background(), "test-id").Execute()
	if err == nil || response.StatusCode != 429 || response.Header.Get("Retry-After") != "5" {
		t.Fatal("missing HTTP error information")
	}
	response.Body.Close()
	if calls != 2 {
		t.Fatalf("unexpected retry: %d", calls)
	}
}
