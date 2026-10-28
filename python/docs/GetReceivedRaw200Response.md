# GetReceivedRaw200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | Private signed URL. Expires within five minutes; treat as a credential. | 
**expires_at** | **str** |  | 

## Example

```python
from moonemail.models.get_received_raw200_response import GetReceivedRaw200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceivedRaw200Response from a JSON string
get_received_raw200_response_instance = GetReceivedRaw200Response.from_json(json)
# print the JSON string representation of the object
print(GetReceivedRaw200Response.to_json())

# convert the object into a dict
get_received_raw200_response_dict = get_received_raw200_response_instance.to_dict()
# create an instance of GetReceivedRaw200Response from a dict
get_received_raw200_response_from_dict = GetReceivedRaw200Response.from_dict(get_received_raw200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


