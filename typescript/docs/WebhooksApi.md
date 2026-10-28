# WebhooksApi

All URIs are relative to *https://api.moonemail.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebhook**](WebhooksApi.md#createwebhookoperation) | **POST** /webhooks | Create webhook |
| [**deleteWebhook**](WebhooksApi.md#deletewebhook) | **DELETE** /webhooks/{id} | Delete webhook |
| [**getWebhook**](WebhooksApi.md#getwebhook) | **GET** /webhooks/{id} | Get webhook |
| [**listWebhookDeliveries**](WebhooksApi.md#listwebhookdeliveries) | **GET** /webhooks/{id}/deliveries | List webhook deliveries |
| [**listWebhooks**](WebhooksApi.md#listwebhooks) | **GET** /webhooks | List webhooks |
| [**updateWebhook**](WebhooksApi.md#updatewebhookoperation) | **PATCH** /webhooks/{id} | Update webhook |



## createWebhook

> CreateWebhook201Response createWebhook(createWebhookRequest)

Create webhook

Create an event destination. Returns a signing secret once: store it securely, never include it in reports.  Required permission: &#x60;webhooks:write&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from 'moonemail';
import type { CreateWebhookOperationRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // CreateWebhookRequest
    createWebhookRequest: ...,
  } satisfies CreateWebhookOperationRequest;

  try {
    const data = await api.createWebhook(body);
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
| **createWebhookRequest** | [CreateWebhookRequest](CreateWebhookRequest.md) |  | |

### Return type

[**CreateWebhook201Response**](CreateWebhook201Response.md)

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


## deleteWebhook

> DeleteWebhook200Response deleteWebhook(id)

Delete webhook

Delete an event destination. Only when explicitly requested.  Required permission: &#x60;webhooks:delete&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from 'moonemail';
import type { DeleteWebhookRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies DeleteWebhookRequest;

  try {
    const data = await api.deleteWebhook(body);
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

[**DeleteWebhook200Response**](DeleteWebhook200Response.md)

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


## getWebhook

> ListWebhooks200ResponseDataInner getWebhook(id)

Get webhook

Read a webhook configuration without its signing secret.  Required permission: &#x60;webhooks:read&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from 'moonemail';
import type { GetWebhookRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies GetWebhookRequest;

  try {
    const data = await api.getWebhook(body);
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

[**ListWebhooks200ResponseDataInner**](ListWebhooks200ResponseDataInner.md)

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


## listWebhookDeliveries

> ListWebhookDeliveries200Response listWebhookDeliveries(id)

List webhook deliveries

Inspect webhook delivery attempts.  Required permission: &#x60;webhooks:read&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from 'moonemail';
import type { ListWebhookDeliveriesRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies ListWebhookDeliveriesRequest;

  try {
    const data = await api.listWebhookDeliveries(body);
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

[**ListWebhookDeliveries200Response**](ListWebhookDeliveries200Response.md)

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


## listWebhooks

> ListWebhooks200Response listWebhooks()

List webhooks

List team webhook destinations without existing signing secrets.  Required permission: &#x60;webhooks:read&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from 'moonemail';
import type { ListWebhooksRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  try {
    const data = await api.listWebhooks();
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

[**ListWebhooks200Response**](ListWebhooks200Response.md)

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


## updateWebhook

> UpdateWebhook200Response updateWebhook(id, updateWebhookRequest)

Update webhook

Change a webhook destination, events or enabled status. A new destination receives team event data.  Required permission: &#x60;webhooks:write&#x60;.

### Example

```ts
import {
  Configuration,
  WebhooksApi,
} from 'moonemail';
import type { UpdateWebhookOperationRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new WebhooksApi(config);

  const body = {
    // string
    id: id_example,
    // UpdateWebhookRequest
    updateWebhookRequest: ...,
  } satisfies UpdateWebhookOperationRequest;

  try {
    const data = await api.updateWebhook(body);
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
| **updateWebhookRequest** | [UpdateWebhookRequest](UpdateWebhookRequest.md) |  | |

### Return type

[**UpdateWebhook200Response**](UpdateWebhook200Response.md)

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

