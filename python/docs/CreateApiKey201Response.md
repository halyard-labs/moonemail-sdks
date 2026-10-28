# CreateApiKey201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**token** | **str** | Returned once. Save securely. | 
**hint** | **str** |  | 
**permission** | **str** |  | 
**scopes** | **List[str]** |  | 
**expires_at** | **str** |  | 

## Example

```python
from moonemail.models.create_api_key201_response import CreateApiKey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKey201Response from a JSON string
create_api_key201_response_instance = CreateApiKey201Response.from_json(json)
# print the JSON string representation of the object
print(CreateApiKey201Response.to_json())

# convert the object into a dict
create_api_key201_response_dict = create_api_key201_response_instance.to_dict()
# create an instance of CreateApiKey201Response from a dict
create_api_key201_response_from_dict = CreateApiKey201Response.from_dict(create_api_key201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


