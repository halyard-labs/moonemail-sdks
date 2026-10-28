# ListWebhooks200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**endpoint** | **str** |  | 
**events** | **List[str]** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**signing_secret** | **str** | Only revealed to dashboard user sessions; never returned by API-key reads. | [optional] 

## Example

```python
from moonemail.models.list_webhooks200_response_data_inner import ListWebhooks200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhooks200ResponseDataInner from a JSON string
list_webhooks200_response_data_inner_instance = ListWebhooks200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListWebhooks200ResponseDataInner.to_json())

# convert the object into a dict
list_webhooks200_response_data_inner_dict = list_webhooks200_response_data_inner_instance.to_dict()
# create an instance of ListWebhooks200ResponseDataInner from a dict
list_webhooks200_response_data_inner_from_dict = ListWebhooks200ResponseDataInner.from_dict(list_webhooks200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


