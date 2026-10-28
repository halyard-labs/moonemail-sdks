# ListEmails200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**HasMore** | **bool** |  | 
**Data** | [**[]ListEmails200ResponseDataInner**](ListEmails200ResponseDataInner.md) |  | 

## Methods

### NewListEmails200Response

`func NewListEmails200Response(object string, hasMore bool, data []ListEmails200ResponseDataInner, ) *ListEmails200Response`

NewListEmails200Response instantiates a new ListEmails200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListEmails200ResponseWithDefaults

`func NewListEmails200ResponseWithDefaults() *ListEmails200Response`

NewListEmails200ResponseWithDefaults instantiates a new ListEmails200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListEmails200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListEmails200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListEmails200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetHasMore

`func (o *ListEmails200Response) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *ListEmails200Response) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *ListEmails200Response) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.


### GetData

`func (o *ListEmails200Response) GetData() []ListEmails200ResponseDataInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListEmails200Response) GetDataOk() (*[]ListEmails200ResponseDataInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ListEmails200Response) SetData(v []ListEmails200ResponseDataInner)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


