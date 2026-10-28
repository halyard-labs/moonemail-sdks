# CreateWebhook201Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**Id** | **string** |  | 
**SigningSecret** | **string** | Save securely to verify incoming webhook signatures. | 

## Methods

### NewCreateWebhook201Response

`func NewCreateWebhook201Response(object string, id string, signingSecret string, ) *CreateWebhook201Response`

NewCreateWebhook201Response instantiates a new CreateWebhook201Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateWebhook201ResponseWithDefaults

`func NewCreateWebhook201ResponseWithDefaults() *CreateWebhook201Response`

NewCreateWebhook201ResponseWithDefaults instantiates a new CreateWebhook201Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *CreateWebhook201Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *CreateWebhook201Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *CreateWebhook201Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetId

`func (o *CreateWebhook201Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CreateWebhook201Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CreateWebhook201Response) SetId(v string)`

SetId sets Id field to given value.


### GetSigningSecret

`func (o *CreateWebhook201Response) GetSigningSecret() string`

GetSigningSecret returns the SigningSecret field if non-nil, zero value otherwise.

### GetSigningSecretOk

`func (o *CreateWebhook201Response) GetSigningSecretOk() (*string, bool)`

GetSigningSecretOk returns a tuple with the SigningSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSigningSecret

`func (o *CreateWebhook201Response) SetSigningSecret(v string)`

SetSigningSecret sets SigningSecret field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


