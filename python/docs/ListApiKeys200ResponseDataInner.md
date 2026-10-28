# ListApiKeys200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**permission** | **str** |  | 
**scopes** | **List[str]** |  | [optional] 
**domain_id** | **str** |  | 
**hint** | **str** |  | 
**created_at** | **str** |  | 
**last_used_at** | **str** |  | 
**expires_at** | **str** |  | 

## Example

```python
from moonemail.models.list_api_keys200_response_data_inner import ListApiKeys200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListApiKeys200ResponseDataInner from a JSON string
list_api_keys200_response_data_inner_instance = ListApiKeys200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListApiKeys200ResponseDataInner.to_json())

# convert the object into a dict
list_api_keys200_response_data_inner_dict = list_api_keys200_response_data_inner_instance.to_dict()
# create an instance of ListApiKeys200ResponseDataInner from a dict
list_api_keys200_response_data_inner_from_dict = ListApiKeys200ResponseDataInner.from_dict(list_api_keys200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


