# GetReceivedEmail200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**InboxId** | **string** |  | 
**From** | **string** |  | 
**To** | **[]string** |  | 
**Subject** | **string** |  | 
**MessageId** | **string** |  | 
**CreatedAt** | **string** |  | 
**Status** | **string** |  | 
**QuarantineReason** | Pointer to **string** |  | [optional] 
**Attachments** | [**[]ListReceivedEmails200ResponseDataInnerAttachmentsInner**](ListReceivedEmails200ResponseDataInnerAttachmentsInner.md) |  | 
**ExpiresAt** | **int32** | Expiry as Unix seconds. | 
**Authentication** | Pointer to [**ListReceivedEmails200ResponseDataInnerAuthentication**](ListReceivedEmails200ResponseDataInnerAuthentication.md) |  | [optional] 
**Html** | Pointer to **string** |  | [optional] 
**Text** | Pointer to **string** |  | [optional] 
**Headers** | Pointer to **map[string][]string** |  | [optional] 

## Methods

### NewGetReceivedEmail200Response

`func NewGetReceivedEmail200Response(id string, inboxId string, from string, to []string, subject string, messageId string, createdAt string, status string, attachments []ListReceivedEmails200ResponseDataInnerAttachmentsInner, expiresAt int32, ) *GetReceivedEmail200Response`

NewGetReceivedEmail200Response instantiates a new GetReceivedEmail200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetReceivedEmail200ResponseWithDefaults

`func NewGetReceivedEmail200ResponseWithDefaults() *GetReceivedEmail200Response`

NewGetReceivedEmail200ResponseWithDefaults instantiates a new GetReceivedEmail200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *GetReceivedEmail200Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GetReceivedEmail200Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GetReceivedEmail200Response) SetId(v string)`

SetId sets Id field to given value.


### GetInboxId

`func (o *GetReceivedEmail200Response) GetInboxId() string`

GetInboxId returns the InboxId field if non-nil, zero value otherwise.

### GetInboxIdOk

`func (o *GetReceivedEmail200Response) GetInboxIdOk() (*string, bool)`

GetInboxIdOk returns a tuple with the InboxId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInboxId

`func (o *GetReceivedEmail200Response) SetInboxId(v string)`

SetInboxId sets InboxId field to given value.


### GetFrom

`func (o *GetReceivedEmail200Response) GetFrom() string`

GetFrom returns the From field if non-nil, zero value otherwise.

### GetFromOk

`func (o *GetReceivedEmail200Response) GetFromOk() (*string, bool)`

GetFromOk returns a tuple with the From field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrom

`func (o *GetReceivedEmail200Response) SetFrom(v string)`

SetFrom sets From field to given value.


### GetTo

`func (o *GetReceivedEmail200Response) GetTo() []string`

GetTo returns the To field if non-nil, zero value otherwise.

### GetToOk

`func (o *GetReceivedEmail200Response) GetToOk() (*[]string, bool)`

GetToOk returns a tuple with the To field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTo

`func (o *GetReceivedEmail200Response) SetTo(v []string)`

SetTo sets To field to given value.


### SetToNil

`func (o *GetReceivedEmail200Response) SetToNil(b bool)`

 SetToNil sets the value for To to be an explicit nil

### UnsetTo
`func (o *GetReceivedEmail200Response) UnsetTo()`

UnsetTo ensures that no value is present for To, not even an explicit nil
### GetSubject

`func (o *GetReceivedEmail200Response) GetSubject() string`

GetSubject returns the Subject field if non-nil, zero value otherwise.

### GetSubjectOk

`func (o *GetReceivedEmail200Response) GetSubjectOk() (*string, bool)`

GetSubjectOk returns a tuple with the Subject field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubject

`func (o *GetReceivedEmail200Response) SetSubject(v string)`

SetSubject sets Subject field to given value.


### GetMessageId

`func (o *GetReceivedEmail200Response) GetMessageId() string`

GetMessageId returns the MessageId field if non-nil, zero value otherwise.

### GetMessageIdOk

`func (o *GetReceivedEmail200Response) GetMessageIdOk() (*string, bool)`

GetMessageIdOk returns a tuple with the MessageId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessageId

`func (o *GetReceivedEmail200Response) SetMessageId(v string)`

SetMessageId sets MessageId field to given value.


### GetCreatedAt

`func (o *GetReceivedEmail200Response) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *GetReceivedEmail200Response) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *GetReceivedEmail200Response) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetStatus

`func (o *GetReceivedEmail200Response) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *GetReceivedEmail200Response) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *GetReceivedEmail200Response) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetQuarantineReason

`func (o *GetReceivedEmail200Response) GetQuarantineReason() string`

GetQuarantineReason returns the QuarantineReason field if non-nil, zero value otherwise.

### GetQuarantineReasonOk

`func (o *GetReceivedEmail200Response) GetQuarantineReasonOk() (*string, bool)`

GetQuarantineReasonOk returns a tuple with the QuarantineReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuarantineReason

`func (o *GetReceivedEmail200Response) SetQuarantineReason(v string)`

SetQuarantineReason sets QuarantineReason field to given value.

### HasQuarantineReason

`func (o *GetReceivedEmail200Response) HasQuarantineReason() bool`

HasQuarantineReason returns a boolean if a field has been set.

### GetAttachments

`func (o *GetReceivedEmail200Response) GetAttachments() []ListReceivedEmails200ResponseDataInnerAttachmentsInner`

GetAttachments returns the Attachments field if non-nil, zero value otherwise.

### GetAttachmentsOk

`func (o *GetReceivedEmail200Response) GetAttachmentsOk() (*[]ListReceivedEmails200ResponseDataInnerAttachmentsInner, bool)`

GetAttachmentsOk returns a tuple with the Attachments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttachments

`func (o *GetReceivedEmail200Response) SetAttachments(v []ListReceivedEmails200ResponseDataInnerAttachmentsInner)`

SetAttachments sets Attachments field to given value.


### SetAttachmentsNil

`func (o *GetReceivedEmail200Response) SetAttachmentsNil(b bool)`

 SetAttachmentsNil sets the value for Attachments to be an explicit nil

### UnsetAttachments
`func (o *GetReceivedEmail200Response) UnsetAttachments()`

UnsetAttachments ensures that no value is present for Attachments, not even an explicit nil
### GetExpiresAt

`func (o *GetReceivedEmail200Response) GetExpiresAt() int32`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GetReceivedEmail200Response) GetExpiresAtOk() (*int32, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GetReceivedEmail200Response) SetExpiresAt(v int32)`

SetExpiresAt sets ExpiresAt field to given value.


### GetAuthentication

`func (o *GetReceivedEmail200Response) GetAuthentication() ListReceivedEmails200ResponseDataInnerAuthentication`

GetAuthentication returns the Authentication field if non-nil, zero value otherwise.

### GetAuthenticationOk

`func (o *GetReceivedEmail200Response) GetAuthenticationOk() (*ListReceivedEmails200ResponseDataInnerAuthentication, bool)`

GetAuthenticationOk returns a tuple with the Authentication field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthentication

`func (o *GetReceivedEmail200Response) SetAuthentication(v ListReceivedEmails200ResponseDataInnerAuthentication)`

SetAuthentication sets Authentication field to given value.

### HasAuthentication

`func (o *GetReceivedEmail200Response) HasAuthentication() bool`

HasAuthentication returns a boolean if a field has been set.

### GetHtml

`func (o *GetReceivedEmail200Response) GetHtml() string`

GetHtml returns the Html field if non-nil, zero value otherwise.

### GetHtmlOk

`func (o *GetReceivedEmail200Response) GetHtmlOk() (*string, bool)`

GetHtmlOk returns a tuple with the Html field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHtml

`func (o *GetReceivedEmail200Response) SetHtml(v string)`

SetHtml sets Html field to given value.

### HasHtml

`func (o *GetReceivedEmail200Response) HasHtml() bool`

HasHtml returns a boolean if a field has been set.

### GetText

`func (o *GetReceivedEmail200Response) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *GetReceivedEmail200Response) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *GetReceivedEmail200Response) SetText(v string)`

SetText sets Text field to given value.

### HasText

`func (o *GetReceivedEmail200Response) HasText() bool`

HasText returns a boolean if a field has been set.

### GetHeaders

`func (o *GetReceivedEmail200Response) GetHeaders() map[string][]string`

GetHeaders returns the Headers field if non-nil, zero value otherwise.

### GetHeadersOk

`func (o *GetReceivedEmail200Response) GetHeadersOk() (*map[string][]string, bool)`

GetHeadersOk returns a tuple with the Headers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeaders

`func (o *GetReceivedEmail200Response) SetHeaders(v map[string][]string)`

SetHeaders sets Headers field to given value.

### HasHeaders

`func (o *GetReceivedEmail200Response) HasHeaders() bool`

HasHeaders returns a boolean if a field has been set.

### SetHeadersNil

`func (o *GetReceivedEmail200Response) SetHeadersNil(b bool)`

 SetHeadersNil sets the value for Headers to be an explicit nil

### UnsetHeaders
`func (o *GetReceivedEmail200Response) UnsetHeaders()`

UnsetHeaders ensures that no value is present for Headers, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


