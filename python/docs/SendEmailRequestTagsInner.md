# SendEmailRequestTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from moonemail.models.send_email_request_tags_inner import SendEmailRequestTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailRequestTagsInner from a JSON string
send_email_request_tags_inner_instance = SendEmailRequestTagsInner.from_json(json)
# print the JSON string representation of the object
print(SendEmailRequestTagsInner.to_json())

# convert the object into a dict
send_email_request_tags_inner_dict = send_email_request_tags_inner_instance.to_dict()
# create an instance of SendEmailRequestTagsInner from a dict
send_email_request_tags_inner_from_dict = SendEmailRequestTagsInner.from_dict(send_email_request_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


