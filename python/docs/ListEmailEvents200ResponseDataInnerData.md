# ListEmailEvents200ResponseDataInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounce** | [**ListEmailEvents200ResponseDataInnerDataBounce**](ListEmailEvents200ResponseDataInnerDataBounce.md) |  | [optional] 
**click** | [**ListEmailEvents200ResponseDataInnerDataClick**](ListEmailEvents200ResponseDataInnerDataClick.md) |  | [optional] 
**failed** | [**ListEmailEvents200ResponseDataInnerDataFailed**](ListEmailEvents200ResponseDataInnerDataFailed.md) |  | [optional] 
**suppressed** | [**ListEmailEvents200ResponseDataInnerDataFailed**](ListEmailEvents200ResponseDataInnerDataFailed.md) |  | [optional] 

## Example

```python
from moonemail.models.list_email_events200_response_data_inner_data import ListEmailEvents200ResponseDataInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of ListEmailEvents200ResponseDataInnerData from a JSON string
list_email_events200_response_data_inner_data_instance = ListEmailEvents200ResponseDataInnerData.from_json(json)
# print the JSON string representation of the object
print(ListEmailEvents200ResponseDataInnerData.to_json())

# convert the object into a dict
list_email_events200_response_data_inner_data_dict = list_email_events200_response_data_inner_data_instance.to_dict()
# create an instance of ListEmailEvents200ResponseDataInnerData from a dict
list_email_events200_response_data_inner_data_from_dict = ListEmailEvents200ResponseDataInnerData.from_dict(list_email_events200_response_data_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


