# GetReceivedEmail200Response

Content fields are omitted for quarantined messages.

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
**html** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**headers** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from moonemail.models.get_received_email200_response import GetReceivedEmail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceivedEmail200Response from a JSON string
get_received_email200_response_instance = GetReceivedEmail200Response.from_json(json)
# print the JSON string representation of the object
print(GetReceivedEmail200Response.to_json())

# convert the object into a dict
get_received_email200_response_dict = get_received_email200_response_instance.to_dict()
# create an instance of GetReceivedEmail200Response from a dict
get_received_email200_response_from_dict = GetReceivedEmail200Response.from_dict(get_received_email200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


