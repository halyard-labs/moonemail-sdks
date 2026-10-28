# ListSuppressions200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**reason** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from moonemail.models.list_suppressions200_response_data_inner import ListSuppressions200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListSuppressions200ResponseDataInner from a JSON string
list_suppressions200_response_data_inner_instance = ListSuppressions200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListSuppressions200ResponseDataInner.to_json())

# convert the object into a dict
list_suppressions200_response_data_inner_dict = list_suppressions200_response_data_inner_instance.to_dict()
# create an instance of ListSuppressions200ResponseDataInner from a dict
list_suppressions200_response_data_inner_from_dict = ListSuppressions200ResponseDataInner.from_dict(list_suppressions200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


