# ListEmails200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**message_id** | **str** |  | 
**to** | **List[str]** |  | 
**var_from** | **str** |  | 
**created_at** | **str** |  | 
**subject** | **str** |  | 
**bcc** | **List[str]** |  | 
**cc** | **List[str]** |  | 
**reply_to** | **List[str]** |  | 
**last_event** | **str** |  | 
**scheduled_at** | **str** |  | 

## Example

```python
from moonemail.models.list_emails200_response_data_inner import ListEmails200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListEmails200ResponseDataInner from a JSON string
list_emails200_response_data_inner_instance = ListEmails200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListEmails200ResponseDataInner.to_json())

# convert the object into a dict
list_emails200_response_data_inner_dict = list_emails200_response_data_inner_instance.to_dict()
# create an instance of ListEmails200ResponseDataInner from a dict
list_emails200_response_data_inner_from_dict = ListEmails200ResponseDataInner.from_dict(list_emails200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


