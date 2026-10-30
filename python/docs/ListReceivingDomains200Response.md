# ListReceivingDomains200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**has_more** | **bool** |  | 
**data** | [**List[PrepareReceivingDomain200Response]**](PrepareReceivingDomain200Response.md) |  | 

## Example

```python
from moonemail.models.list_receiving_domains200_response import ListReceivingDomains200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceivingDomains200Response from a JSON string
list_receiving_domains200_response_instance = ListReceivingDomains200Response.from_json(json)
# print the JSON string representation of the object
print(ListReceivingDomains200Response.to_json())

# convert the object into a dict
list_receiving_domains200_response_dict = list_receiving_domains200_response_instance.to_dict()
# create an instance of ListReceivingDomains200Response from a dict
list_receiving_domains200_response_from_dict = ListReceivingDomains200Response.from_dict(list_receiving_domains200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


