# ListWebhookDeliveries200ResponseDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WebhookId** | **string** |  | 
**EventId** | **string** |  | 
**EventType** | **string** |  | 
**EmailId** | **string** |  | 
**Attempt** | **int32** |  | 
**StatusCode** | **int32** | Zero when no HTTP response was received. | 
**Ok** | **bool** |  | 
**DurationMs** | **int32** |  | 
**Error** | Pointer to **string** |  | [optional] 
**CreatedAt** | **string** |  | 

## Methods

### NewListWebhookDeliveries200ResponseDataInner

`func NewListWebhookDeliveries200ResponseDataInner(webhookId string, eventId string, eventType string, emailId string, attempt int32, statusCode int32, ok bool, durationMs int32, createdAt string, ) *ListWebhookDeliveries200ResponseDataInner`

NewListWebhookDeliveries200ResponseDataInner instantiates a new ListWebhookDeliveries200ResponseDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhookDeliveries200ResponseDataInnerWithDefaults

`func NewListWebhookDeliveries200ResponseDataInnerWithDefaults() *ListWebhookDeliveries200ResponseDataInner`

NewListWebhookDeliveries200ResponseDataInnerWithDefaults instantiates a new ListWebhookDeliveries200ResponseDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWebhookId

`func (o *ListWebhookDeliveries200ResponseDataInner) GetWebhookId() string`

GetWebhookId returns the WebhookId field if non-nil, zero value otherwise.

### GetWebhookIdOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetWebhookIdOk() (*string, bool)`

GetWebhookIdOk returns a tuple with the WebhookId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebhookId

`func (o *ListWebhookDeliveries200ResponseDataInner) SetWebhookId(v string)`

SetWebhookId sets WebhookId field to given value.


### GetEventId

`func (o *ListWebhookDeliveries200ResponseDataInner) GetEventId() string`

GetEventId returns the EventId field if non-nil, zero value otherwise.

### GetEventIdOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetEventIdOk() (*string, bool)`

GetEventIdOk returns a tuple with the EventId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventId

`func (o *ListWebhookDeliveries200ResponseDataInner) SetEventId(v string)`

SetEventId sets EventId field to given value.


### GetEventType

`func (o *ListWebhookDeliveries200ResponseDataInner) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetEventTypeOk() (*string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *ListWebhookDeliveries200ResponseDataInner) SetEventType(v string)`

SetEventType sets EventType field to given value.


### GetEmailId

`func (o *ListWebhookDeliveries200ResponseDataInner) GetEmailId() string`

GetEmailId returns the EmailId field if non-nil, zero value otherwise.

### GetEmailIdOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetEmailIdOk() (*string, bool)`

GetEmailIdOk returns a tuple with the EmailId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailId

`func (o *ListWebhookDeliveries200ResponseDataInner) SetEmailId(v string)`

SetEmailId sets EmailId field to given value.


### GetAttempt

`func (o *ListWebhookDeliveries200ResponseDataInner) GetAttempt() int32`

GetAttempt returns the Attempt field if non-nil, zero value otherwise.

### GetAttemptOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetAttemptOk() (*int32, bool)`

GetAttemptOk returns a tuple with the Attempt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttempt

`func (o *ListWebhookDeliveries200ResponseDataInner) SetAttempt(v int32)`

SetAttempt sets Attempt field to given value.


### GetStatusCode

`func (o *ListWebhookDeliveries200ResponseDataInner) GetStatusCode() int32`

GetStatusCode returns the StatusCode field if non-nil, zero value otherwise.

### GetStatusCodeOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetStatusCodeOk() (*int32, bool)`

GetStatusCodeOk returns a tuple with the StatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusCode

`func (o *ListWebhookDeliveries200ResponseDataInner) SetStatusCode(v int32)`

SetStatusCode sets StatusCode field to given value.


### GetOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetOk() bool`

GetOk returns the Ok field if non-nil, zero value otherwise.

### GetOkOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetOkOk() (*bool, bool)`

GetOkOk returns a tuple with the Ok field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOk

`func (o *ListWebhookDeliveries200ResponseDataInner) SetOk(v bool)`

SetOk sets Ok field to given value.


### GetDurationMs

`func (o *ListWebhookDeliveries200ResponseDataInner) GetDurationMs() int32`

GetDurationMs returns the DurationMs field if non-nil, zero value otherwise.

### GetDurationMsOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetDurationMsOk() (*int32, bool)`

GetDurationMsOk returns a tuple with the DurationMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDurationMs

`func (o *ListWebhookDeliveries200ResponseDataInner) SetDurationMs(v int32)`

SetDurationMs sets DurationMs field to given value.


### GetError

`func (o *ListWebhookDeliveries200ResponseDataInner) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *ListWebhookDeliveries200ResponseDataInner) SetError(v string)`

SetError sets Error field to given value.

### HasError

`func (o *ListWebhookDeliveries200ResponseDataInner) HasError() bool`

HasError returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ListWebhookDeliveries200ResponseDataInner) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ListWebhookDeliveries200ResponseDataInner) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ListWebhookDeliveries200ResponseDataInner) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


