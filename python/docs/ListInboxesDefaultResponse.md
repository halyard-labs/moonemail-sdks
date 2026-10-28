# ListInboxesDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**name** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from moonemail.models.list_inboxes_default_response import ListInboxesDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInboxesDefaultResponse from a JSON string
list_inboxes_default_response_instance = ListInboxesDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(ListInboxesDefaultResponse.to_json())

# convert the object into a dict
list_inboxes_default_response_dict = list_inboxes_default_response_instance.to_dict()
# create an instance of ListInboxesDefaultResponse from a dict
list_inboxes_default_response_from_dict = ListInboxesDefaultResponse.from_dict(list_inboxes_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


