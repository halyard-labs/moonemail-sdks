# ListDomains200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**region** | **str** |  | 

## Example

```python
from moonemail.models.list_domains200_response_data_inner import ListDomains200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomains200ResponseDataInner from a JSON string
list_domains200_response_data_inner_instance = ListDomains200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListDomains200ResponseDataInner.to_json())

# convert the object into a dict
list_domains200_response_data_inner_dict = list_domains200_response_data_inner_instance.to_dict()
# create an instance of ListDomains200ResponseDataInner from a dict
list_domains200_response_data_inner_from_dict = ListDomains200ResponseDataInner.from_dict(list_domains200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


