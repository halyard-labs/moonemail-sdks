# ListReceivedEmails200ResponseDataInnerAuthentication

Provider receipt verdicts; not sender-supplied headers. Older messages may omit this.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spf** | **str** |  | 
**dkim** | **str** |  | 
**dmarc** | **str** |  | 

## Example

```python
from moonemail.models.list_received_emails200_response_data_inner_authentication import ListReceivedEmails200ResponseDataInnerAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceivedEmails200ResponseDataInnerAuthentication from a JSON string
list_received_emails200_response_data_inner_authentication_instance = ListReceivedEmails200ResponseDataInnerAuthentication.from_json(json)
# print the JSON string representation of the object
print(ListReceivedEmails200ResponseDataInnerAuthentication.to_json())

# convert the object into a dict
list_received_emails200_response_data_inner_authentication_dict = list_received_emails200_response_data_inner_authentication_instance.to_dict()
# create an instance of ListReceivedEmails200ResponseDataInnerAuthentication from a dict
list_received_emails200_response_data_inner_authentication_from_dict = ListReceivedEmails200ResponseDataInnerAuthentication.from_dict(list_received_emails200_response_data_inner_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


