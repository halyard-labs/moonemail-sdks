# CreateWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Endpoint** | **string** |  | 
**Events** | **[]string** |  | 

## Methods

### NewCreateWebhookRequest

`func NewCreateWebhookRequest(endpoint string, events []string, ) *CreateWebhookRequest`

NewCreateWebhookRequest instantiates a new CreateWebhookRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateWebhookRequestWithDefaults

`func NewCreateWebhookRequestWithDefaults() *CreateWebhookRequest`

NewCreateWebhookRequestWithDefaults instantiates a new CreateWebhookRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEndpoint

`func (o *CreateWebhookRequest) GetEndpoint() string`

GetEndpoint returns the Endpoint field if non-nil, zero value otherwise.

### GetEndpointOk

`func (o *CreateWebhookRequest) GetEndpointOk() (*string, bool)`

GetEndpointOk returns a tuple with the Endpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndpoint

`func (o *CreateWebhookRequest) SetEndpoint(v string)`

SetEndpoint sets Endpoint field to given value.


### GetEvents

`func (o *CreateWebhookRequest) GetEvents() []string`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *CreateWebhookRequest) GetEventsOk() (*[]string, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *CreateWebhookRequest) SetEvents(v []string)`

SetEvents sets Events field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


