# ListReceivingDomains200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**HasMore** | **bool** |  | 
**Data** | [**[]PrepareReceivingDomain200Response**](PrepareReceivingDomain200Response.md) |  | 

## Methods

### NewListReceivingDomains200Response

`func NewListReceivingDomains200Response(object string, hasMore bool, data []PrepareReceivingDomain200Response, ) *ListReceivingDomains200Response`

NewListReceivingDomains200Response instantiates a new ListReceivingDomains200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListReceivingDomains200ResponseWithDefaults

`func NewListReceivingDomains200ResponseWithDefaults() *ListReceivingDomains200Response`

NewListReceivingDomains200ResponseWithDefaults instantiates a new ListReceivingDomains200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListReceivingDomains200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListReceivingDomains200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListReceivingDomains200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetHasMore

`func (o *ListReceivingDomains200Response) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *ListReceivingDomains200Response) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *ListReceivingDomains200Response) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.


### GetData

`func (o *ListReceivingDomains200Response) GetData() []PrepareReceivingDomain200Response`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListReceivingDomains200Response) GetDataOk() (*[]PrepareReceivingDomain200Response, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ListReceivingDomains200Response) SetData(v []PrepareReceivingDomain200Response)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


