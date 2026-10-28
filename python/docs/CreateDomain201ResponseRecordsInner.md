# CreateDomain201ResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**ttl** | **str** |  | 
**status** | **str** |  | 
**value** | **str** |  | 
**priority** | **int** |  | [optional] 

## Example

```python
from moonemail.models.create_domain201_response_records_inner import CreateDomain201ResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomain201ResponseRecordsInner from a JSON string
create_domain201_response_records_inner_instance = CreateDomain201ResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(CreateDomain201ResponseRecordsInner.to_json())

# convert the object into a dict
create_domain201_response_records_inner_dict = create_domain201_response_records_inner_instance.to_dict()
# create an instance of CreateDomain201ResponseRecordsInner from a dict
create_domain201_response_records_inner_from_dict = CreateDomain201ResponseRecordsInner.from_dict(create_domain201_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


