# \ReceivingAPI

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetReceivedAttachment**](ReceivingAPI.md#GetReceivedAttachment) | **Get** /emails/receiving/{id}/attachments/{attachment_id} | Get received attachment
[**GetReceivedEmail**](ReceivingAPI.md#GetReceivedEmail) | **Get** /emails/receiving/{id} | Get received email
[**GetReceivedRaw**](ReceivingAPI.md#GetReceivedRaw) | **Get** /emails/receiving/{id}/raw | Get received raw
[**ListReceivedAttachments**](ReceivingAPI.md#ListReceivedAttachments) | **Get** /emails/receiving/{id}/attachments | List received attachments
[**ListReceivedEmails**](ReceivingAPI.md#ListReceivedEmails) | **Get** /emails/receiving | List received emails



## GetReceivedAttachment

> GetReceivedAttachment200Response GetReceivedAttachment(ctx, id, attachmentId).Execute()

Get received attachment



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
	attachmentId := "attachmentId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ReceivingAPI.GetReceivedAttachment(context.Background(), id, attachmentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReceivingAPI.GetReceivedAttachment``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetReceivedAttachment`: GetReceivedAttachment200Response
	fmt.Fprintf(os.Stdout, "Response from `ReceivingAPI.GetReceivedAttachment`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 
**attachmentId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetReceivedAttachmentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**GetReceivedAttachment200Response**](GetReceivedAttachment200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetReceivedEmail

> GetReceivedEmail200Response GetReceivedEmail(ctx, id).Execute()

Get received email



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
	resp, r, err := apiClient.ReceivingAPI.GetReceivedEmail(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReceivingAPI.GetReceivedEmail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetReceivedEmail`: GetReceivedEmail200Response
	fmt.Fprintf(os.Stdout, "Response from `ReceivingAPI.GetReceivedEmail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetReceivedEmailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetReceivedEmail200Response**](GetReceivedEmail200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetReceivedRaw

> GetReceivedRaw200Response GetReceivedRaw(ctx, id).Execute()

Get received raw



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
	resp, r, err := apiClient.ReceivingAPI.GetReceivedRaw(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReceivingAPI.GetReceivedRaw``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetReceivedRaw`: GetReceivedRaw200Response
	fmt.Fprintf(os.Stdout, "Response from `ReceivingAPI.GetReceivedRaw`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetReceivedRawRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetReceivedRaw200Response**](GetReceivedRaw200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListReceivedAttachments

> ListReceivedAttachments200Response ListReceivedAttachments(ctx, id).Execute()

List received attachments



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
	resp, r, err := apiClient.ReceivingAPI.ListReceivedAttachments(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReceivingAPI.ListReceivedAttachments``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListReceivedAttachments`: ListReceivedAttachments200Response
	fmt.Fprintf(os.Stdout, "Response from `ReceivingAPI.ListReceivedAttachments`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiListReceivedAttachmentsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ListReceivedAttachments200Response**](ListReceivedAttachments200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListReceivedEmails

> ListReceivedEmails200Response ListReceivedEmails(ctx).Limit(limit).After(after).Execute()

List received emails



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
	after := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ReceivingAPI.ListReceivedEmails(context.Background()).Limit(limit).After(after).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ReceivingAPI.ListReceivedEmails``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListReceivedEmails`: ListReceivedEmails200Response
	fmt.Fprintf(os.Stdout, "Response from `ReceivingAPI.ListReceivedEmails`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListReceivedEmailsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** |  | 
 **after** | **string** |  | 

### Return type

[**ListReceivedEmails200Response**](ListReceivedEmails200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

