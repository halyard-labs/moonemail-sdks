# InboxesApi

All URIs are relative to *https://api.moonemail.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInbox**](InboxesApi.md#createinboxoperation) | **POST** /inboxes | Create inbox |
| [**getInbox**](InboxesApi.md#getinbox) | **GET** /inboxes/{id} | Get inbox |
| [**listInboxes**](InboxesApi.md#listinboxes) | **GET** /inboxes | List inboxes |
| [**updateInbox**](InboxesApi.md#updateinboxoperation) | **PATCH** /inboxes/{id} | Update inbox |



## createInbox

> CreateInbox200Response createInbox(createInboxRequest, idempotencyKey)

Create inbox

Create a random receiving address for this team. Name is a label, not an email local-part. Reuse the idempotency key on retries.  Required permission: &#x60;inboxes:write&#x60;.

### Example

```ts
import {
  Configuration,
  InboxesApi,
} from 'moonemail';
import type { CreateInboxOperationRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new InboxesApi(config);

  const body = {
    // CreateInboxRequest
    createInboxRequest: ...,
    // string | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. (optional)
    idempotencyKey: idempotencyKey_example,
  } satisfies CreateInboxOperationRequest;

  try {
    const data = await api.createInbox(body);
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
| **createInboxRequest** | [CreateInboxRequest](CreateInboxRequest.md) |  | |
| **idempotencyKey** | `string` | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. | [Optional] [Defaults to `undefined`] |

### Return type

[**CreateInbox200Response**](CreateInbox200Response.md)

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


## getInbox

> CreateInbox200Response getInbox(id)

Get inbox

Get a team receiving address and its status.  Required permission: &#x60;inboxes:read&#x60;.

### Example

```ts
import {
  Configuration,
  InboxesApi,
} from 'moonemail';
import type { GetInboxRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new InboxesApi(config);

  const body = {
    // string
    id: id_example,
  } satisfies GetInboxRequest;

  try {
    const data = await api.getInbox(body);
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

[**CreateInbox200Response**](CreateInbox200Response.md)

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


## listInboxes

> ListInboxes200Response listInboxes(limit, after)

List inboxes

List receiving addresses owned by this team.  Required permission: &#x60;inboxes:read&#x60;.

### Example

```ts
import {
  Configuration,
  InboxesApi,
} from 'moonemail';
import type { ListInboxesRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new InboxesApi(config);

  const body = {
    // number (optional)
    limit: 56,
    // string (optional)
    after: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies ListInboxesRequest;

  try {
    const data = await api.listInboxes(body);
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
| **limit** | `number` |  | [Optional] [Defaults to `undefined`] |
| **after** | `string` |  | [Optional] [Defaults to `undefined`] |

### Return type

[**ListInboxes200Response**](ListInboxes200Response.md)

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


## updateInbox

> CreateInbox200Response updateInbox(id, updateInboxRequest)

Update inbox

Enable or disable delivery into an inbox. Disabled addresses discard new incoming mail; addresses are never reassigned.  Required permission: &#x60;inboxes:write&#x60;.

### Example

```ts
import {
  Configuration,
  InboxesApi,
} from 'moonemail';
import type { UpdateInboxOperationRequest } from 'moonemail';

async function example() {
  console.log("🚀 Testing moonemail SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerKey
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new InboxesApi(config);

  const body = {
    // string
    id: id_example,
    // UpdateInboxRequest
    updateInboxRequest: ...,
  } satisfies UpdateInboxOperationRequest;

  try {
    const data = await api.updateInbox(body);
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
| **updateInboxRequest** | [UpdateInboxRequest](UpdateInboxRequest.md) |  | |

### Return type

[**CreateInbox200Response**](CreateInbox200Response.md)

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

