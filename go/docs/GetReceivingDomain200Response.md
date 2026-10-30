# GetReceivingDomain200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DomainId** | **string** |  | 
**Name** | **string** |  | 
**Status** | **string** |  | 
**VerifiedUntil** | **int32** |  | 
**CreatedAt** | **string** |  | 
**Records** | [**[]GetReceivingDomain200ResponseRecordsInner**](GetReceivingDomain200ResponseRecordsInner.md) |  | 

## Methods

### NewGetReceivingDomain200Response

`func NewGetReceivingDomain200Response(domainId string, name string, status string, verifiedUntil int32, createdAt string, records []GetReceivingDomain200ResponseRecordsInner, ) *GetReceivingDomain200Response`

NewGetReceivingDomain200Response instantiates a new GetReceivingDomain200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetReceivingDomain200ResponseWithDefaults

`func NewGetReceivingDomain200ResponseWithDefaults() *GetReceivingDomain200Response`

NewGetReceivingDomain200ResponseWithDefaults instantiates a new GetReceivingDomain200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDomainId

`func (o *GetReceivingDomain200Response) GetDomainId() string`

GetDomainId returns the DomainId field if non-nil, zero value otherwise.

### GetDomainIdOk

`func (o *GetReceivingDomain200Response) GetDomainIdOk() (*string, bool)`

GetDomainIdOk returns a tuple with the DomainId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomainId

`func (o *GetReceivingDomain200Response) SetDomainId(v string)`

SetDomainId sets DomainId field to given value.


### GetName

`func (o *GetReceivingDomain200Response) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *GetReceivingDomain200Response) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *GetReceivingDomain200Response) SetName(v string)`

SetName sets Name field to given value.


### GetStatus

`func (o *GetReceivingDomain200Response) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *GetReceivingDomain200Response) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *GetReceivingDomain200Response) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetVerifiedUntil

`func (o *GetReceivingDomain200Response) GetVerifiedUntil() int32`

GetVerifiedUntil returns the VerifiedUntil field if non-nil, zero value otherwise.

### GetVerifiedUntilOk

`func (o *GetReceivingDomain200Response) GetVerifiedUntilOk() (*int32, bool)`

GetVerifiedUntilOk returns a tuple with the VerifiedUntil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerifiedUntil

`func (o *GetReceivingDomain200Response) SetVerifiedUntil(v int32)`

SetVerifiedUntil sets VerifiedUntil field to given value.


### GetCreatedAt

`func (o *GetReceivingDomain200Response) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *GetReceivingDomain200Response) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *GetReceivingDomain200Response) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetRecords

`func (o *GetReceivingDomain200Response) GetRecords() []GetReceivingDomain200ResponseRecordsInner`

GetRecords returns the Records field if non-nil, zero value otherwise.

### GetRecordsOk

`func (o *GetReceivingDomain200Response) GetRecordsOk() (*[]GetReceivingDomain200ResponseRecordsInner, bool)`

GetRecordsOk returns a tuple with the Records field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecords

`func (o *GetReceivingDomain200Response) SetRecords(v []GetReceivingDomain200ResponseRecordsInner)`

SetRecords sets Records field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


