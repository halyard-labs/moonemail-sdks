# UpdateEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_at** | **str** |  | 

## Example

```python
from moonemail.models.update_email_request import UpdateEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailRequest from a JSON string
update_email_request_instance = UpdateEmailRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailRequest.to_json())

# convert the object into a dict
update_email_request_dict = update_email_request_instance.to_dict()
# create an instance of UpdateEmailRequest from a dict
update_email_request_from_dict = UpdateEmailRequest.from_dict(update_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


