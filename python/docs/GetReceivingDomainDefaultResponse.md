# GetReceivingDomainDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**name** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from moonemail.models.get_receiving_domain_default_response import GetReceivingDomainDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceivingDomainDefaultResponse from a JSON string
get_receiving_domain_default_response_instance = GetReceivingDomainDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(GetReceivingDomainDefaultResponse.to_json())

# convert the object into a dict
get_receiving_domain_default_response_dict = get_receiving_domain_default_response_instance.to_dict()
# create an instance of GetReceivingDomainDefaultResponse from a dict
get_receiving_domain_default_response_from_dict = GetReceivingDomainDefaultResponse.from_dict(get_receiving_domain_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


