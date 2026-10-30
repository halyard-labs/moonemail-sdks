# \InboxesAPI

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateInbox**](InboxesAPI.md#CreateInbox) | **Post** /inboxes | Create inbox
[**GetInbox**](InboxesAPI.md#GetInbox) | **Get** /inboxes/{id} | Get inbox
[**ListInboxes**](InboxesAPI.md#ListInboxes) | **Get** /inboxes | List inboxes
[**UpdateInbox**](InboxesAPI.md#UpdateInbox) | **Patch** /inboxes/{id} | Update inbox



## CreateInbox

> ListInboxes200ResponseDataInner CreateInbox(ctx).CreateInboxRequest(createInboxRequest).IdempotencyKey(idempotencyKey).Execute()

Create inbox



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
	createInboxRequest := *openapiclient.NewCreateInboxRequest("Name_example") // CreateInboxRequest | 
	idempotencyKey := "idempotencyKey_example" // string | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InboxesAPI.CreateInbox(context.Background()).CreateInboxRequest(createInboxRequest).IdempotencyKey(idempotencyKey).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InboxesAPI.CreateInbox``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateInbox`: ListInboxes200ResponseDataInner
	fmt.Fprintf(os.Stdout, "Response from `InboxesAPI.CreateInbox`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateInboxRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createInboxRequest** | [**CreateInboxRequest**](CreateInboxRequest.md) |  | 
 **idempotencyKey** | **string** | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. | 

### Return type

[**ListInboxes200ResponseDataInner**](ListInboxes200ResponseDataInner.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetInbox

> ListInboxes200ResponseDataInner GetInbox(ctx, id).Execute()

Get inbox



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
	resp, r, err := apiClient.InboxesAPI.GetInbox(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InboxesAPI.GetInbox``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetInbox`: ListInboxes200ResponseDataInner
	fmt.Fprintf(os.Stdout, "Response from `InboxesAPI.GetInbox`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetInboxRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ListInboxes200ResponseDataInner**](ListInboxes200ResponseDataInner.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListInboxes

> ListInboxes200Response ListInboxes(ctx).Limit(limit).After(after).Execute()

List inboxes



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
	resp, r, err := apiClient.InboxesAPI.ListInboxes(context.Background()).Limit(limit).After(after).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InboxesAPI.ListInboxes``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListInboxes`: ListInboxes200Response
	fmt.Fprintf(os.Stdout, "Response from `InboxesAPI.ListInboxes`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListInboxesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** |  | 
 **after** | **string** |  | 

### Return type

[**ListInboxes200Response**](ListInboxes200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateInbox

> ListInboxes200ResponseDataInner UpdateInbox(ctx, id).UpdateInboxRequest(updateInboxRequest).Execute()

Update inbox



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
	updateInboxRequest := *openapiclient.NewUpdateInboxRequest("Status_example") // UpdateInboxRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InboxesAPI.UpdateInbox(context.Background(), id).UpdateInboxRequest(updateInboxRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InboxesAPI.UpdateInbox``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateInbox`: ListInboxes200ResponseDataInner
	fmt.Fprintf(os.Stdout, "Response from `InboxesAPI.UpdateInbox`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateInboxRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateInboxRequest** | [**UpdateInboxRequest**](UpdateInboxRequest.md) |  | 

### Return type

[**ListInboxes200ResponseDataInner**](ListInboxes200ResponseDataInner.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

