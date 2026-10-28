# DeleteApiKey200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**deleted** | **bool** |  | 

## Example

```python
from moonemail.models.delete_api_key200_response import DeleteApiKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteApiKey200Response from a JSON string
delete_api_key200_response_instance = DeleteApiKey200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteApiKey200Response.to_json())

# convert the object into a dict
delete_api_key200_response_dict = delete_api_key200_response_instance.to_dict()
# create an instance of DeleteApiKey200Response from a dict
delete_api_key200_response_from_dict = DeleteApiKey200Response.from_dict(delete_api_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


