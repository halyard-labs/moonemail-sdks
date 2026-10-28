# ListReceivedAttachments200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**HasMore** | **bool** |  | 
**Data** | [**[]ListReceivedEmails200ResponseDataInnerAttachmentsInner**](ListReceivedEmails200ResponseDataInnerAttachmentsInner.md) |  | 

## Methods

### NewListReceivedAttachments200Response

`func NewListReceivedAttachments200Response(object string, hasMore bool, data []ListReceivedEmails200ResponseDataInnerAttachmentsInner, ) *ListReceivedAttachments200Response`

NewListReceivedAttachments200Response instantiates a new ListReceivedAttachments200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListReceivedAttachments200ResponseWithDefaults

`func NewListReceivedAttachments200ResponseWithDefaults() *ListReceivedAttachments200Response`

NewListReceivedAttachments200ResponseWithDefaults instantiates a new ListReceivedAttachments200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListReceivedAttachments200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListReceivedAttachments200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListReceivedAttachments200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetHasMore

`func (o *ListReceivedAttachments200Response) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *ListReceivedAttachments200Response) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *ListReceivedAttachments200Response) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.


### GetData

`func (o *ListReceivedAttachments200Response) GetData() []ListReceivedEmails200ResponseDataInnerAttachmentsInner`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ListReceivedAttachments200Response) GetDataOk() (*[]ListReceivedEmails200ResponseDataInnerAttachmentsInner, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ListReceivedAttachments200Response) SetData(v []ListReceivedEmails200ResponseDataInnerAttachmentsInner)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


