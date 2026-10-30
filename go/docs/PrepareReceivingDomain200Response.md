# PrepareReceivingDomain200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DomainId** | **string** |  | 
**Name** | **string** |  | 
**Status** | **string** |  | 
**VerifiedUntil** | **int32** |  | 
**CreatedAt** | **string** |  | 
**Records** | [**[]PrepareReceivingDomain200ResponseRecordsInner**](PrepareReceivingDomain200ResponseRecordsInner.md) |  | 

## Methods

### NewPrepareReceivingDomain200Response

`func NewPrepareReceivingDomain200Response(domainId string, name string, status string, verifiedUntil int32, createdAt string, records []PrepareReceivingDomain200ResponseRecordsInner, ) *PrepareReceivingDomain200Response`

NewPrepareReceivingDomain200Response instantiates a new PrepareReceivingDomain200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPrepareReceivingDomain200ResponseWithDefaults

`func NewPrepareReceivingDomain200ResponseWithDefaults() *PrepareReceivingDomain200Response`

NewPrepareReceivingDomain200ResponseWithDefaults instantiates a new PrepareReceivingDomain200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDomainId

`func (o *PrepareReceivingDomain200Response) GetDomainId() string`

GetDomainId returns the DomainId field if non-nil, zero value otherwise.

### GetDomainIdOk

`func (o *PrepareReceivingDomain200Response) GetDomainIdOk() (*string, bool)`

GetDomainIdOk returns a tuple with the DomainId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomainId

`func (o *PrepareReceivingDomain200Response) SetDomainId(v string)`

SetDomainId sets DomainId field to given value.


### GetName

`func (o *PrepareReceivingDomain200Response) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PrepareReceivingDomain200Response) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PrepareReceivingDomain200Response) SetName(v string)`

SetName sets Name field to given value.


### GetStatus

`func (o *PrepareReceivingDomain200Response) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PrepareReceivingDomain200Response) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PrepareReceivingDomain200Response) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetVerifiedUntil

`func (o *PrepareReceivingDomain200Response) GetVerifiedUntil() int32`

GetVerifiedUntil returns the VerifiedUntil field if non-nil, zero value otherwise.

### GetVerifiedUntilOk

`func (o *PrepareReceivingDomain200Response) GetVerifiedUntilOk() (*int32, bool)`

GetVerifiedUntilOk returns a tuple with the VerifiedUntil field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerifiedUntil

`func (o *PrepareReceivingDomain200Response) SetVerifiedUntil(v int32)`

SetVerifiedUntil sets VerifiedUntil field to given value.


### GetCreatedAt

`func (o *PrepareReceivingDomain200Response) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *PrepareReceivingDomain200Response) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *PrepareReceivingDomain200Response) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetRecords

`func (o *PrepareReceivingDomain200Response) GetRecords() []PrepareReceivingDomain200ResponseRecordsInner`

GetRecords returns the Records field if non-nil, zero value otherwise.

### GetRecordsOk

`func (o *PrepareReceivingDomain200Response) GetRecordsOk() (*[]PrepareReceivingDomain200ResponseRecordsInner, bool)`

GetRecordsOk returns a tuple with the Records field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecords

`func (o *PrepareReceivingDomain200Response) SetRecords(v []PrepareReceivingDomain200ResponseRecordsInner)`

SetRecords sets Records field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


