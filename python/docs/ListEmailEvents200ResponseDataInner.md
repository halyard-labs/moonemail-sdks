# ListEmailEvents200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**created_at** | **str** |  | 
**data** | [**ListEmailEvents200ResponseDataInnerData**](ListEmailEvents200ResponseDataInnerData.md) |  | 

## Example

```python
from moonemail.models.list_email_events200_response_data_inner import ListEmailEvents200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListEmailEvents200ResponseDataInner from a JSON string
list_email_events200_response_data_inner_instance = ListEmailEvents200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListEmailEvents200ResponseDataInner.to_json())

# convert the object into a dict
list_email_events200_response_data_inner_dict = list_email_events200_response_data_inner_instance.to_dict()
# create an instance of ListEmailEvents200ResponseDataInner from a dict
list_email_events200_response_data_inner_from_dict = ListEmailEvents200ResponseDataInner.from_dict(list_email_events200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


