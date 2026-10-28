# moonemail.InboxesApi

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inbox**](InboxesApi.md#create_inbox) | **POST** /inboxes | Create inbox
[**get_inbox**](InboxesApi.md#get_inbox) | **GET** /inboxes/{id} | Get inbox
[**list_inboxes**](InboxesApi.md#list_inboxes) | **GET** /inboxes | List inboxes
[**update_inbox**](InboxesApi.md#update_inbox) | **PATCH** /inboxes/{id} | Update inbox


# **create_inbox**
> CreateInbox200Response create_inbox(create_inbox_request, idempotency_key=idempotency_key)

Create inbox

Create a random receiving address for this team. Name is a label, not an email local-part. Reuse the idempotency key on retries.

Required permission: `inboxes:write`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.create_inbox200_response import CreateInbox200Response
from moonemail.models.create_inbox_request import CreateInboxRequest
from moonemail.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.moonemail.co
# See configuration.py for a list of all supported configuration parameters.
configuration = moonemail.Configuration(
    host = "https://api.moonemail.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerKey
configuration = moonemail.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moonemail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moonemail.InboxesApi(api_client)
    create_inbox_request = moonemail.CreateInboxRequest() # CreateInboxRequest | 
    idempotency_key = 'idempotency_key_example' # str | Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. (optional)

    try:
        # Create inbox
        api_response = api_instance.create_inbox(create_inbox_request, idempotency_key=idempotency_key)
        print("The response of InboxesApi->create_inbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboxesApi->create_inbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inbox_request** | [**CreateInboxRequest**](CreateInboxRequest.md)|  | 
 **idempotency_key** | **str**| Optional in REST; mandatory for the MCP sending tool. Reuse the same key and payload for retries. | [optional] 

### Return type

[**CreateInbox200Response**](CreateInbox200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox**
> CreateInbox200Response get_inbox(id)

Get inbox

Get a team receiving address and its status.

Required permission: `inboxes:read`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.create_inbox200_response import CreateInbox200Response
from moonemail.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.moonemail.co
# See configuration.py for a list of all supported configuration parameters.
configuration = moonemail.Configuration(
    host = "https://api.moonemail.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerKey
configuration = moonemail.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moonemail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moonemail.InboxesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get inbox
        api_response = api_instance.get_inbox(id)
        print("The response of InboxesApi->get_inbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboxesApi->get_inbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CreateInbox200Response**](CreateInbox200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inboxes**
> ListInboxes200Response list_inboxes(limit=limit, after=after)

List inboxes

List receiving addresses owned by this team.

Required permission: `inboxes:read`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.list_inboxes200_response import ListInboxes200Response
from moonemail.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.moonemail.co
# See configuration.py for a list of all supported configuration parameters.
configuration = moonemail.Configuration(
    host = "https://api.moonemail.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerKey
configuration = moonemail.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moonemail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moonemail.InboxesApi(api_client)
    limit = 56 # int |  (optional)
    after = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        # List inboxes
        api_response = api_instance.list_inboxes(limit=limit, after=after)
        print("The response of InboxesApi->list_inboxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboxesApi->list_inboxes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **after** | **UUID**|  | [optional] 

### Return type

[**ListInboxes200Response**](ListInboxes200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbox**
> CreateInbox200Response update_inbox(id, update_inbox_request)

Update inbox

Enable or disable delivery into an inbox. Disabled addresses discard new incoming mail; addresses are never reassigned.

Required permission: `inboxes:write`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.create_inbox200_response import CreateInbox200Response
from moonemail.models.update_inbox_request import UpdateInboxRequest
from moonemail.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.moonemail.co
# See configuration.py for a list of all supported configuration parameters.
configuration = moonemail.Configuration(
    host = "https://api.moonemail.co"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerKey
configuration = moonemail.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moonemail.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moonemail.InboxesApi(api_client)
    id = 'id_example' # str | 
    update_inbox_request = moonemail.UpdateInboxRequest() # UpdateInboxRequest | 

    try:
        # Update inbox
        api_response = api_instance.update_inbox(id, update_inbox_request)
        print("The response of InboxesApi->update_inbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboxesApi->update_inbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_inbox_request** | [**UpdateInboxRequest**](UpdateInboxRequest.md)|  | 

### Return type

[**CreateInbox200Response**](CreateInbox200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

