# ListEmailEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**has_more** | **bool** |  | 
**data** | [**List[ListEmailEvents200ResponseDataInner]**](ListEmailEvents200ResponseDataInner.md) |  | 

## Example

```python
from moonemail.models.list_email_events200_response import ListEmailEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListEmailEvents200Response from a JSON string
list_email_events200_response_instance = ListEmailEvents200Response.from_json(json)
# print the JSON string representation of the object
print(ListEmailEvents200Response.to_json())

# convert the object into a dict
list_email_events200_response_dict = list_email_events200_response_instance.to_dict()
# create an instance of ListEmailEvents200Response from a dict
list_email_events200_response_from_dict = ListEmailEvents200Response.from_dict(list_email_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


