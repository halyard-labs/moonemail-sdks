# \EmailsAPI

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CancelEmail**](EmailsAPI.md#CancelEmail) | **Post** /emails/{id}/cancel | Cancel email
[**GetEmail**](EmailsAPI.md#GetEmail) | **Get** /emails/{id} | Get email
[**ListEmailEvents**](EmailsAPI.md#ListEmailEvents) | **Get** /emails/{id}/events | List email events
[**ListEmails**](EmailsAPI.md#ListEmails) | **Get** /emails | List emails
[**SendBatch**](EmailsAPI.md#SendBatch) | **Post** /emails/batch | Send batch
[**SendEmail**](EmailsAPI.md#SendEmail) | **Post** /emails | Send email
[**UpdateEmail**](EmailsAPI.md#UpdateEmail) | **Patch** /emails/{id} | Update email



## CancelEmail

> UpdateEmail200Response CancelEmail(ctx, id).Execute()

Cancel email



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmailsAPI.CancelEmail(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmailsAPI.CancelEmail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CancelEmail`: UpdateEmail200Response
	fmt.Fprintf(os.Stdout, "Response from `EmailsAPI.CancelEmail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiCancelEmailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**UpdateEmail200Response**](UpdateEmail200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEmail

> GetEmail200Response GetEmail(ctx, id).Execute()

Get email



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmailsAPI.GetEmail(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmailsAPI.GetEmail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetEmail`: GetEmail200Response
	fmt.Fprintf(os.Stdout, "Response from `EmailsAPI.GetEmail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEmailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetEmail200Response**](GetEmail200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListEmailEvents

> ListEmailEvents200Response ListEmailEvents(ctx, id).Execute()

List email events



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
	id := "id_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmailsAPI.ListEmailEvents(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmailsAPI.ListEmailEvents``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListEmailEvents`: ListEmailEvents200Response
	fmt.Fprintf(os.Stdout, "Response from `EmailsAPI.ListEmailEvents`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListEmailEventsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ListEmailEvents200Response**](ListEmailEvents200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListEmails

> ListEmails200Response ListEmails(ctx).Limit(limit).After(after).Before(before).Execute()

List emails



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
	limit := int32(56) // int32 |  (optional)
	after := "after_example" // string |  (optional)
	before := "before_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmailsAPI.ListEmails(context.Background()).Limit(limit).After(after).Before(before).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmailsAPI.ListEmails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListEmails`: ListEmails200Response
	fmt.Fprintf(os.Stdout, "Response from `EmailsAPI.ListEmails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListEmailsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** |  | 
 **after** | **string** |  | 
 **before** | **string** |  | 

### Return type

[**ListEmails200Response**](ListEmails200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SendBatch

> SendBatch200Response SendBatch(ctx).SendEmailRequest(sendEmailRequest).IdempotencyKey(idempotencyKey).Execute()

Send batch



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
	sendEmailRequest := []openapiclient.SendEmailRequest{*openapiclient.NewSendEmailRequest("From_example", openapiclient.send_email_request_to{ArrayOfString: new([]string)}, "Subject_example")} // []SendEmailRequest | 
	idempotencyKey := "idempotencyKey_example" // string | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmailsAPI.SendBatch(context.Background()).SendEmailRequest(sendEmailRequest).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmailsAPI.SendBatch``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SendBatch`: SendBatch200Response
	fmt.Fprintf(os.Stdout, "Response from `EmailsAPI.SendBatch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSendBatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sendEmailRequest** | [**[]SendEmailRequest**](SendEmailRequest.md) |  | 
 **idempotencyKey** | **string** | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. | 

### Return type

[**SendBatch200Response**](SendBatch200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## SendEmail

> SendEmail200Response SendEmail(ctx).SendEmailRequest(sendEmailRequest).IdempotencyKey(idempotencyKey).Execute()

Send email



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
	sendEmailRequest := *openapiclient.NewSendEmailRequest("From_example", openapiclient.send_email_request_to{ArrayOfString: new([]string)}, "Subject_example") // SendEmailRequest | 
	idempotencyKey := "idempotencyKey_example" // string | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmailsAPI.SendEmail(context.Background()).SendEmailRequest(sendEmailRequest).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmailsAPI.SendEmail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `SendEmail`: SendEmail200Response
	fmt.Fprintf(os.Stdout, "Response from `EmailsAPI.SendEmail`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiSendEmailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sendEmailRequest** | [**SendEmailRequest**](SendEmailRequest.md) |  | 
 **idempotencyKey** | **string** | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. | 

### Return type

[**SendEmail200Response**](SendEmail200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateEmail

> UpdateEmail200Response UpdateEmail(ctx, id).UpdateEmailRequest(updateEmailRequest).Execute()

Update email



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/halyard-labs/moonemail-sdks/go"
)

func main() {
	id := "id_example" // string | 
	updateEmailRequest := *openapiclient.NewUpdateEmailRequest("ScheduledAt_example") // UpdateEmailRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmailsAPI.UpdateEmail(context.Background(), id).UpdateEmailRequest(updateEmailRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmailsAPI.UpdateEmail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateEmail`: UpdateEmail200Response
	fmt.Fprintf(os.Stdout, "Response from `EmailsAPI.UpdateEmail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateEmailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateEmailRequest** | [**UpdateEmailRequest**](UpdateEmailRequest.md) |  | 

### Return type

[**UpdateEmail200Response**](UpdateEmail200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

