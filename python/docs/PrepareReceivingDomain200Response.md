# PrepareReceivingDomain200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**verified_until** | **int** |  | 
**created_at** | **str** |  | 
**records** | [**List[PrepareReceivingDomain200ResponseRecordsInner]**](PrepareReceivingDomain200ResponseRecordsInner.md) |  | 

## Example

```python
from moonemail.models.prepare_receiving_domain200_response import PrepareReceivingDomain200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareReceivingDomain200Response from a JSON string
prepare_receiving_domain200_response_instance = PrepareReceivingDomain200Response.from_json(json)
# print the JSON string representation of the object
print(PrepareReceivingDomain200Response.to_json())

# convert the object into a dict
prepare_receiving_domain200_response_dict = prepare_receiving_domain200_response_instance.to_dict()
# create an instance of PrepareReceivingDomain200Response from a dict
prepare_receiving_domain200_response_from_dict = PrepareReceivingDomain200Response.from_dict(prepare_receiving_domain200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


