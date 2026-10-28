# ListReceivedEmails200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**inbox_id** | **str** |  | 
**var_from** | **str** |  | 
**to** | **List[str]** |  | 
**subject** | **str** |  | 
**message_id** | **str** |  | 
**created_at** | **str** |  | 
**status** | **str** |  | 
**quarantine_reason** | **str** |  | [optional] 
**attachments** | [**List[ListReceivedEmails200ResponseDataInnerAttachmentsInner]**](ListReceivedEmails200ResponseDataInnerAttachmentsInner.md) |  | 
**expires_at** | **int** | Expiry as Unix seconds. | 
**authentication** | [**ListReceivedEmails200ResponseDataInnerAuthentication**](ListReceivedEmails200ResponseDataInnerAuthentication.md) |  | [optional] 

## Example

```python
from moonemail.models.list_received_emails200_response_data_inner import ListReceivedEmails200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceivedEmails200ResponseDataInner from a JSON string
list_received_emails200_response_data_inner_instance = ListReceivedEmails200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListReceivedEmails200ResponseDataInner.to_json())

# convert the object into a dict
list_received_emails200_response_data_inner_dict = list_received_emails200_response_data_inner_instance.to_dict()
# create an instance of ListReceivedEmails200ResponseDataInner from a dict
list_received_emails200_response_data_inner_from_dict = ListReceivedEmails200ResponseDataInner.from_dict(list_received_emails200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


