# ListWebhookDeliveries200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** |  | 
**event_id** | **str** |  | 
**event_type** | **str** |  | 
**email_id** | **str** |  | 
**attempt** | **int** |  | 
**status_code** | **int** | Zero when no HTTP response was received. | 
**ok** | **bool** |  | 
**duration_ms** | **int** |  | 
**error** | **str** |  | [optional] 
**created_at** | **str** |  | 

## Example

```python
from moonemail.models.list_webhook_deliveries200_response_data_inner import ListWebhookDeliveries200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookDeliveries200ResponseDataInner from a JSON string
list_webhook_deliveries200_response_data_inner_instance = ListWebhookDeliveries200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListWebhookDeliveries200ResponseDataInner.to_json())

# convert the object into a dict
list_webhook_deliveries200_response_data_inner_dict = list_webhook_deliveries200_response_data_inner_instance.to_dict()
# create an instance of ListWebhookDeliveries200ResponseDataInner from a dict
list_webhook_deliveries200_response_data_inner_from_dict = ListWebhookDeliveries200ResponseDataInner.from_dict(list_webhook_deliveries200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


