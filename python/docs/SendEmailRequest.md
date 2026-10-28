# SendEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | 
**subject** | **str** |  | 
**bcc** | [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | [optional] 
**cc** | [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | [optional] 
**reply_to** | [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | [optional] 
**html** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**attachments** | [**List[SendEmailRequestAttachmentsInner]**](SendEmailRequestAttachmentsInner.md) |  | [optional] 
**tags** | [**List[SendEmailRequestTagsInner]**](SendEmailRequestTagsInner.md) |  | [optional] 
**scheduled_at** | **str** |  | [optional] 

## Example

```python
from moonemail.models.send_email_request import SendEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailRequest from a JSON string
send_email_request_instance = SendEmailRequest.from_json(json)
# print the JSON string representation of the object
print(SendEmailRequest.to_json())

# convert the object into a dict
send_email_request_dict = send_email_request_instance.to_dict()
# create an instance of SendEmailRequest from a dict
send_email_request_from_dict = SendEmailRequest.from_dict(send_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


