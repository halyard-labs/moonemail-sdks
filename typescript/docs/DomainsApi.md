# DomainsApi

All URIs are relative to *https://api.moonemail.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDomain**](DomainsApi.md#createdomainoperation) | **POST** /domains | Create domain |
| [**deleteDomain**](DomainsApi.md#deletedomain) | **DELETE** /domains/{id} | Delete domain |
| [**getDomain**](DomainsApi.md#getdomain) | **GET** /domains/{id} | Get domain |
| [**getDomainHealth**](DomainsApi.md#getdomainhealth) | **GET** /domains/{id}/health | Get domain health |
| [**listDomains**](DomainsApi.md#listdomains) | **GET** /domains | List domains |
| [**updateDomain**](DomainsApi.md#updatedomainoperation) | **PATCH** /domains/{id} | Update domain |
| [**verifyDomain**](DomainsApi.md#verifydomain) | **POST** /domains/{id}/verify | Verify domain |



## createDomain

> CreateDomain201Response createDomain(createDomainRequest)

Create domain

Add a sending domain and return required DNS records. Does not publish DNS at your provider.  Required permission: &#x60;domains:write&#x60;.

### Example

```ts
import {
  Configuration,
  DomainsApi,
} from 'moonemail';
import type { CreateDomainOperationRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DomainsApi(config);

  const body = {
    // CreateDomainRequest
    createDomainRequest: ...,
  } satisfies CreateDomainOperationRequest;

  try {
    const data = await api.createDomain(body);
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
| **createDomainRequest** | [CreateDomainRequest](CreateDomainRequest.md) |  | |

### Return type

[**CreateDomain201Response**](CreateDomain201Response.md)

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


## deleteDomain

> DeleteDomain200Response deleteDomain(id)

Delete domain

Remove a sending domain, interrupting sending through it. Only when explicitly requested.  Required permission: &#x60;domains:delete&#x60;.

### Example

```ts
import {
  Configuration,
  DomainsApi,
} from 'moonemail';
import type { DeleteDomainRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DomainsApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies DeleteDomainRequest;

  try {
    const data = await api.deleteDomain(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |

### Return type

[**DeleteDomain200Response**](DeleteDomain200Response.md)

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


## getDomain

> CreateDomain201Response getDomain(id)

Get domain

Read sending domain settings, verification status and DNS records.  Required permission: &#x60;domains:read&#x60;.

### Example

```ts
import {
  Configuration,
  DomainsApi,
} from 'moonemail';
import type { GetDomainRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DomainsApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies GetDomainRequest;

  try {
    const data = await api.getDomain(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |

### Return type

[**CreateDomain201Response**](CreateDomain201Response.md)

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


## getDomainHealth

> GetDomainHealth200Response getDomainHealth(id)

Get domain health

Read per-domain sending status and provider bounce/complaint reputation samples. Missing or stale data is not evidence of good health; these are lagging indicators, not inbox placement predictions.  Required permission: &#x60;domains:read&#x60;.

### Example

```ts
import {
  Configuration,
  DomainsApi,
} from 'moonemail';
import type { GetDomainHealthRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DomainsApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies GetDomainHealthRequest;

  try {
    const data = await api.getDomainHealth(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |

### Return type

[**GetDomainHealth200Response**](GetDomainHealth200Response.md)

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


## listDomains

> ListDomains200Response listDomains()

List domains

List team sending domains.  Required permission: &#x60;domains:read&#x60;.

### Example

```ts
import {
  Configuration,
  DomainsApi,
} from 'moonemail';
import type { ListDomainsRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DomainsApi(config);

  try {
    const data = await api.listDomains();
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

[**ListDomains200Response**](ListDomains200Response.md)

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


## updateDomain

> UpdateDomain200Response updateDomain(id, updateDomainRequest)

Update domain

Change tracking or TLS settings. Read existing settings first.  Required permission: &#x60;domains:write&#x60;.

### Example

```ts
import {
  Configuration,
  DomainsApi,
} from 'moonemail';
import type { UpdateDomainOperationRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DomainsApi(config);

  const body = {
    // string
    id: id_example,
    // UpdateDomainRequest
    updateDomainRequest: ...,
  } satisfies UpdateDomainOperationRequest;

  try {
    const data = await api.updateDomain(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |
| **updateDomainRequest** | [UpdateDomainRequest](UpdateDomainRequest.md) |  | |

### Return type

[**UpdateDomain200Response**](UpdateDomain200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## verifyDomain

> UpdateDomain200Response verifyDomain(id)

Verify domain

Request a fresh verification check after publishing DNS records.  Required permission: &#x60;domains:write&#x60;.

### Example

```ts
import {
  Configuration,
  DomainsApi,
} from 'moonemail';
import type { VerifyDomainRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new DomainsApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies VerifyDomainRequest;

  try {
    const data = await api.verifyDomain(body);
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
| **id** | `string` |  | [Defaults to `undefined`] |

### Return type

[**UpdateDomain200Response**](UpdateDomain200Response.md)

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

