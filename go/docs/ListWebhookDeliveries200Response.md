# ListWebhookDeliveries200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**HasMore** | **bool** |  | 
**Data** | [**[]ListWebhookDeliveries200ResponseDataInner**](ListWebhookDeliveries200ResponseDataInner.md) |  | 

## Methods

### NewListWebhookDeliveries200Response

`func NewListWebhookDeliveries200Response(object string, hasMore bool, data []ListWebhookDeliveries200ResponseDataInner, ) *ListWebhookDeliveries200Response`

NewListWebhookDeliveries200Response instantiates a new ListWebhookDeliveries200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhookDeliveries200ResponseWithDefaults

`func NewListWebhookDeliveries200ResponseWithDefaults() *ListWebhookDeliveries200Response`

NewListWebhookDeliveries200ResponseWithDefaults instantiates a new ListWebhookDeliveries200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListWebhookDeliveries200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListWebhookDeliveries200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListWebhookDeliveries200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetHasMore

`func (o *ListWebhookDeliveries200Response) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *ListWebhookDeliveries200Response) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *ListWebhookDeliveries200Response) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.


### GetData

`func (o *ListWebhookDeliveries200Response) GetData() []ListWebhookDeliveries200ResponseDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListWebhookDeliveries200Response) GetDataOk() (*[]ListWebhookDeliveries200ResponseDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ListWebhookDeliveries200Response) SetData(v []ListWebhookDeliveries200ResponseDataInner)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


