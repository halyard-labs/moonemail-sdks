# GetReceivedAttachment200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Filename** | **string** |  | 
**ContentType** | **string** |  | 
**ContentDisposition** | **string** |  | 
**ContentId** | Pointer to **string** |  | [optional] 
**Size** | **int32** |  | 
**DownloadUrl** | **string** | Private signed URL. Expires within five minutes; treat as a credential. | 
**ExpiresAt** | **string** |  | 

## Methods

### NewGetReceivedAttachment200Response

`func NewGetReceivedAttachment200Response(id string, filename string, contentType string, contentDisposition string, size int32, downloadUrl string, expiresAt string, ) *GetReceivedAttachment200Response`

NewGetReceivedAttachment200Response instantiates a new GetReceivedAttachment200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetReceivedAttachment200ResponseWithDefaults

`func NewGetReceivedAttachment200ResponseWithDefaults() *GetReceivedAttachment200Response`

NewGetReceivedAttachment200ResponseWithDefaults instantiates a new GetReceivedAttachment200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *GetReceivedAttachment200Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GetReceivedAttachment200Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GetReceivedAttachment200Response) SetId(v string)`

SetId sets Id field to given value.


### GetFilename

`func (o *GetReceivedAttachment200Response) GetFilename() string`

GetFilename returns the Filename field if non-nil, zero value otherwise.

### GetFilenameOk

`func (o *GetReceivedAttachment200Response) GetFilenameOk() (*string, bool)`

GetFilenameOk returns a tuple with the Filename field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilename

`func (o *GetReceivedAttachment200Response) SetFilename(v string)`

SetFilename sets Filename field to given value.


### GetContentType

`func (o *GetReceivedAttachment200Response) GetContentType() string`

GetContentType returns the ContentType field if non-nil, zero value otherwise.

### GetContentTypeOk

`func (o *GetReceivedAttachment200Response) GetContentTypeOk() (*string, bool)`

GetContentTypeOk returns a tuple with the ContentType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentType

`func (o *GetReceivedAttachment200Response) SetContentType(v string)`

SetContentType sets ContentType field to given value.


### GetContentDisposition

`func (o *GetReceivedAttachment200Response) GetContentDisposition() string`

GetContentDisposition returns the ContentDisposition field if non-nil, zero value otherwise.

### GetContentDispositionOk

`func (o *GetReceivedAttachment200Response) GetContentDispositionOk() (*string, bool)`

GetContentDispositionOk returns a tuple with the ContentDisposition field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentDisposition

`func (o *GetReceivedAttachment200Response) SetContentDisposition(v string)`

SetContentDisposition sets ContentDisposition field to given value.


### GetContentId

`func (o *GetReceivedAttachment200Response) GetContentId() string`

GetContentId returns the ContentId field if non-nil, zero value otherwise.

### GetContentIdOk

`func (o *GetReceivedAttachment200Response) GetContentIdOk() (*string, bool)`

GetContentIdOk returns a tuple with the ContentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentId

`func (o *GetReceivedAttachment200Response) SetContentId(v string)`

SetContentId sets ContentId field to given value.

### HasContentId

`func (o *GetReceivedAttachment200Response) HasContentId() bool`

HasContentId returns a boolean if a field has been set.

### GetSize

`func (o *GetReceivedAttachment200Response) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *GetReceivedAttachment200Response) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *GetReceivedAttachment200Response) SetSize(v int32)`

SetSize sets Size field to given value.


### GetDownloadUrl

`func (o *GetReceivedAttachment200Response) GetDownloadUrl() string`

GetDownloadUrl returns the DownloadUrl field if non-nil, zero value otherwise.

### GetDownloadUrlOk

`func (o *GetReceivedAttachment200Response) GetDownloadUrlOk() (*string, bool)`

GetDownloadUrlOk returns a tuple with the DownloadUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDownloadUrl

`func (o *GetReceivedAttachment200Response) SetDownloadUrl(v string)`

SetDownloadUrl sets DownloadUrl field to given value.


### GetExpiresAt

`func (o *GetReceivedAttachment200Response) GetExpiresAt() string`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GetReceivedAttachment200Response) GetExpiresAtOk() (*string, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GetReceivedAttachment200Response) SetExpiresAt(v string)`

SetExpiresAt sets ExpiresAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


