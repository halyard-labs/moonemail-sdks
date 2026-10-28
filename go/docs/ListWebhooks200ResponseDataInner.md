# ListWebhooks200ResponseDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Object** | **string** |  | 
**Id** | **string** |  | 
**Endpoint** | **string** |  | 
**Events** | **[]string** |  | 
**Status** | **string** |  | 
**CreatedAt** | **string** |  | 
**SigningSecret** | Pointer to **string** | Only revealed to dashboard user sessions; never returned by API-key reads. | [optional] 

## Methods

### NewListWebhooks200ResponseDataInner

`func NewListWebhooks200ResponseDataInner(object string, id string, endpoint string, events []string, status string, createdAt string, ) *ListWebhooks200ResponseDataInner`

NewListWebhooks200ResponseDataInner instantiates a new ListWebhooks200ResponseDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhooks200ResponseDataInnerWithDefaults

`func NewListWebhooks200ResponseDataInnerWithDefaults() *ListWebhooks200ResponseDataInner`

NewListWebhooks200ResponseDataInnerWithDefaults instantiates a new ListWebhooks200ResponseDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetObject

`func (o *ListWebhooks200ResponseDataInner) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *ListWebhooks200ResponseDataInner) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *ListWebhooks200ResponseDataInner) SetObject(v string)`

SetObject sets Object field to given value.


### GetId

`func (o *ListWebhooks200ResponseDataInner) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ListWebhooks200ResponseDataInner) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ListWebhooks200ResponseDataInner) SetId(v string)`

SetId sets Id field to given value.


### GetEndpoint

`func (o *ListWebhooks200ResponseDataInner) GetEndpoint() string`

GetEndpoint returns the Endpoint field if non-nil, zero value otherwise.

### GetEndpointOk

`func (o *ListWebhooks200ResponseDataInner) GetEndpointOk() (*string, bool)`

GetEndpointOk returns a tuple with the Endpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndpoint

`func (o *ListWebhooks200ResponseDataInner) SetEndpoint(v string)`

SetEndpoint sets Endpoint field to given value.


### GetEvents

`func (o *ListWebhooks200ResponseDataInner) GetEvents() []string`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *ListWebhooks200ResponseDataInner) GetEventsOk() (*[]string, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *ListWebhooks200ResponseDataInner) SetEvents(v []string)`

SetEvents sets Events field to given value.


### SetEventsNil

`func (o *ListWebhooks200ResponseDataInner) SetEventsNil(b bool)`

 SetEventsNil sets the value for Events to be an explicit nil

### UnsetEvents
`func (o *ListWebhooks200ResponseDataInner) UnsetEvents()`

UnsetEvents ensures that no value is present for Events, not even an explicit nil
### GetStatus

`func (o *ListWebhooks200ResponseDataInner) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ListWebhooks200ResponseDataInner) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ListWebhooks200ResponseDataInner) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedAt

`func (o *ListWebhooks200ResponseDataInner) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ListWebhooks200ResponseDataInner) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ListWebhooks200ResponseDataInner) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetSigningSecret

`func (o *ListWebhooks200ResponseDataInner) GetSigningSecret() string`

GetSigningSecret returns the SigningSecret field if non-nil, zero value otherwise.

### GetSigningSecretOk

`func (o *ListWebhooks200ResponseDataInner) GetSigningSecretOk() (*string, bool)`

GetSigningSecretOk returns a tuple with the SigningSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSigningSecret

`func (o *ListWebhooks200ResponseDataInner) SetSigningSecret(v string)`

SetSigningSecret sets SigningSecret field to given value.

### HasSigningSecret

`func (o *ListWebhooks200ResponseDataInner) HasSigningSecret() bool`

HasSigningSecret returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


