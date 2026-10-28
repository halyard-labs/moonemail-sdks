# ListReceivedAttachments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**has_more** | **bool** |  | 
**data** | [**List[ListReceivedEmails200ResponseDataInnerAttachmentsInner]**](ListReceivedEmails200ResponseDataInnerAttachmentsInner.md) |  | 

## Example

```python
from moonemail.models.list_received_attachments200_response import ListReceivedAttachments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceivedAttachments200Response from a JSON string
list_received_attachments200_response_instance = ListReceivedAttachments200Response.from_json(json)
# print the JSON string representation of the object
print(ListReceivedAttachments200Response.to_json())

# convert the object into a dict
list_received_attachments200_response_dict = list_received_attachments200_response_instance.to_dict()
# create an instance of ListReceivedAttachments200Response from a dict
list_received_attachments200_response_from_dict = ListReceivedAttachments200Response.from_dict(list_received_attachments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


