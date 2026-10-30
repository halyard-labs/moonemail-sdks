# CreateInboxRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**DomainId** | Pointer to **string** |  | [optional] 
**LocalPart** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateInboxRequest

`func NewCreateInboxRequest(name string, ) *CreateInboxRequest`

NewCreateInboxRequest instantiates a new CreateInboxRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateInboxRequestWithDefaults

`func NewCreateInboxRequestWithDefaults() *CreateInboxRequest`

NewCreateInboxRequestWithDefaults instantiates a new CreateInboxRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateInboxRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateInboxRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateInboxRequest) SetName(v string)`

SetName sets Name field to given value.


### GetDomainId

`func (o *CreateInboxRequest) GetDomainId() string`

GetDomainId returns the DomainId field if non-nil, zero value otherwise.

### GetDomainIdOk

`func (o *CreateInboxRequest) GetDomainIdOk() (*string, bool)`

GetDomainIdOk returns a tuple with the DomainId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomainId

`func (o *CreateInboxRequest) SetDomainId(v string)`

SetDomainId sets DomainId field to given value.

### HasDomainId

`func (o *CreateInboxRequest) HasDomainId() bool`

HasDomainId returns a boolean if a field has been set.

### GetLocalPart

`func (o *CreateInboxRequest) GetLocalPart() string`

GetLocalPart returns the LocalPart field if non-nil, zero value otherwise.

### GetLocalPartOk

`func (o *CreateInboxRequest) GetLocalPartOk() (*string, bool)`

GetLocalPartOk returns a tuple with the LocalPart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocalPart

`func (o *CreateInboxRequest) SetLocalPart(v string)`

SetLocalPart sets LocalPart field to given value.

### HasLocalPart

`func (o *CreateInboxRequest) HasLocalPart() bool`

HasLocalPart returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


