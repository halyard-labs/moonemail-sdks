# GetEmail200Response

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
**Object** | **string** |  | 
**Html** | **NullableString** |  | 
**Text** | **NullableString** |  | 
**Tags** | [**[]GetEmail200ResponseTagsInner**](GetEmail200ResponseTagsInner.md) |  | 

## Methods

### NewGetEmail200Response

`func NewGetEmail200Response(id string, messageId NullableString, to []string, from string, createdAt string, subject string, bcc []string, cc []string, replyTo []string, lastEvent string, scheduledAt NullableString, object string, html NullableString, text NullableString, tags []GetEmail200ResponseTagsInner, ) *GetEmail200Response`

NewGetEmail200Response instantiates a new GetEmail200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetEmail200ResponseWithDefaults

`func NewGetEmail200ResponseWithDefaults() *GetEmail200Response`

NewGetEmail200ResponseWithDefaults instantiates a new GetEmail200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *GetEmail200Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GetEmail200Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GetEmail200Response) SetId(v string)`

SetId sets Id field to given value.


### GetMessageId

`func (o *GetEmail200Response) GetMessageId() string`

GetMessageId returns the MessageId field if non-nil, zero value otherwise.

### GetMessageIdOk

`func (o *GetEmail200Response) GetMessageIdOk() (*string, bool)`

GetMessageIdOk returns a tuple with the MessageId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessageId

`func (o *GetEmail200Response) SetMessageId(v string)`

SetMessageId sets MessageId field to given value.


### SetMessageIdNil

`func (o *GetEmail200Response) SetMessageIdNil(b bool)`

 SetMessageIdNil sets the value for MessageId to be an explicit nil

### UnsetMessageId
`func (o *GetEmail200Response) UnsetMessageId()`

UnsetMessageId ensures that no value is present for MessageId, not even an explicit nil
### GetTo

`func (o *GetEmail200Response) GetTo() []string`

GetTo returns the To field if non-nil, zero value otherwise.

### GetToOk

`func (o *GetEmail200Response) GetToOk() (*[]string, bool)`

GetToOk returns a tuple with the To field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTo

`func (o *GetEmail200Response) SetTo(v []string)`

SetTo sets To field to given value.


### GetFrom

`func (o *GetEmail200Response) GetFrom() string`

GetFrom returns the From field if non-nil, zero value otherwise.

### GetFromOk

`func (o *GetEmail200Response) GetFromOk() (*string, bool)`

GetFromOk returns a tuple with the From field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrom

`func (o *GetEmail200Response) SetFrom(v string)`

SetFrom sets From field to given value.


### GetCreatedAt

`func (o *GetEmail200Response) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *GetEmail200Response) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *GetEmail200Response) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetSubject

`func (o *GetEmail200Response) GetSubject() string`

GetSubject returns the Subject field if non-nil, zero value otherwise.

### GetSubjectOk

`func (o *GetEmail200Response) GetSubjectOk() (*string, bool)`

GetSubjectOk returns a tuple with the Subject field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubject

`func (o *GetEmail200Response) SetSubject(v string)`

SetSubject sets Subject field to given value.


### GetBcc

`func (o *GetEmail200Response) GetBcc() []string`

GetBcc returns the Bcc field if non-nil, zero value otherwise.

### GetBccOk

`func (o *GetEmail200Response) GetBccOk() (*[]string, bool)`

GetBccOk returns a tuple with the Bcc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBcc

`func (o *GetEmail200Response) SetBcc(v []string)`

SetBcc sets Bcc field to given value.


### GetCc

`func (o *GetEmail200Response) GetCc() []string`

GetCc returns the Cc field if non-nil, zero value otherwise.

### GetCcOk

`func (o *GetEmail200Response) GetCcOk() (*[]string, bool)`

GetCcOk returns a tuple with the Cc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCc

`func (o *GetEmail200Response) SetCc(v []string)`

SetCc sets Cc field to given value.


### GetReplyTo

`func (o *GetEmail200Response) GetReplyTo() []string`

GetReplyTo returns the ReplyTo field if non-nil, zero value otherwise.

### GetReplyToOk

`func (o *GetEmail200Response) GetReplyToOk() (*[]string, bool)`

GetReplyToOk returns a tuple with the ReplyTo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReplyTo

`func (o *GetEmail200Response) SetReplyTo(v []string)`

SetReplyTo sets ReplyTo field to given value.


### GetLastEvent

`func (o *GetEmail200Response) GetLastEvent() string`

GetLastEvent returns the LastEvent field if non-nil, zero value otherwise.

### GetLastEventOk

`func (o *GetEmail200Response) GetLastEventOk() (*string, bool)`

GetLastEventOk returns a tuple with the LastEvent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastEvent

`func (o *GetEmail200Response) SetLastEvent(v string)`

SetLastEvent sets LastEvent field to given value.


### GetScheduledAt

`func (o *GetEmail200Response) GetScheduledAt() string`

GetScheduledAt returns the ScheduledAt field if non-nil, zero value otherwise.

### GetScheduledAtOk

`func (o *GetEmail200Response) GetScheduledAtOk() (*string, bool)`

GetScheduledAtOk returns a tuple with the ScheduledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledAt

`func (o *GetEmail200Response) SetScheduledAt(v string)`

SetScheduledAt sets ScheduledAt field to given value.


### SetScheduledAtNil

`func (o *GetEmail200Response) SetScheduledAtNil(b bool)`

 SetScheduledAtNil sets the value for ScheduledAt to be an explicit nil

### UnsetScheduledAt
`func (o *GetEmail200Response) UnsetScheduledAt()`

UnsetScheduledAt ensures that no value is present for ScheduledAt, not even an explicit nil
### GetObject

`func (o *GetEmail200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *GetEmail200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *GetEmail200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetHtml

`func (o *GetEmail200Response) GetHtml() string`

GetHtml returns the Html field if non-nil, zero value otherwise.

### GetHtmlOk

`func (o *GetEmail200Response) GetHtmlOk() (*string, bool)`

GetHtmlOk returns a tuple with the Html field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtml

`func (o *GetEmail200Response) SetHtml(v string)`

SetHtml sets Html field to given value.


### SetHtmlNil

`func (o *GetEmail200Response) SetHtmlNil(b bool)`

 SetHtmlNil sets the value for Html to be an explicit nil

### UnsetHtml
`func (o *GetEmail200Response) UnsetHtml()`

UnsetHtml ensures that no value is present for Html, not even an explicit nil
### GetText

`func (o *GetEmail200Response) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *GetEmail200Response) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *GetEmail200Response) SetText(v string)`

SetText sets Text field to given value.


### SetTextNil

`func (o *GetEmail200Response) SetTextNil(b bool)`

 SetTextNil sets the value for Text to be an explicit nil

### UnsetText
`func (o *GetEmail200Response) UnsetText()`

UnsetText ensures that no value is present for Text, not even an explicit nil
### GetTags

`func (o *GetEmail200Response) GetTags() []GetEmail200ResponseTagsInner`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *GetEmail200Response) GetTagsOk() (*[]GetEmail200ResponseTagsInner, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *GetEmail200Response) SetTags(v []GetEmail200ResponseTagsInner)`

SetTags sets Tags field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


