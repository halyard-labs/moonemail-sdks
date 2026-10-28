# CreateInbox200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**address** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**aliases** | **List[str]** |  | [optional] 

## Example

```python
from moonemail.models.create_inbox200_response import CreateInbox200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInbox200Response from a JSON string
create_inbox200_response_instance = CreateInbox200Response.from_json(json)
# print the JSON string representation of the object
print(CreateInbox200Response.to_json())

# convert the object into a dict
create_inbox200_response_dict = create_inbox200_response_instance.to_dict()
# create an instance of CreateInbox200Response from a dict
create_inbox200_response_from_dict = CreateInbox200Response.from_dict(create_inbox200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


