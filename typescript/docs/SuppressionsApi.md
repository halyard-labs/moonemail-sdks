# SuppressionsApi

All URIs are relative to *https://api.moonemail.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSuppression**](SuppressionsApi.md#addsuppressionoperation) | **POST** /suppressions | Add suppression |
| [**listSuppressions**](SuppressionsApi.md#listsuppressions) | **GET** /suppressions | List suppressions |
| [**removeSuppression**](SuppressionsApi.md#removesuppression) | **DELETE** /suppressions/{email} | Remove suppression |



## addSuppression

> AddSuppression201Response addSuppression(addSuppressionRequest)

Add suppression

Prevent sending to a recipient.  Required permission: &#x60;suppressions:write&#x60;.

### Example

```ts
import {
  Configuration,
  SuppressionsApi,
} from 'moonemail';
import type { AddSuppressionOperationRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SuppressionsApi(config);

  const body = {
    // AddSuppressionRequest
    addSuppressionRequest: ...,
  } satisfies AddSuppressionOperationRequest;

  try {
    const data = await api.addSuppression(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **addSuppressionRequest** | [AddSuppressionRequest](AddSuppressionRequest.md) |  | |

### Return type

[**AddSuppression201Response**](AddSuppression201Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSuppressions

> ListSuppressions200Response listSuppressions()

List suppressions

Read suppressed recipient addresses and reasons.  Required permission: &#x60;suppressions:read&#x60;.

### Example

```ts
import {
  Configuration,
  SuppressionsApi,
} from 'moonemail';
import type { ListSuppressionsRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SuppressionsApi(config);

  try {
    const data = await api.listSuppressions();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListSuppressions200Response**](ListSuppressions200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## removeSuppression

> RemoveSuppression200Response removeSuppression(email)

Remove suppression

Allow sending to a suppressed recipient again. Only when explicitly requested.  Required permission: &#x60;suppressions:delete&#x60;.

### Example

```ts
import {
  Configuration,
  SuppressionsApi,
} from 'moonemail';
import type { RemoveSuppressionRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SuppressionsApi(config);

  const body = {
    // string
    email: email_example,
  } satisfies RemoveSuppressionRequest;

  try {
    const data = await api.removeSuppression(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email** | `string` |  | [Defaults to `undefined`] |

### Return type

[**RemoveSuppression200Response**](RemoveSuppression200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

