# UpdateDomainRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OpenTracking** | Pointer to **bool** |  | [optional] 
**ClickTracking** | Pointer to **bool** |  | [optional] 
**TrackingSubdomain** | Pointer to **NullableString** |  | [optional] 
**Tls** | Pointer to **string** |  | [optional] 

## Methods

### NewUpdateDomainRequest

`func NewUpdateDomainRequest() *UpdateDomainRequest`

NewUpdateDomainRequest instantiates a new UpdateDomainRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateDomainRequestWithDefaults

`func NewUpdateDomainRequestWithDefaults() *UpdateDomainRequest`

NewUpdateDomainRequestWithDefaults instantiates a new UpdateDomainRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOpenTracking

`func (o *UpdateDomainRequest) GetOpenTracking() bool`

GetOpenTracking returns the OpenTracking field if non-nil, zero value otherwise.

### GetOpenTrackingOk

`func (o *UpdateDomainRequest) GetOpenTrackingOk() (*bool, bool)`

GetOpenTrackingOk returns a tuple with the OpenTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpenTracking

`func (o *UpdateDomainRequest) SetOpenTracking(v bool)`

SetOpenTracking sets OpenTracking field to given value.

### HasOpenTracking

`func (o *UpdateDomainRequest) HasOpenTracking() bool`

HasOpenTracking returns a boolean if a field has been set.

### GetClickTracking

`func (o *UpdateDomainRequest) GetClickTracking() bool`

GetClickTracking returns the ClickTracking field if non-nil, zero value otherwise.

### GetClickTrackingOk

`func (o *UpdateDomainRequest) GetClickTrackingOk() (*bool, bool)`

GetClickTrackingOk returns a tuple with the ClickTracking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClickTracking

`func (o *UpdateDomainRequest) SetClickTracking(v bool)`

SetClickTracking sets ClickTracking field to given value.

### HasClickTracking

`func (o *UpdateDomainRequest) HasClickTracking() bool`

HasClickTracking returns a boolean if a field has been set.

### GetTrackingSubdomain

`func (o *UpdateDomainRequest) GetTrackingSubdomain() string`

GetTrackingSubdomain returns the TrackingSubdomain field if non-nil, zero value otherwise.

### GetTrackingSubdomainOk

`func (o *UpdateDomainRequest) GetTrackingSubdomainOk() (*string, bool)`

GetTrackingSubdomainOk returns a tuple with the TrackingSubdomain field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrackingSubdomain

`func (o *UpdateDomainRequest) SetTrackingSubdomain(v string)`

SetTrackingSubdomain sets TrackingSubdomain field to given value.

### HasTrackingSubdomain

`func (o *UpdateDomainRequest) HasTrackingSubdomain() bool`

HasTrackingSubdomain returns a boolean if a field has been set.

### SetTrackingSubdomainNil

`func (o *UpdateDomainRequest) SetTrackingSubdomainNil(b bool)`

 SetTrackingSubdomainNil sets the value for TrackingSubdomain to be an explicit nil

### UnsetTrackingSubdomain
`func (o *UpdateDomainRequest) UnsetTrackingSubdomain()`

UnsetTrackingSubdomain ensures that no value is present for TrackingSubdomain, not even an explicit nil
### GetTls

`func (o *UpdateDomainRequest) GetTls() string`

GetTls returns the Tls field if non-nil, zero value otherwise.

### GetTlsOk

`func (o *UpdateDomainRequest) GetTlsOk() (*string, bool)`

GetTlsOk returns a tuple with the Tls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTls

`func (o *UpdateDomainRequest) SetTls(v string)`

SetTls sets Tls field to given value.

### HasTls

`func (o *UpdateDomainRequest) HasTls() bool`

HasTls returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


