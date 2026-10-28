# GetReceivedAttachment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**filename** | **str** |  | 
**content_type** | **str** |  | 
**content_disposition** | **str** |  | 
**content_id** | **str** |  | [optional] 
**size** | **int** |  | 
**download_url** | **str** | Private signed URL. Expires within five minutes; treat as a credential. | 
**expires_at** | **str** |  | 

## Example

```python
from moonemail.models.get_received_attachment200_response import GetReceivedAttachment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceivedAttachment200Response from a JSON string
get_received_attachment200_response_instance = GetReceivedAttachment200Response.from_json(json)
# print the JSON string representation of the object
print(GetReceivedAttachment200Response.to_json())

# convert the object into a dict
get_received_attachment200_response_dict = get_received_attachment200_response_instance.to_dict()
# create an instance of GetReceivedAttachment200Response from a dict
get_received_attachment200_response_from_dict = GetReceivedAttachment200Response.from_dict(get_received_attachment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


