# ListWebhooks200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**HasMore** | **bool** |  | 
**Data** | [**[]ListWebhooks200ResponseDataInner**](ListWebhooks200ResponseDataInner.md) |  | 

## Methods

### NewListWebhooks200Response

`func NewListWebhooks200Response(object string, hasMore bool, data []ListWebhooks200ResponseDataInner, ) *ListWebhooks200Response`

NewListWebhooks200Response instantiates a new ListWebhooks200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhooks200ResponseWithDefaults

`func NewListWebhooks200ResponseWithDefaults() *ListWebhooks200Response`

NewListWebhooks200ResponseWithDefaults instantiates a new ListWebhooks200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListWebhooks200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListWebhooks200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListWebhooks200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetHasMore

`func (o *ListWebhooks200Response) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *ListWebhooks200Response) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *ListWebhooks200Response) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.


### GetData

`func (o *ListWebhooks200Response) GetData() []ListWebhooks200ResponseDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListWebhooks200Response) GetDataOk() (*[]ListWebhooks200ResponseDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ListWebhooks200Response) SetData(v []ListWebhooks200ResponseDataInner)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


