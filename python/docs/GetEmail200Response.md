# GetEmail200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**message_id** | **str** |  | 
**to** | **List[str]** |  | 
**var_from** | **str** |  | 
**created_at** | **str** |  | 
**subject** | **str** |  | 
**bcc** | **List[str]** |  | 
**cc** | **List[str]** |  | 
**reply_to** | **List[str]** |  | 
**last_event** | **str** |  | 
**scheduled_at** | **str** |  | 
**object** | **str** |  | 
**html** | **str** |  | 
**text** | **str** |  | 
**tags** | [**List[GetEmail200ResponseTagsInner]**](GetEmail200ResponseTagsInner.md) |  | 

## Example

```python
from moonemail.models.get_email200_response import GetEmail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmail200Response from a JSON string
get_email200_response_instance = GetEmail200Response.from_json(json)
# print the JSON string representation of the object
print(GetEmail200Response.to_json())

# convert the object into a dict
get_email200_response_dict = get_email200_response_instance.to_dict()
# create an instance of GetEmail200Response from a dict
get_email200_response_from_dict = GetEmail200Response.from_dict(get_email200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


