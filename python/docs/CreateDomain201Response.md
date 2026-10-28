# CreateDomain201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**region** | **str** |  | 
**object** | **str** |  | 
**open_tracking** | **bool** |  | 
**click_tracking** | **bool** |  | 
**tracking_subdomain** | **str** |  | 
**custom_return_path** | **str** |  | 
**tls** | **str** |  | 
**capabilities** | [**CreateDomain201ResponseCapabilities**](CreateDomain201ResponseCapabilities.md) |  | 
**records** | [**List[CreateDomain201ResponseRecordsInner]**](CreateDomain201ResponseRecordsInner.md) |  | 

## Example

```python
from moonemail.models.create_domain201_response import CreateDomain201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomain201Response from a JSON string
create_domain201_response_instance = CreateDomain201Response.from_json(json)
# print the JSON string representation of the object
print(CreateDomain201Response.to_json())

# convert the object into a dict
create_domain201_response_dict = create_domain201_response_instance.to_dict()
# create an instance of CreateDomain201Response from a dict
create_domain201_response_from_dict = CreateDomain201Response.from_dict(create_domain201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


