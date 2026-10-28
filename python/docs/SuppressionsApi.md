# moonemail.SuppressionsApi

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_suppression**](SuppressionsApi.md#add_suppression) | **POST** /suppressions | Add suppression
[**list_suppressions**](SuppressionsApi.md#list_suppressions) | **GET** /suppressions | List suppressions
[**remove_suppression**](SuppressionsApi.md#remove_suppression) | **DELETE** /suppressions/{email} | Remove suppression


# **add_suppression**
> AddSuppression201Response add_suppression(add_suppression_request)

Add suppression

Prevent sending to a recipient.

Required permission: `suppressions:write`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.add_suppression201_response import AddSuppression201Response
from moonemail.models.add_suppression_request import AddSuppressionRequest
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
    api_instance = moonemail.SuppressionsApi(api_client)
    add_suppression_request = moonemail.AddSuppressionRequest() # AddSuppressionRequest | 

    try:
        # Add suppression
        api_response = api_instance.add_suppression(add_suppression_request)
        print("The response of SuppressionsApi->add_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->add_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_suppression_request** | [**AddSuppressionRequest**](AddSuppressionRequest.md)|  | 

### Return type

[**AddSuppression201Response**](AddSuppression201Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_suppressions**
> ListSuppressions200Response list_suppressions()

List suppressions

Read suppressed recipient addresses and reasons.

Required permission: `suppressions:read`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.list_suppressions200_response import ListSuppressions200Response
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
    api_instance = moonemail.SuppressionsApi(api_client)

    try:
        # List suppressions
        api_response = api_instance.list_suppressions()
        print("The response of SuppressionsApi->list_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->list_suppressions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListSuppressions200Response**](ListSuppressions200Response.md)

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

# **remove_suppression**
> RemoveSuppression200Response remove_suppression(email)

Remove suppression

Allow sending to a suppressed recipient again. Only when explicitly requested.

Required permission: `suppressions:delete`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.remove_suppression200_response import RemoveSuppression200Response
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
    api_instance = moonemail.SuppressionsApi(api_client)
    email = 'email_example' # str | 

    try:
        # Remove suppression
        api_response = api_instance.remove_suppression(email)
        print("The response of SuppressionsApi->remove_suppression:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuppressionsApi->remove_suppression: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**RemoveSuppression200Response**](RemoveSuppression200Response.md)

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

