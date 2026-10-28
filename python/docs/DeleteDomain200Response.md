# DeleteDomain200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**deleted** | **bool** |  | 

## Example

```python
from moonemail.models.delete_domain200_response import DeleteDomain200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomain200Response from a JSON string
delete_domain200_response_instance = DeleteDomain200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteDomain200Response.to_json())

# convert the object into a dict
delete_domain200_response_dict = delete_domain200_response_instance.to_dict()
# create an instance of DeleteDomain200Response from a dict
delete_domain200_response_from_dict = DeleteDomain200Response.from_dict(delete_domain200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


