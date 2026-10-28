# ListInboxes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**has_more** | **bool** |  | 
**data** | [**List[ListInboxes200ResponseDataInner]**](ListInboxes200ResponseDataInner.md) |  | 

## Example

```python
from moonemail.models.list_inboxes200_response import ListInboxes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListInboxes200Response from a JSON string
list_inboxes200_response_instance = ListInboxes200Response.from_json(json)
# print the JSON string representation of the object
print(ListInboxes200Response.to_json())

# convert the object into a dict
list_inboxes200_response_dict = list_inboxes200_response_instance.to_dict()
# create an instance of ListInboxes200Response from a dict
list_inboxes200_response_from_dict = ListInboxes200Response.from_dict(list_inboxes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


