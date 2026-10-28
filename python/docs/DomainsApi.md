# moonemail.DomainsApi

All URIs are relative to *https://api.moonemail.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain**](DomainsApi.md#create_domain) | **POST** /domains | Create domain
[**delete_domain**](DomainsApi.md#delete_domain) | **DELETE** /domains/{id} | Delete domain
[**get_domain**](DomainsApi.md#get_domain) | **GET** /domains/{id} | Get domain
[**get_domain_health**](DomainsApi.md#get_domain_health) | **GET** /domains/{id}/health | Get domain health
[**list_domains**](DomainsApi.md#list_domains) | **GET** /domains | List domains
[**update_domain**](DomainsApi.md#update_domain) | **PATCH** /domains/{id} | Update domain
[**verify_domain**](DomainsApi.md#verify_domain) | **POST** /domains/{id}/verify | Verify domain


# **create_domain**
> CreateDomain201Response create_domain(create_domain_request)

Create domain

Add a sending domain and return required DNS records. Does not publish DNS at your provider.

Required permission: `domains:write`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.create_domain201_response import CreateDomain201Response
from moonemail.models.create_domain_request import CreateDomainRequest
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
    api_instance = moonemail.DomainsApi(api_client)
    create_domain_request = moonemail.CreateDomainRequest() # CreateDomainRequest | 

    try:
        # Create domain
        api_response = api_instance.create_domain(create_domain_request)
        print("The response of DomainsApi->create_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->create_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_domain_request** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | 

### Return type

[**CreateDomain201Response**](CreateDomain201Response.md)

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

# **delete_domain**
> DeleteDomain200Response delete_domain(id)

Delete domain

Remove a sending domain, interrupting sending through it. Only when explicitly requested.

Required permission: `domains:delete`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.delete_domain200_response import DeleteDomain200Response
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
    api_instance = moonemail.DomainsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete domain
        api_response = api_instance.delete_domain(id)
        print("The response of DomainsApi->delete_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DeleteDomain200Response**](DeleteDomain200Response.md)

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

# **get_domain**
> CreateDomain201Response get_domain(id)

Get domain

Read sending domain settings, verification status and DNS records.

Required permission: `domains:read`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.create_domain201_response import CreateDomain201Response
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
    api_instance = moonemail.DomainsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get domain
        api_response = api_instance.get_domain(id)
        print("The response of DomainsApi->get_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CreateDomain201Response**](CreateDomain201Response.md)

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

# **get_domain_health**
> GetDomainHealth200Response get_domain_health(id)

Get domain health

Read per-domain sending status and provider bounce/complaint reputation samples. Missing or stale data is not evidence of good health; these are lagging indicators, not inbox placement predictions.

Required permission: `domains:read`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.get_domain_health200_response import GetDomainHealth200Response
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
    api_instance = moonemail.DomainsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get domain health
        api_response = api_instance.get_domain_health(id)
        print("The response of DomainsApi->get_domain_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetDomainHealth200Response**](GetDomainHealth200Response.md)

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

# **list_domains**
> ListDomains200Response list_domains()

List domains

List team sending domains.

Required permission: `domains:read`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.list_domains200_response import ListDomains200Response
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
    api_instance = moonemail.DomainsApi(api_client)

    try:
        # List domains
        api_response = api_instance.list_domains()
        print("The response of DomainsApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDomains200Response**](ListDomains200Response.md)

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

# **update_domain**
> UpdateDomain200Response update_domain(id, update_domain_request)

Update domain

Change tracking or TLS settings. Read existing settings first.

Required permission: `domains:write`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.update_domain200_response import UpdateDomain200Response
from moonemail.models.update_domain_request import UpdateDomainRequest
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
    api_instance = moonemail.DomainsApi(api_client)
    id = 'id_example' # str | 
    update_domain_request = moonemail.UpdateDomainRequest() # UpdateDomainRequest | 

    try:
        # Update domain
        api_response = api_instance.update_domain(id, update_domain_request)
        print("The response of DomainsApi->update_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_domain_request** | [**UpdateDomainRequest**](UpdateDomainRequest.md)|  | 

### Return type

[**UpdateDomain200Response**](UpdateDomain200Response.md)

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

# **verify_domain**
> UpdateDomain200Response verify_domain(id)

Verify domain

Request a fresh verification check after publishing DNS records.

Required permission: `domains:write`.

### Example

* Bearer Authentication (bearerKey):

```python
import moonemail
from moonemail.models.update_domain200_response import UpdateDomain200Response
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
    api_instance = moonemail.DomainsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Verify domain
        api_response = api_instance.verify_domain(id)
        print("The response of DomainsApi->verify_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->verify_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UpdateDomain200Response**](UpdateDomain200Response.md)

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

