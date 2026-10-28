# ListEmails200ResponseDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**MessageId** | **NullableString** |  | 
**To** | **[]string** |  | 
**From** | **string** |  | 
**CreatedAt** | **string** |  | 
**Subject** | **string** |  | 
**Bcc** | **[]string** |  | 
**Cc** | **[]string** |  | 
**ReplyTo** | **[]string** |  | 
**LastEvent** | **string** |  | 
**ScheduledAt** | **NullableString** |  | 

## Methods

### NewListEmails200ResponseDataInner

`func NewListEmails200ResponseDataInner(id string, messageId NullableString, to []string, from string, createdAt string, subject string, bcc []string, cc []string, replyTo []string, lastEvent string, scheduledAt NullableString, ) *ListEmails200ResponseDataInner`

NewListEmails200ResponseDataInner instantiates a new ListEmails200ResponseDataInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListEmails200ResponseDataInnerWithDefaults

`func NewListEmails200ResponseDataInnerWithDefaults() *ListEmails200ResponseDataInner`

NewListEmails200ResponseDataInnerWithDefaults instantiates a new ListEmails200ResponseDataInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ListEmails200ResponseDataInner) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ListEmails200ResponseDataInner) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ListEmails200ResponseDataInner) SetId(v string)`

SetId sets Id field to given value.


### GetMessageId

`func (o *ListEmails200ResponseDataInner) GetMessageId() string`

GetMessageId returns the MessageId field if non-nil, zero value otherwise.

### GetMessageIdOk

`func (o *ListEmails200ResponseDataInner) GetMessageIdOk() (*string, bool)`

GetMessageIdOk returns a tuple with the MessageId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessageId

`func (o *ListEmails200ResponseDataInner) SetMessageId(v string)`

SetMessageId sets MessageId field to given value.


### SetMessageIdNil

`func (o *ListEmails200ResponseDataInner) SetMessageIdNil(b bool)`

 SetMessageIdNil sets the value for MessageId to be an explicit nil

### UnsetMessageId
`func (o *ListEmails200ResponseDataInner) UnsetMessageId()`

UnsetMessageId ensures that no value is present for MessageId, not even an explicit nil
### GetTo

`func (o *ListEmails200ResponseDataInner) GetTo() []string`

GetTo returns the To field if non-nil, zero value otherwise.

### GetToOk

`func (o *ListEmails200ResponseDataInner) GetToOk() (*[]string, bool)`

GetToOk returns a tuple with the To field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTo

`func (o *ListEmails200ResponseDataInner) SetTo(v []string)`

SetTo sets To field to given value.


### GetFrom

`func (o *ListEmails200ResponseDataInner) GetFrom() string`

GetFrom returns the From field if non-nil, zero value otherwise.

### GetFromOk

`func (o *ListEmails200ResponseDataInner) GetFromOk() (*string, bool)`

GetFromOk returns a tuple with the From field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrom

`func (o *ListEmails200ResponseDataInner) SetFrom(v string)`

SetFrom sets From field to given value.


### GetCreatedAt

`func (o *ListEmails200ResponseDataInner) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ListEmails200ResponseDataInner) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ListEmails200ResponseDataInner) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetSubject

`func (o *ListEmails200ResponseDataInner) GetSubject() string`

GetSubject returns the Subject field if non-nil, zero value otherwise.

### GetSubjectOk

`func (o *ListEmails200ResponseDataInner) GetSubjectOk() (*string, bool)`

GetSubjectOk returns a tuple with the Subject field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubject

`func (o *ListEmails200ResponseDataInner) SetSubject(v string)`

SetSubject sets Subject field to given value.


### GetBcc

`func (o *ListEmails200ResponseDataInner) GetBcc() []string`

GetBcc returns the Bcc field if non-nil, zero value otherwise.

### GetBccOk

`func (o *ListEmails200ResponseDataInner) GetBccOk() (*[]string, bool)`

GetBccOk returns a tuple with the Bcc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBcc

`func (o *ListEmails200ResponseDataInner) SetBcc(v []string)`

SetBcc sets Bcc field to given value.


### GetCc

`func (o *ListEmails200ResponseDataInner) GetCc() []string`

GetCc returns the Cc field if non-nil, zero value otherwise.

### GetCcOk

`func (o *ListEmails200ResponseDataInner) GetCcOk() (*[]string, bool)`

GetCcOk returns a tuple with the Cc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCc

`func (o *ListEmails200ResponseDataInner) SetCc(v []string)`

SetCc sets Cc field to given value.


### GetReplyTo

`func (o *ListEmails200ResponseDataInner) GetReplyTo() []string`

GetReplyTo returns the ReplyTo field if non-nil, zero value otherwise.

### GetReplyToOk

`func (o *ListEmails200ResponseDataInner) GetReplyToOk() (*[]string, bool)`

GetReplyToOk returns a tuple with the ReplyTo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReplyTo

`func (o *ListEmails200ResponseDataInner) SetReplyTo(v []string)`

SetReplyTo sets ReplyTo field to given value.


### GetLastEvent

`func (o *ListEmails200ResponseDataInner) GetLastEvent() string`

GetLastEvent returns the LastEvent field if non-nil, zero value otherwise.

### GetLastEventOk

`func (o *ListEmails200ResponseDataInner) GetLastEventOk() (*string, bool)`

GetLastEventOk returns a tuple with the LastEvent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastEvent

`func (o *ListEmails200ResponseDataInner) SetLastEvent(v string)`

SetLastEvent sets LastEvent field to given value.


### GetScheduledAt

`func (o *ListEmails200ResponseDataInner) GetScheduledAt() string`

GetScheduledAt returns the ScheduledAt field if non-nil, zero value otherwise.

### GetScheduledAtOk

`func (o *ListEmails200ResponseDataInner) GetScheduledAtOk() (*string, bool)`

GetScheduledAtOk returns a tuple with the ScheduledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledAt

`func (o *ListEmails200ResponseDataInner) SetScheduledAt(v string)`

SetScheduledAt sets ScheduledAt field to given value.


### SetScheduledAtNil

`func (o *ListEmails200ResponseDataInner) SetScheduledAtNil(b bool)`

 SetScheduledAtNil sets the value for ScheduledAt to be an explicit nil

### UnsetScheduledAt
`func (o *ListEmails200ResponseDataInner) UnsetScheduledAt()`

UnsetScheduledAt ensures that no value is present for ScheduledAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


