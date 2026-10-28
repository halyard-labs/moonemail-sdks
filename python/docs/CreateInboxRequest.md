# CreateInboxRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from moonemail.models.create_inbox_request import CreateInboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInboxRequest from a JSON string
create_inbox_request_instance = CreateInboxRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInboxRequest.to_json())

# convert the object into a dict
create_inbox_request_dict = create_inbox_request_instance.to_dict()
# create an instance of CreateInboxRequest from a dict
create_inbox_request_from_dict = CreateInboxRequest.from_dict(create_inbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


