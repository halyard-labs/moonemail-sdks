# \DomainsAPI

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateDomain**](DomainsAPI.md#CreateDomain) | **Post** /domains | Create domain
[**DeleteDomain**](DomainsAPI.md#DeleteDomain) | **Delete** /domains/{id} | Delete domain
[**GetDomain**](DomainsAPI.md#GetDomain) | **Get** /domains/{id} | Get domain
[**GetDomainHealth**](DomainsAPI.md#GetDomainHealth) | **Get** /domains/{id}/health | Get domain health
[**ListDomains**](DomainsAPI.md#ListDomains) | **Get** /domains | List domains
[**UpdateDomain**](DomainsAPI.md#UpdateDomain) | **Patch** /domains/{id} | Update domain
[**VerifyDomain**](DomainsAPI.md#VerifyDomain) | **Post** /domains/{id}/verify | Verify domain



## CreateDomain

> CreateDomain201Response CreateDomain(ctx).CreateDomainRequest(createDomainRequest).Execute()

Create domain



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
	createDomainRequest := *openapiclient.NewCreateDomainRequest("Name_example") // CreateDomainRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DomainsAPI.CreateDomain(context.Background()).CreateDomainRequest(createDomainRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainsAPI.CreateDomain``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateDomain`: CreateDomain201Response
	fmt.Fprintf(os.Stdout, "Response from `DomainsAPI.CreateDomain`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateDomainRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDomainRequest** | [**CreateDomainRequest**](CreateDomainRequest.md) |  | 

### Return type

[**CreateDomain201Response**](CreateDomain201Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteDomain

> DeleteDomain200Response DeleteDomain(ctx, id).Execute()

Delete domain



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
	resp, r, err := apiClient.DomainsAPI.DeleteDomain(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainsAPI.DeleteDomain``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteDomain`: DeleteDomain200Response
	fmt.Fprintf(os.Stdout, "Response from `DomainsAPI.DeleteDomain`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteDomainRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**DeleteDomain200Response**](DeleteDomain200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDomain

> CreateDomain201Response GetDomain(ctx, id).Execute()

Get domain



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
	resp, r, err := apiClient.DomainsAPI.GetDomain(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainsAPI.GetDomain``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDomain`: CreateDomain201Response
	fmt.Fprintf(os.Stdout, "Response from `DomainsAPI.GetDomain`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDomainRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CreateDomain201Response**](CreateDomain201Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDomainHealth

> GetDomainHealth200Response GetDomainHealth(ctx, id).Execute()

Get domain health



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
	resp, r, err := apiClient.DomainsAPI.GetDomainHealth(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainsAPI.GetDomainHealth``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDomainHealth`: GetDomainHealth200Response
	fmt.Fprintf(os.Stdout, "Response from `DomainsAPI.GetDomainHealth`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDomainHealthRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**GetDomainHealth200Response**](GetDomainHealth200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListDomains

> ListDomains200Response ListDomains(ctx).Execute()

List domains



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
	resp, r, err := apiClient.DomainsAPI.ListDomains(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainsAPI.ListDomains``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListDomains`: ListDomains200Response
	fmt.Fprintf(os.Stdout, "Response from `DomainsAPI.ListDomains`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListDomainsRequest struct via the builder pattern


### Return type

[**ListDomains200Response**](ListDomains200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateDomain

> UpdateDomain200Response UpdateDomain(ctx, id).UpdateDomainRequest(updateDomainRequest).Execute()

Update domain



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
	updateDomainRequest := *openapiclient.NewUpdateDomainRequest() // UpdateDomainRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DomainsAPI.UpdateDomain(context.Background(), id).UpdateDomainRequest(updateDomainRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainsAPI.UpdateDomain``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateDomain`: UpdateDomain200Response
	fmt.Fprintf(os.Stdout, "Response from `DomainsAPI.UpdateDomain`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateDomainRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateDomainRequest** | [**UpdateDomainRequest**](UpdateDomainRequest.md) |  | 

### Return type

[**UpdateDomain200Response**](UpdateDomain200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VerifyDomain

> UpdateDomain200Response VerifyDomain(ctx, id).Execute()

Verify domain



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
	resp, r, err := apiClient.DomainsAPI.VerifyDomain(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DomainsAPI.VerifyDomain``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VerifyDomain`: UpdateDomain200Response
	fmt.Fprintf(os.Stdout, "Response from `DomainsAPI.VerifyDomain`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiVerifyDomainRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**UpdateDomain200Response**](UpdateDomain200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

