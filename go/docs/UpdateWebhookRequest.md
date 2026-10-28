# UpdateWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Endpoint** | Pointer to **string** |  | [optional] 
**Events** | Pointer to **[]string** |  | [optional] 
**Status** | Pointer to **string** |  | [optional] 

## Methods

### NewUpdateWebhookRequest

`func NewUpdateWebhookRequest() *UpdateWebhookRequest`

NewUpdateWebhookRequest instantiates a new UpdateWebhookRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateWebhookRequestWithDefaults

`func NewUpdateWebhookRequestWithDefaults() *UpdateWebhookRequest`

NewUpdateWebhookRequestWithDefaults instantiates a new UpdateWebhookRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEndpoint

`func (o *UpdateWebhookRequest) GetEndpoint() string`

GetEndpoint returns the Endpoint field if non-nil, zero value otherwise.

### GetEndpointOk

`func (o *UpdateWebhookRequest) GetEndpointOk() (*string, bool)`

GetEndpointOk returns a tuple with the Endpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndpoint

`func (o *UpdateWebhookRequest) SetEndpoint(v string)`

SetEndpoint sets Endpoint field to given value.

### HasEndpoint

`func (o *UpdateWebhookRequest) HasEndpoint() bool`

HasEndpoint returns a boolean if a field has been set.

### GetEvents

`func (o *UpdateWebhookRequest) GetEvents() []string`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *UpdateWebhookRequest) GetEventsOk() (*[]string, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *UpdateWebhookRequest) SetEvents(v []string)`

SetEvents sets Events field to given value.

### HasEvents

`func (o *UpdateWebhookRequest) HasEvents() bool`

HasEvents returns a boolean if a field has been set.

### GetStatus

`func (o *UpdateWebhookRequest) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateWebhookRequest) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateWebhookRequest) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *UpdateWebhookRequest) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


