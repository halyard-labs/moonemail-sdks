# \APIKeysAPI

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateApiKey**](APIKeysAPI.md#CreateApiKey) | **Post** /api-keys | Create API key
[**DeleteApiKey**](APIKeysAPI.md#DeleteApiKey) | **Delete** /api-keys/{id} | Delete API key
[**ListApiKeys**](APIKeysAPI.md#ListApiKeys) | **Get** /api-keys | List API keys



## CreateApiKey

> CreateApiKey201Response CreateApiKey(ctx).CreateApiKeyRequest(createApiKeyRequest).Execute()

Create API key



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
	createApiKeyRequest := *openapiclient.NewCreateApiKeyRequest("Name_example") // CreateApiKeyRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.APIKeysAPI.CreateApiKey(context.Background()).CreateApiKeyRequest(createApiKeyRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIKeysAPI.CreateApiKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateApiKey`: CreateApiKey201Response
	fmt.Fprintf(os.Stdout, "Response from `APIKeysAPI.CreateApiKey`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateApiKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createApiKeyRequest** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md) |  | 

### Return type

[**CreateApiKey201Response**](CreateApiKey201Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteApiKey

> DeleteApiKey200Response DeleteApiKey(ctx, id).Execute()

Delete API key



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
	resp, r, err := apiClient.APIKeysAPI.DeleteApiKey(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIKeysAPI.DeleteApiKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteApiKey`: DeleteApiKey200Response
	fmt.Fprintf(os.Stdout, "Response from `APIKeysAPI.DeleteApiKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteApiKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DeleteApiKey200Response**](DeleteApiKey200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListApiKeys

> ListApiKeys200Response ListApiKeys(ctx).Execute()

List API keys



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.APIKeysAPI.ListApiKeys(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `APIKeysAPI.ListApiKeys``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListApiKeys`: ListApiKeys200Response
	fmt.Fprintf(os.Stdout, "Response from `APIKeysAPI.ListApiKeys`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListApiKeysRequest struct via the builder pattern


### Return type

[**ListApiKeys200Response**](ListApiKeys200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

