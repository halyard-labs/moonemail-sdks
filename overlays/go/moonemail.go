package moonemail

import (
	"errors"
	"net/http"
	"strings"
	"time"
)

// New returns a server-side Moonemail client. Generated API methods accept context
// cancellation. It does not retry sends; reuse the idempotency key for retries.
func New(apiKey string) (*APIClient, error) {
	if strings.TrimSpace(apiKey) == "" {
		return nil, errors.New("a Moonemail API key is required")
	}
	config := NewConfiguration()
	config.AddDefaultHeader("Authorization", "Bearer "+apiKey)
	config.HTTPClient = &http.Client{Timeout: 30 * time.Second}
	return NewAPIClient(config), nil
}
