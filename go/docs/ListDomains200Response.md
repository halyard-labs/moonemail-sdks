# ListDomains200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**HasMore** | **bool** |  | 
**Data** | [**[]ListDomains200ResponseDataInner**](ListDomains200ResponseDataInner.md) |  | 

## Methods

### NewListDomains200Response

`func NewListDomains200Response(object string, hasMore bool, data []ListDomains200ResponseDataInner, ) *ListDomains200Response`

NewListDomains200Response instantiates a new ListDomains200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListDomains200ResponseWithDefaults

`func NewListDomains200ResponseWithDefaults() *ListDomains200Response`

NewListDomains200ResponseWithDefaults instantiates a new ListDomains200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListDomains200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListDomains200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListDomains200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetHasMore

`func (o *ListDomains200Response) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *ListDomains200Response) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *ListDomains200Response) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.


### GetData

`func (o *ListDomains200Response) GetData() []ListDomains200ResponseDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListDomains200Response) GetDataOk() (*[]ListDomains200ResponseDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ListDomains200Response) SetData(v []ListDomains200ResponseDataInner)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


