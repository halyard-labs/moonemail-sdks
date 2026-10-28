# GetReceivedRaw200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DownloadUrl** | **string** | Private signed URL. Expires within five minutes; treat as a credential. | 
**ExpiresAt** | **string** |  | 

## Methods

### NewGetReceivedRaw200Response

`func NewGetReceivedRaw200Response(downloadUrl string, expiresAt string, ) *GetReceivedRaw200Response`

NewGetReceivedRaw200Response instantiates a new GetReceivedRaw200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetReceivedRaw200ResponseWithDefaults

`func NewGetReceivedRaw200ResponseWithDefaults() *GetReceivedRaw200Response`

NewGetReceivedRaw200ResponseWithDefaults instantiates a new GetReceivedRaw200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDownloadUrl

`func (o *GetReceivedRaw200Response) GetDownloadUrl() string`

GetDownloadUrl returns the DownloadUrl field if non-nil, zero value otherwise.

### GetDownloadUrlOk

`func (o *GetReceivedRaw200Response) GetDownloadUrlOk() (*string, bool)`

GetDownloadUrlOk returns a tuple with the DownloadUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDownloadUrl

`func (o *GetReceivedRaw200Response) SetDownloadUrl(v string)`

SetDownloadUrl sets DownloadUrl field to given value.


### GetExpiresAt

`func (o *GetReceivedRaw200Response) GetExpiresAt() string`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *GetReceivedRaw200Response) GetExpiresAtOk() (*string, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *GetReceivedRaw200Response) SetExpiresAt(v string)`

SetExpiresAt sets ExpiresAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


