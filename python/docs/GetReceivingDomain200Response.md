# GetReceivingDomain200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**verified_until** | **int** |  | 
**created_at** | **str** |  | 
**records** | [**List[GetReceivingDomain200ResponseRecordsInner]**](GetReceivingDomain200ResponseRecordsInner.md) |  | 

## Example

```python
from moonemail.models.get_receiving_domain200_response import GetReceivingDomain200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceivingDomain200Response from a JSON string
get_receiving_domain200_response_instance = GetReceivingDomain200Response.from_json(json)
# print the JSON string representation of the object
print(GetReceivingDomain200Response.to_json())

# convert the object into a dict
get_receiving_domain200_response_dict = get_receiving_domain200_response_instance.to_dict()
# create an instance of GetReceivingDomain200Response from a dict
get_receiving_domain200_response_from_dict = GetReceivingDomain200Response.from_dict(get_receiving_domain200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


