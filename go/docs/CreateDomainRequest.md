# CreateDomainRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Region** | Pointer to **string** |  | [optional] 
**CustomReturnPath** | Pointer to **string** |  | [optional] 
**OpenTracking** | Pointer to **bool** |  | [optional] 
**ClickTracking** | Pointer to **bool** |  | [optional] 
**TrackingSubdomain** | Pointer to **NullableString** |  | [optional] 
**Tls** | Pointer to **string** |  | [optional] 

## Methods

### NewCreateDomainRequest

`func NewCreateDomainRequest(name string, ) *CreateDomainRequest`

NewCreateDomainRequest instantiates a new CreateDomainRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateDomainRequestWithDefaults

`func NewCreateDomainRequestWithDefaults() *CreateDomainRequest`

NewCreateDomainRequestWithDefaults instantiates a new CreateDomainRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateDomainRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateDomainRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateDomainRequest) SetName(v string)`

SetName sets Name field to given value.


### GetRegion

`func (o *CreateDomainRequest) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *CreateDomainRequest) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *CreateDomainRequest) SetRegion(v string)`

SetRegion sets Region field to given value.

### HasRegion

`func (o *CreateDomainRequest) HasRegion() bool`

HasRegion returns a boolean if a field has been set.

### GetCustomReturnPath

`func (o *CreateDomainRequest) GetCustomReturnPath() string`

GetCustomReturnPath returns the CustomReturnPath field if non-nil, zero value otherwise.

### GetCustomReturnPathOk

`func (o *CreateDomainRequest) GetCustomReturnPathOk() (*string, bool)`

GetCustomReturnPathOk returns a tuple with the CustomReturnPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomReturnPath

`func (o *CreateDomainRequest) SetCustomReturnPath(v string)`

SetCustomReturnPath sets CustomReturnPath field to given value.

### HasCustomReturnPath

`func (o *CreateDomainRequest) HasCustomReturnPath() bool`

HasCustomReturnPath returns a boolean if a field has been set.

### GetOpenTracking

`func (o *CreateDomainRequest) GetOpenTracking() bool`

GetOpenTracking returns the OpenTracking field if non-nil, zero value otherwise.

### GetOpenTrackingOk

`func (o *CreateDomainRequest) GetOpenTrackingOk() (*bool, bool)`

GetOpenTrackingOk returns a tuple with the OpenTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenTracking

`func (o *CreateDomainRequest) SetOpenTracking(v bool)`

SetOpenTracking sets OpenTracking field to given value.

### HasOpenTracking

`func (o *CreateDomainRequest) HasOpenTracking() bool`

HasOpenTracking returns a boolean if a field has been set.

### GetClickTracking

`func (o *CreateDomainRequest) GetClickTracking() bool`

GetClickTracking returns the ClickTracking field if non-nil, zero value otherwise.

### GetClickTrackingOk

`func (o *CreateDomainRequest) GetClickTrackingOk() (*bool, bool)`

GetClickTrackingOk returns a tuple with the ClickTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClickTracking

`func (o *CreateDomainRequest) SetClickTracking(v bool)`

SetClickTracking sets ClickTracking field to given value.

### HasClickTracking

`func (o *CreateDomainRequest) HasClickTracking() bool`

HasClickTracking returns a boolean if a field has been set.

### GetTrackingSubdomain

`func (o *CreateDomainRequest) GetTrackingSubdomain() string`

GetTrackingSubdomain returns the TrackingSubdomain field if non-nil, zero value otherwise.

### GetTrackingSubdomainOk

`func (o *CreateDomainRequest) GetTrackingSubdomainOk() (*string, bool)`

GetTrackingSubdomainOk returns a tuple with the TrackingSubdomain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackingSubdomain

`func (o *CreateDomainRequest) SetTrackingSubdomain(v string)`

SetTrackingSubdomain sets TrackingSubdomain field to given value.

### HasTrackingSubdomain

`func (o *CreateDomainRequest) HasTrackingSubdomain() bool`

HasTrackingSubdomain returns a boolean if a field has been set.

### SetTrackingSubdomainNil

`func (o *CreateDomainRequest) SetTrackingSubdomainNil(b bool)`

 SetTrackingSubdomainNil sets the value for TrackingSubdomain to be an explicit nil

### UnsetTrackingSubdomain
`func (o *CreateDomainRequest) UnsetTrackingSubdomain()`

UnsetTrackingSubdomain ensures that no value is present for TrackingSubdomain, not even an explicit nil
### GetTls

`func (o *CreateDomainRequest) GetTls() string`

GetTls returns the Tls field if non-nil, zero value otherwise.

### GetTlsOk

`func (o *CreateDomainRequest) GetTlsOk() (*string, bool)`

GetTlsOk returns a tuple with the Tls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTls

`func (o *CreateDomainRequest) SetTls(v string)`

SetTls sets Tls field to given value.

### HasTls

`func (o *CreateDomainRequest) HasTls() bool`

HasTls returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


