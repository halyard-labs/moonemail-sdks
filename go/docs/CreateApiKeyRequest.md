# CreateApiKeyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Permission** | Pointer to **string** |  | [optional] 
**Scopes** | Pointer to **[]string** |  | [optional] 
**DomainId** | Pointer to **string** |  | [optional] 
**ExpiresAt** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateApiKeyRequest

`func NewCreateApiKeyRequest(name string, ) *CreateApiKeyRequest`

NewCreateApiKeyRequest instantiates a new CreateApiKeyRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateApiKeyRequestWithDefaults

`func NewCreateApiKeyRequestWithDefaults() *CreateApiKeyRequest`

NewCreateApiKeyRequestWithDefaults instantiates a new CreateApiKeyRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateApiKeyRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateApiKeyRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateApiKeyRequest) SetName(v string)`

SetName sets Name field to given value.


### GetPermission

`func (o *CreateApiKeyRequest) GetPermission() string`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *CreateApiKeyRequest) GetPermissionOk() (*string, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *CreateApiKeyRequest) SetPermission(v string)`

SetPermission sets Permission field to given value.

### HasPermission

`func (o *CreateApiKeyRequest) HasPermission() bool`

HasPermission returns a boolean if a field has been set.

### GetScopes

`func (o *CreateApiKeyRequest) GetScopes() []string`

GetScopes returns the Scopes field if non-nil, zero value otherwise.

### GetScopesOk

`func (o *CreateApiKeyRequest) GetScopesOk() (*[]string, bool)`

GetScopesOk returns a tuple with the Scopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopes

`func (o *CreateApiKeyRequest) SetScopes(v []string)`

SetScopes sets Scopes field to given value.

### HasScopes

`func (o *CreateApiKeyRequest) HasScopes() bool`

HasScopes returns a boolean if a field has been set.

### GetDomainId

`func (o *CreateApiKeyRequest) GetDomainId() string`

GetDomainId returns the DomainId field if non-nil, zero value otherwise.

### GetDomainIdOk

`func (o *CreateApiKeyRequest) GetDomainIdOk() (*string, bool)`

GetDomainIdOk returns a tuple with the DomainId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomainId

`func (o *CreateApiKeyRequest) SetDomainId(v string)`

SetDomainId sets DomainId field to given value.

### HasDomainId

`func (o *CreateApiKeyRequest) HasDomainId() bool`

HasDomainId returns a boolean if a field has been set.

### GetExpiresAt

`func (o *CreateApiKeyRequest) GetExpiresAt() string`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *CreateApiKeyRequest) GetExpiresAtOk() (*string, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *CreateApiKeyRequest) SetExpiresAt(v string)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *CreateApiKeyRequest) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


