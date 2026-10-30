# ListInboxes200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**address** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**aliases** | **List[str]** |  | [optional] 
**domain_id** | **str** |  | [optional] 

## Example

```python
from moonemail.models.list_inboxes200_response_data_inner import ListInboxes200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListInboxes200ResponseDataInner from a JSON string
list_inboxes200_response_data_inner_instance = ListInboxes200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListInboxes200ResponseDataInner.to_json())

# convert the object into a dict
list_inboxes200_response_data_inner_dict = list_inboxes200_response_data_inner_instance.to_dict()
# create an instance of ListInboxes200ResponseDataInner from a dict
list_inboxes200_response_data_inner_from_dict = ListInboxes200ResponseDataInner.from_dict(list_inboxes200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


