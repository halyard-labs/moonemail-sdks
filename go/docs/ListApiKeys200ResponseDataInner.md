# ListApiKeys200ResponseDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**Id** | **string** |  | 
**Name** | **string** |  | 
**Permission** | **string** |  | 
**Scopes** | Pointer to **[]string** |  | [optional] 
**DomainId** | **NullableString** |  | 
**Hint** | **string** |  | 
**CreatedAt** | **string** |  | 
**LastUsedAt** | **NullableString** |  | 
**ExpiresAt** | **NullableString** |  | 

## Methods

### NewListApiKeys200ResponseDataInner

`func NewListApiKeys200ResponseDataInner(object string, id string, name string, permission string, domainId NullableString, hint string, createdAt string, lastUsedAt NullableString, expiresAt NullableString, ) *ListApiKeys200ResponseDataInner`

NewListApiKeys200ResponseDataInner instantiates a new ListApiKeys200ResponseDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListApiKeys200ResponseDataInnerWithDefaults

`func NewListApiKeys200ResponseDataInnerWithDefaults() *ListApiKeys200ResponseDataInner`

NewListApiKeys200ResponseDataInnerWithDefaults instantiates a new ListApiKeys200ResponseDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListApiKeys200ResponseDataInner) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListApiKeys200ResponseDataInner) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListApiKeys200ResponseDataInner) SetObject(v string)`

SetObject sets Object field to given value.


### GetId

`func (o *ListApiKeys200ResponseDataInner) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ListApiKeys200ResponseDataInner) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ListApiKeys200ResponseDataInner) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *ListApiKeys200ResponseDataInner) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ListApiKeys200ResponseDataInner) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ListApiKeys200ResponseDataInner) SetName(v string)`

SetName sets Name field to given value.


### GetPermission

`func (o *ListApiKeys200ResponseDataInner) GetPermission() string`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *ListApiKeys200ResponseDataInner) GetPermissionOk() (*string, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *ListApiKeys200ResponseDataInner) SetPermission(v string)`

SetPermission sets Permission field to given value.


### GetScopes

`func (o *ListApiKeys200ResponseDataInner) GetScopes() []string`

GetScopes returns the Scopes field if non-nil, zero value otherwise.

### GetScopesOk

`func (o *ListApiKeys200ResponseDataInner) GetScopesOk() (*[]string, bool)`

GetScopesOk returns a tuple with the Scopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopes

`func (o *ListApiKeys200ResponseDataInner) SetScopes(v []string)`

SetScopes sets Scopes field to given value.

### HasScopes

`func (o *ListApiKeys200ResponseDataInner) HasScopes() bool`

HasScopes returns a boolean if a field has been set.

### GetDomainId

`func (o *ListApiKeys200ResponseDataInner) GetDomainId() string`

GetDomainId returns the DomainId field if non-nil, zero value otherwise.

### GetDomainIdOk

`func (o *ListApiKeys200ResponseDataInner) GetDomainIdOk() (*string, bool)`

GetDomainIdOk returns a tuple with the DomainId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomainId

`func (o *ListApiKeys200ResponseDataInner) SetDomainId(v string)`

SetDomainId sets DomainId field to given value.


### SetDomainIdNil

`func (o *ListApiKeys200ResponseDataInner) SetDomainIdNil(b bool)`

 SetDomainIdNil sets the value for DomainId to be an explicit nil

### UnsetDomainId
`func (o *ListApiKeys200ResponseDataInner) UnsetDomainId()`

UnsetDomainId ensures that no value is present for DomainId, not even an explicit nil
### GetHint

`func (o *ListApiKeys200ResponseDataInner) GetHint() string`

GetHint returns the Hint field if non-nil, zero value otherwise.

### GetHintOk

`func (o *ListApiKeys200ResponseDataInner) GetHintOk() (*string, bool)`

GetHintOk returns a tuple with the Hint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHint

`func (o *ListApiKeys200ResponseDataInner) SetHint(v string)`

SetHint sets Hint field to given value.


### GetCreatedAt

`func (o *ListApiKeys200ResponseDataInner) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ListApiKeys200ResponseDataInner) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ListApiKeys200ResponseDataInner) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetLastUsedAt

`func (o *ListApiKeys200ResponseDataInner) GetLastUsedAt() string`

GetLastUsedAt returns the LastUsedAt field if non-nil, zero value otherwise.

### GetLastUsedAtOk

`func (o *ListApiKeys200ResponseDataInner) GetLastUsedAtOk() (*string, bool)`

GetLastUsedAtOk returns a tuple with the LastUsedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUsedAt

`func (o *ListApiKeys200ResponseDataInner) SetLastUsedAt(v string)`

SetLastUsedAt sets LastUsedAt field to given value.


### SetLastUsedAtNil

`func (o *ListApiKeys200ResponseDataInner) SetLastUsedAtNil(b bool)`

 SetLastUsedAtNil sets the value for LastUsedAt to be an explicit nil

### UnsetLastUsedAt
`func (o *ListApiKeys200ResponseDataInner) UnsetLastUsedAt()`

UnsetLastUsedAt ensures that no value is present for LastUsedAt, not even an explicit nil
### GetExpiresAt

`func (o *ListApiKeys200ResponseDataInner) GetExpiresAt() string`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ListApiKeys200ResponseDataInner) GetExpiresAtOk() (*string, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ListApiKeys200ResponseDataInner) SetExpiresAt(v string)`

SetExpiresAt sets ExpiresAt field to given value.


### SetExpiresAtNil

`func (o *ListApiKeys200ResponseDataInner) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *ListApiKeys200ResponseDataInner) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


