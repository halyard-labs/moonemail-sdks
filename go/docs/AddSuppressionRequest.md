# AddSuppressionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | **string** |  | 
**Reason** | Pointer to **string** |  | [optional] 

## Methods

### NewAddSuppressionRequest

`func NewAddSuppressionRequest(email string, ) *AddSuppressionRequest`

NewAddSuppressionRequest instantiates a new AddSuppressionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddSuppressionRequestWithDefaults

`func NewAddSuppressionRequestWithDefaults() *AddSuppressionRequest`

NewAddSuppressionRequestWithDefaults instantiates a new AddSuppressionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEmail

`func (o *AddSuppressionRequest) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *AddSuppressionRequest) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *AddSuppressionRequest) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetReason

`func (o *AddSuppressionRequest) GetReason() string`

GetReason returns the Reason field if non-nil, zero value otherwise.

### GetReasonOk

`func (o *AddSuppressionRequest) GetReasonOk() (*string, bool)`

GetReasonOk returns a tuple with the Reason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReason

`func (o *AddSuppressionRequest) SetReason(v string)`

SetReason sets Reason field to given value.

### HasReason

`func (o *AddSuppressionRequest) HasReason() bool`

HasReason returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


