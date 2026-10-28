# UpdateInboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from moonemail.models.update_inbox_request import UpdateInboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInboxRequest from a JSON string
update_inbox_request_instance = UpdateInboxRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInboxRequest.to_json())

# convert the object into a dict
update_inbox_request_dict = update_inbox_request_instance.to_dict()
# create an instance of UpdateInboxRequest from a dict
update_inbox_request_from_dict = UpdateInboxRequest.from_dict(update_inbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


