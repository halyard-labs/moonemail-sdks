# SendEmailRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**From** | **string** |  | 
**To** | [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | 
**Subject** | **string** |  | 
**Bcc** | Pointer to [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | [optional] 
**Cc** | Pointer to [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | [optional] 
**ReplyTo** | Pointer to [**SendEmailRequestTo**](SendEmailRequestTo.md) |  | [optional] 
**Html** | Pointer to **string** |  | [optional] 
**Text** | Pointer to **string** |  | [optional] 
**Headers** | Pointer to **map[string]string** |  | [optional] 
**Attachments** | Pointer to [**[]SendEmailRequestAttachmentsInner**](SendEmailRequestAttachmentsInner.md) |  | [optional] 
**Tags** | Pointer to [**[]SendEmailRequestTagsInner**](SendEmailRequestTagsInner.md) |  | [optional] 
**ScheduledAt** | Pointer to **string** |  | [optional] 

## Methods

### NewSendEmailRequest

`func NewSendEmailRequest(from string, to SendEmailRequestTo, subject string, ) *SendEmailRequest`

NewSendEmailRequest instantiates a new SendEmailRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSendEmailRequestWithDefaults

`func NewSendEmailRequestWithDefaults() *SendEmailRequest`

NewSendEmailRequestWithDefaults instantiates a new SendEmailRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFrom

`func (o *SendEmailRequest) GetFrom() string`

GetFrom returns the From field if non-nil, zero value otherwise.

### GetFromOk

`func (o *SendEmailRequest) GetFromOk() (*string, bool)`

GetFromOk returns a tuple with the From field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrom

`func (o *SendEmailRequest) SetFrom(v string)`

SetFrom sets From field to given value.


### GetTo

`func (o *SendEmailRequest) GetTo() SendEmailRequestTo`

GetTo returns the To field if non-nil, zero value otherwise.

### GetToOk

`func (o *SendEmailRequest) GetToOk() (*SendEmailRequestTo, bool)`

GetToOk returns a tuple with the To field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTo

`func (o *SendEmailRequest) SetTo(v SendEmailRequestTo)`

SetTo sets To field to given value.


### GetSubject

`func (o *SendEmailRequest) GetSubject() string`

GetSubject returns the Subject field if non-nil, zero value otherwise.

### GetSubjectOk

`func (o *SendEmailRequest) GetSubjectOk() (*string, bool)`

GetSubjectOk returns a tuple with the Subject field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubject

`func (o *SendEmailRequest) SetSubject(v string)`

SetSubject sets Subject field to given value.


### GetBcc

`func (o *SendEmailRequest) GetBcc() SendEmailRequestTo`

GetBcc returns the Bcc field if non-nil, zero value otherwise.

### GetBccOk

`func (o *SendEmailRequest) GetBccOk() (*SendEmailRequestTo, bool)`

GetBccOk returns a tuple with the Bcc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBcc

`func (o *SendEmailRequest) SetBcc(v SendEmailRequestTo)`

SetBcc sets Bcc field to given value.

### HasBcc

`func (o *SendEmailRequest) HasBcc() bool`

HasBcc returns a boolean if a field has been set.

### GetCc

`func (o *SendEmailRequest) GetCc() SendEmailRequestTo`

GetCc returns the Cc field if non-nil, zero value otherwise.

### GetCcOk

`func (o *SendEmailRequest) GetCcOk() (*SendEmailRequestTo, bool)`

GetCcOk returns a tuple with the Cc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCc

`func (o *SendEmailRequest) SetCc(v SendEmailRequestTo)`

SetCc sets Cc field to given value.

### HasCc

`func (o *SendEmailRequest) HasCc() bool`

HasCc returns a boolean if a field has been set.

### GetReplyTo

`func (o *SendEmailRequest) GetReplyTo() SendEmailRequestTo`

GetReplyTo returns the ReplyTo field if non-nil, zero value otherwise.

### GetReplyToOk

`func (o *SendEmailRequest) GetReplyToOk() (*SendEmailRequestTo, bool)`

GetReplyToOk returns a tuple with the ReplyTo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReplyTo

`func (o *SendEmailRequest) SetReplyTo(v SendEmailRequestTo)`

SetReplyTo sets ReplyTo field to given value.

### HasReplyTo

`func (o *SendEmailRequest) HasReplyTo() bool`

HasReplyTo returns a boolean if a field has been set.

### GetHtml

`func (o *SendEmailRequest) GetHtml() string`

GetHtml returns the Html field if non-nil, zero value otherwise.

### GetHtmlOk

`func (o *SendEmailRequest) GetHtmlOk() (*string, bool)`

GetHtmlOk returns a tuple with the Html field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtml

`func (o *SendEmailRequest) SetHtml(v string)`

SetHtml sets Html field to given value.

### HasHtml

`func (o *SendEmailRequest) HasHtml() bool`

HasHtml returns a boolean if a field has been set.

### GetText

`func (o *SendEmailRequest) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *SendEmailRequest) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *SendEmailRequest) SetText(v string)`

SetText sets Text field to given value.

### HasText

`func (o *SendEmailRequest) HasText() bool`

HasText returns a boolean if a field has been set.

### GetHeaders

`func (o *SendEmailRequest) GetHeaders() map[string]string`

GetHeaders returns the Headers field if non-nil, zero value otherwise.

### GetHeadersOk

`func (o *SendEmailRequest) GetHeadersOk() (*map[string]string, bool)`

GetHeadersOk returns a tuple with the Headers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeaders

`func (o *SendEmailRequest) SetHeaders(v map[string]string)`

SetHeaders sets Headers field to given value.

### HasHeaders

`func (o *SendEmailRequest) HasHeaders() bool`

HasHeaders returns a boolean if a field has been set.

### GetAttachments

`func (o *SendEmailRequest) GetAttachments() []SendEmailRequestAttachmentsInner`

GetAttachments returns the Attachments field if non-nil, zero value otherwise.

### GetAttachmentsOk

`func (o *SendEmailRequest) GetAttachmentsOk() (*[]SendEmailRequestAttachmentsInner, bool)`

GetAttachmentsOk returns a tuple with the Attachments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttachments

`func (o *SendEmailRequest) SetAttachments(v []SendEmailRequestAttachmentsInner)`

SetAttachments sets Attachments field to given value.

### HasAttachments

`func (o *SendEmailRequest) HasAttachments() bool`

HasAttachments returns a boolean if a field has been set.

### GetTags

`func (o *SendEmailRequest) GetTags() []SendEmailRequestTagsInner`

GetTags returns the Tags field if non-nil, zero value otherwise.

### GetTagsOk

`func (o *SendEmailRequest) GetTagsOk() (*[]SendEmailRequestTagsInner, bool)`

GetTagsOk returns a tuple with the Tags field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTags

`func (o *SendEmailRequest) SetTags(v []SendEmailRequestTagsInner)`

SetTags sets Tags field to given value.

### HasTags

`func (o *SendEmailRequest) HasTags() bool`

HasTags returns a boolean if a field has been set.

### GetScheduledAt

`func (o *SendEmailRequest) GetScheduledAt() string`

GetScheduledAt returns the ScheduledAt field if non-nil, zero value otherwise.

### GetScheduledAtOk

`func (o *SendEmailRequest) GetScheduledAtOk() (*string, bool)`

GetScheduledAtOk returns a tuple with the ScheduledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledAt

`func (o *SendEmailRequest) SetScheduledAt(v string)`

SetScheduledAt sets ScheduledAt field to given value.

### HasScheduledAt

`func (o *SendEmailRequest) HasScheduledAt() bool`

HasScheduledAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


