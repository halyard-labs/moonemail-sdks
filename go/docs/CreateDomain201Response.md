# CreateDomain201Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**Status** | **string** |  | 
**CreatedAt** | **string** |  | 
**Region** | **string** |  | 
**Object** | **string** |  | 
**OpenTracking** | **bool** |  | 
**ClickTracking** | **bool** |  | 
**TrackingSubdomain** | **NullableString** |  | 
**CustomReturnPath** | **string** |  | 
**Tls** | **string** |  | 
**Capabilities** | [**CreateDomain201ResponseCapabilities**](CreateDomain201ResponseCapabilities.md) |  | 
**Records** | [**[]CreateDomain201ResponseRecordsInner**](CreateDomain201ResponseRecordsInner.md) |  | 

## Methods

### NewCreateDomain201Response

`func NewCreateDomain201Response(id string, name string, status string, createdAt string, region string, object string, openTracking bool, clickTracking bool, trackingSubdomain NullableString, customReturnPath string, tls string, capabilities CreateDomain201ResponseCapabilities, records []CreateDomain201ResponseRecordsInner, ) *CreateDomain201Response`

NewCreateDomain201Response instantiates a new CreateDomain201Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateDomain201ResponseWithDefaults

`func NewCreateDomain201ResponseWithDefaults() *CreateDomain201Response`

NewCreateDomain201ResponseWithDefaults instantiates a new CreateDomain201Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *CreateDomain201Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CreateDomain201Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CreateDomain201Response) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *CreateDomain201Response) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateDomain201Response) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateDomain201Response) SetName(v string)`

SetName sets Name field to given value.


### GetStatus

`func (o *CreateDomain201Response) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *CreateDomain201Response) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *CreateDomain201Response) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedAt

`func (o *CreateDomain201Response) GetCreatedAt() string`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *CreateDomain201Response) GetCreatedAtOk() (*string, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *CreateDomain201Response) SetCreatedAt(v string)`

SetCreatedAt sets CreatedAt field to given value.


### GetRegion

`func (o *CreateDomain201Response) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *CreateDomain201Response) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *CreateDomain201Response) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetObject

`func (o *CreateDomain201Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *CreateDomain201Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *CreateDomain201Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetOpenTracking

`func (o *CreateDomain201Response) GetOpenTracking() bool`

GetOpenTracking returns the OpenTracking field if non-nil, zero value otherwise.

### GetOpenTrackingOk

`func (o *CreateDomain201Response) GetOpenTrackingOk() (*bool, bool)`

GetOpenTrackingOk returns a tuple with the OpenTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenTracking

`func (o *CreateDomain201Response) SetOpenTracking(v bool)`

SetOpenTracking sets OpenTracking field to given value.


### GetClickTracking

`func (o *CreateDomain201Response) GetClickTracking() bool`

GetClickTracking returns the ClickTracking field if non-nil, zero value otherwise.

### GetClickTrackingOk

`func (o *CreateDomain201Response) GetClickTrackingOk() (*bool, bool)`

GetClickTrackingOk returns a tuple with the ClickTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClickTracking

`func (o *CreateDomain201Response) SetClickTracking(v bool)`

SetClickTracking sets ClickTracking field to given value.


### GetTrackingSubdomain

`func (o *CreateDomain201Response) GetTrackingSubdomain() string`

GetTrackingSubdomain returns the TrackingSubdomain field if non-nil, zero value otherwise.

### GetTrackingSubdomainOk

`func (o *CreateDomain201Response) GetTrackingSubdomainOk() (*string, bool)`

GetTrackingSubdomainOk returns a tuple with the TrackingSubdomain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackingSubdomain

`func (o *CreateDomain201Response) SetTrackingSubdomain(v string)`

SetTrackingSubdomain sets TrackingSubdomain field to given value.


### SetTrackingSubdomainNil

`func (o *CreateDomain201Response) SetTrackingSubdomainNil(b bool)`

 SetTrackingSubdomainNil sets the value for TrackingSubdomain to be an explicit nil

### UnsetTrackingSubdomain
`func (o *CreateDomain201Response) UnsetTrackingSubdomain()`

UnsetTrackingSubdomain ensures that no value is present for TrackingSubdomain, not even an explicit nil
### GetCustomReturnPath

`func (o *CreateDomain201Response) GetCustomReturnPath() string`

GetCustomReturnPath returns the CustomReturnPath field if non-nil, zero value otherwise.

### GetCustomReturnPathOk

`func (o *CreateDomain201Response) GetCustomReturnPathOk() (*string, bool)`

GetCustomReturnPathOk returns a tuple with the CustomReturnPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomReturnPath

`func (o *CreateDomain201Response) SetCustomReturnPath(v string)`

SetCustomReturnPath sets CustomReturnPath field to given value.


### GetTls

`func (o *CreateDomain201Response) GetTls() string`

GetTls returns the Tls field if non-nil, zero value otherwise.

### GetTlsOk

`func (o *CreateDomain201Response) GetTlsOk() (*string, bool)`

GetTlsOk returns a tuple with the Tls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTls

`func (o *CreateDomain201Response) SetTls(v string)`

SetTls sets Tls field to given value.


### GetCapabilities

`func (o *CreateDomain201Response) GetCapabilities() CreateDomain201ResponseCapabilities`

GetCapabilities returns the Capabilities field if non-nil, zero value otherwise.

### GetCapabilitiesOk

`func (o *CreateDomain201Response) GetCapabilitiesOk() (*CreateDomain201ResponseCapabilities, bool)`

GetCapabilitiesOk returns a tuple with the Capabilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCapabilities

`func (o *CreateDomain201Response) SetCapabilities(v CreateDomain201ResponseCapabilities)`

SetCapabilities sets Capabilities field to given value.


### GetRecords

`func (o *CreateDomain201Response) GetRecords() []CreateDomain201ResponseRecordsInner`

GetRecords returns the Records field if non-nil, zero value otherwise.

### GetRecordsOk

`func (o *CreateDomain201Response) GetRecordsOk() (*[]CreateDomain201ResponseRecordsInner, bool)`

GetRecordsOk returns a tuple with the Records field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRecords

`func (o *CreateDomain201Response) SetRecords(v []CreateDomain201ResponseRecordsInner)`

SetRecords sets Records field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


