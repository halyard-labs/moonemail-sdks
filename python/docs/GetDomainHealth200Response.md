# GetDomainHealth200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_at** | **str** |  | 
**sending_enabled** | **bool** |  | 
**metrics_enabled** | **bool** |  | 
**sending_suspended** | **bool** |  | 
**bounce** | [**GetDomainHealth200ResponseBounce**](GetDomainHealth200ResponseBounce.md) |  | 
**complaint** | [**GetDomainHealth200ResponseBounce**](GetDomainHealth200ResponseBounce.md) |  | 

## Example

```python
from moonemail.models.get_domain_health200_response import GetDomainHealth200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainHealth200Response from a JSON string
get_domain_health200_response_instance = GetDomainHealth200Response.from_json(json)
# print the JSON string representation of the object
print(GetDomainHealth200Response.to_json())

# convert the object into a dict
get_domain_health200_response_dict = get_domain_health200_response_instance.to_dict()
# create an instance of GetDomainHealth200Response from a dict
get_domain_health200_response_from_dict = GetDomainHealth200Response.from_dict(get_domain_health200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


