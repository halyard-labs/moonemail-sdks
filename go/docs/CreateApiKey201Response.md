# CreateApiKey201Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**Id** | **string** |  | 
**Token** | **string** | Returned once. Save securely. | 
**Hint** | **string** |  | 
**Permission** | **string** |  | 
**Scopes** | **[]string** |  | 
**ExpiresAt** | **NullableString** |  | 

## Methods

### NewCreateApiKey201Response

`func NewCreateApiKey201Response(object string, id string, token string, hint string, permission string, scopes []string, expiresAt NullableString, ) *CreateApiKey201Response`

NewCreateApiKey201Response instantiates a new CreateApiKey201Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateApiKey201ResponseWithDefaults

`func NewCreateApiKey201ResponseWithDefaults() *CreateApiKey201Response`

NewCreateApiKey201ResponseWithDefaults instantiates a new CreateApiKey201Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *CreateApiKey201Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *CreateApiKey201Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *CreateApiKey201Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetId

`func (o *CreateApiKey201Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CreateApiKey201Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CreateApiKey201Response) SetId(v string)`

SetId sets Id field to given value.


### GetToken

`func (o *CreateApiKey201Response) GetToken() string`

GetToken returns the Token field if non-nil, zero value otherwise.

### GetTokenOk

`func (o *CreateApiKey201Response) GetTokenOk() (*string, bool)`

GetTokenOk returns a tuple with the Token field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToken

`func (o *CreateApiKey201Response) SetToken(v string)`

SetToken sets Token field to given value.


### GetHint

`func (o *CreateApiKey201Response) GetHint() string`

GetHint returns the Hint field if non-nil, zero value otherwise.

### GetHintOk

`func (o *CreateApiKey201Response) GetHintOk() (*string, bool)`

GetHintOk returns a tuple with the Hint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHint

`func (o *CreateApiKey201Response) SetHint(v string)`

SetHint sets Hint field to given value.


### GetPermission

`func (o *CreateApiKey201Response) GetPermission() string`

GetPermission returns the Permission field if non-nil, zero value otherwise.

### GetPermissionOk

`func (o *CreateApiKey201Response) GetPermissionOk() (*string, bool)`

GetPermissionOk returns a tuple with the Permission field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermission

`func (o *CreateApiKey201Response) SetPermission(v string)`

SetPermission sets Permission field to given value.


### GetScopes

`func (o *CreateApiKey201Response) GetScopes() []string`

GetScopes returns the Scopes field if non-nil, zero value otherwise.

### GetScopesOk

`func (o *CreateApiKey201Response) GetScopesOk() (*[]string, bool)`

GetScopesOk returns a tuple with the Scopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopes

`func (o *CreateApiKey201Response) SetScopes(v []string)`

SetScopes sets Scopes field to given value.


### GetExpiresAt

`func (o *CreateApiKey201Response) GetExpiresAt() string`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *CreateApiKey201Response) GetExpiresAtOk() (*string, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *CreateApiKey201Response) SetExpiresAt(v string)`

SetExpiresAt sets ExpiresAt field to given value.


### SetExpiresAtNil

`func (o *CreateApiKey201Response) SetExpiresAtNil(b bool)`

 SetExpiresAtNil sets the value for ExpiresAt to be an explicit nil

### UnsetExpiresAt
`func (o *CreateApiKey201Response) UnsetExpiresAt()`

UnsetExpiresAt ensures that no value is present for ExpiresAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


