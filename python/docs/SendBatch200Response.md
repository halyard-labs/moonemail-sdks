# SendBatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SendEmail200Response]**](SendEmail200Response.md) |  | 

## Example

```python
from moonemail.models.send_batch200_response import SendBatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendBatch200Response from a JSON string
send_batch200_response_instance = SendBatch200Response.from_json(json)
# print the JSON string representation of the object
print(SendBatch200Response.to_json())

# convert the object into a dict
send_batch200_response_dict = send_batch200_response_instance.to_dict()
# create an instance of SendBatch200Response from a dict
send_batch200_response_from_dict = SendBatch200Response.from_dict(send_batch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


