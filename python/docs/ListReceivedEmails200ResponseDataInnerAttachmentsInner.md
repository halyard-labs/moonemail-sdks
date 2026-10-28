# ListReceivedEmails200ResponseDataInnerAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**filename** | **str** |  | 
**content_type** | **str** |  | 
**content_disposition** | **str** |  | 
**content_id** | **str** |  | [optional] 
**size** | **int** |  | 

## Example

```python
from moonemail.models.list_received_emails200_response_data_inner_attachments_inner import ListReceivedEmails200ResponseDataInnerAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceivedEmails200ResponseDataInnerAttachmentsInner from a JSON string
list_received_emails200_response_data_inner_attachments_inner_instance = ListReceivedEmails200ResponseDataInnerAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(ListReceivedEmails200ResponseDataInnerAttachmentsInner.to_json())

# convert the object into a dict
list_received_emails200_response_data_inner_attachments_inner_dict = list_received_emails200_response_data_inner_attachments_inner_instance.to_dict()
# create an instance of ListReceivedEmails200ResponseDataInnerAttachmentsInner from a dict
list_received_emails200_response_data_inner_attachments_inner_from_dict = ListReceivedEmails200ResponseDataInnerAttachmentsInner.from_dict(list_received_emails200_response_data_inner_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


