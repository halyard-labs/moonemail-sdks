# GetDomainHealth200ResponseBounce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | Fraction, not percentage. Null means no usable sample. | 
**observed_at** | **str** |  | 
**state** | **str** |  | 
**review_threshold** | **float** |  | 

## Example

```python
from moonemail.models.get_domain_health200_response_bounce import GetDomainHealth200ResponseBounce

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainHealth200ResponseBounce from a JSON string
get_domain_health200_response_bounce_instance = GetDomainHealth200ResponseBounce.from_json(json)
# print the JSON string representation of the object
print(GetDomainHealth200ResponseBounce.to_json())

# convert the object into a dict
get_domain_health200_response_bounce_dict = get_domain_health200_response_bounce_instance.to_dict()
# create an instance of GetDomainHealth200ResponseBounce from a dict
get_domain_health200_response_bounce_from_dict = GetDomainHealth200ResponseBounce.from_dict(get_domain_health200_response_bounce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


