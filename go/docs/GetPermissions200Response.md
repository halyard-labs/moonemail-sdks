# GetPermissions200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Permission** | **string** |  | 
**Scopes** | **[]string** |  | 
**DomainId** | **NullableString** |  | 
**ExpiresAt** | **NullableString** |  | 
**CanManageApiKeys** | **bool** |  | 
**BillingRequiresOwner** | **bool** |  | 

## Methods

### NewGetPermissions200Response

`func NewGetPermissions200Response(permission string, scopes []string, domainId NullableString, expiresAt NullableString, canManageApiKeys bool, billingRequiresOwner bool, ) *GetPermissions200Response`

NewGetPermissions200Response instantiates a new GetPermissions200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetPermissions200ResponseWithDefaults

`func NewGetPermissions200ResponseWithDefaults() *GetPermissions200Response`

NewGetPermissions200ResponseWithDefaults instantiates a new GetPermissions200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPermission

`func (o *GetPermissions200Response) GetPermission() string`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *GetPermissions200Response) GetPermissionOk() (*string, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *GetPermissions200Response) SetPermission(v string)`

SetPermission sets Permission field to given value.


### GetScopes

`func (o *GetPermissions200Response) GetScopes() []string`

GetScopes returns the Scopes field if non-nil, zero value otherwise.

### GetScopesOk

`func (o *GetPermissions200Response) GetScopesOk() (*[]string, bool)`

GetScopesOk returns a tuple with the Scopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopes

`func (o *GetPermissions200Response) SetScopes(v []string)`

SetScopes sets Scopes field to given value.


### GetDomainId

`func (o *GetPermissions200Response) GetDomainId() string`

GetDomainId returns the DomainId field if non-nil, zero value otherwise.

### GetDomainIdOk

`func (o *GetPermissions200Response) GetDomainIdOk() (*string, bool)`

GetDomainIdOk returns a tuple with the DomainId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDomainId

`func (o *GetPermissions200Response) SetDomainId(v string)`

SetDomainId sets DomainId field to given value.


### SetDomainIdNil

`func (o *GetPermissions200Response) SetDomainIdNil(b bool)`

 SetDomainIdNil sets the value for DomainId to be an explicit nil

### UnsetDomainId
`func (o *GetPermissions200Response) UnsetDomainId()`

UnsetDomainId ensures that no value is present for DomainId, not even an explicit nil
### GetExpiresAt

`func (o *GetPermissions200Response) GetExpiresAt() string`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GetPermissions200Response) GetExpiresAtOk() (*string, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GetPermissions200Response) SetExpiresAt(v string)`

SetExpiresAt sets ExpiresAt field to given value.


### SetExpiresAtNil

`func (o *GetPermissions200Response) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *GetPermissions200Response) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil
### GetCanManageApiKeys

`func (o *GetPermissions200Response) GetCanManageApiKeys() bool`

GetCanManageApiKeys returns the CanManageApiKeys field if non-nil, zero value otherwise.

### GetCanManageApiKeysOk

`func (o *GetPermissions200Response) GetCanManageApiKeysOk() (*bool, bool)`

GetCanManageApiKeysOk returns a tuple with the CanManageApiKeys field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanManageApiKeys

`func (o *GetPermissions200Response) SetCanManageApiKeys(v bool)`

SetCanManageApiKeys sets CanManageApiKeys field to given value.


### GetBillingRequiresOwner

`func (o *GetPermissions200Response) GetBillingRequiresOwner() bool`

GetBillingRequiresOwner returns the BillingRequiresOwner field if non-nil, zero value otherwise.

### GetBillingRequiresOwnerOk

`func (o *GetPermissions200Response) GetBillingRequiresOwnerOk() (*bool, bool)`

GetBillingRequiresOwnerOk returns a tuple with the BillingRequiresOwner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBillingRequiresOwner

`func (o *GetPermissions200Response) SetBillingRequiresOwner(v bool)`

SetBillingRequiresOwner sets BillingRequiresOwner field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


