# moonemail.PermissionsApi

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissions**](PermissionsApi.md#get_permissions) | **GET** /permissions | Get permissions


# **get_permissions**
> GetPermissions200Response get_permissions()

Get permissions

Inspect this credential’s scopes, expiry and sender restriction.

Required permission: `authenticated`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.get_permissions200_response import GetPermissions200Response
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
    api_instance = moonemail.PermissionsApi(api_client)

    try:
        # Get permissions
        api_response = api_instance.get_permissions()
        print("The response of PermissionsApi->get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsApi->get_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPermissions200Response**](GetPermissions200Response.md)

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

