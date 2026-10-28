# \SuppressionsAPI

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddSuppression**](SuppressionsAPI.md#AddSuppression) | **Post** /suppressions | Add suppression
[**ListSuppressions**](SuppressionsAPI.md#ListSuppressions) | **Get** /suppressions | List suppressions
[**RemoveSuppression**](SuppressionsAPI.md#RemoveSuppression) | **Delete** /suppressions/{email} | Remove suppression



## AddSuppression

> AddSuppression201Response AddSuppression(ctx).AddSuppressionRequest(addSuppressionRequest).Execute()

Add suppression



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
	addSuppressionRequest := *openapiclient.NewAddSuppressionRequest("Email_example") // AddSuppressionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SuppressionsAPI.AddSuppression(context.Background()).AddSuppressionRequest(addSuppressionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SuppressionsAPI.AddSuppression``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddSuppression`: AddSuppression201Response
	fmt.Fprintf(os.Stdout, "Response from `SuppressionsAPI.AddSuppression`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAddSuppressionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addSuppressionRequest** | [**AddSuppressionRequest**](AddSuppressionRequest.md) |  | 

### Return type

[**AddSuppression201Response**](AddSuppression201Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSuppressions

> ListSuppressions200Response ListSuppressions(ctx).Execute()

List suppressions



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
	resp, r, err := apiClient.SuppressionsAPI.ListSuppressions(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SuppressionsAPI.ListSuppressions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSuppressions`: ListSuppressions200Response
	fmt.Fprintf(os.Stdout, "Response from `SuppressionsAPI.ListSuppressions`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListSuppressionsRequest struct via the builder pattern


### Return type

[**ListSuppressions200Response**](ListSuppressions200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RemoveSuppression

> RemoveSuppression200Response RemoveSuppression(ctx, email).Execute()

Remove suppression



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
	email := "email_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SuppressionsAPI.RemoveSuppression(context.Background(), email).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SuppressionsAPI.RemoveSuppression``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RemoveSuppression`: RemoveSuppression200Response
	fmt.Fprintf(os.Stdout, "Response from `SuppressionsAPI.RemoveSuppression`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**email** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiRemoveSuppressionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**RemoveSuppression200Response**](RemoveSuppression200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

