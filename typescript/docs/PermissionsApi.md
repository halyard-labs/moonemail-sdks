# PermissionsApi

All URIs are relative to *https://api.moonemail.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPermissions**](PermissionsApi.md#getpermissions) | **GET** /permissions | Get permissions |



## getPermissions

> GetPermissions200Response getPermissions()

Get permissions

Inspect this credential’s scopes, expiry and sender restriction.  Required permission: &#x60;authenticated&#x60;.

### Example

```ts
import {
  Configuration,
  PermissionsApi,
} from 'moonemail';
import type { GetPermissionsRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new PermissionsApi(config);

  try {
    const data = await api.getPermissions();
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

[**GetPermissions200Response**](GetPermissions200Response.md)

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

