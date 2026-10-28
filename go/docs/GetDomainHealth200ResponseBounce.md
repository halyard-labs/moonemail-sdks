# GetDomainHealth200ResponseBounce

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Rate** | **NullableFloat32** | Fraction, not percentage. Null means no usable sample. | 
**ObservedAt** | **NullableString** |  | 
**State** | **string** |  | 
**ReviewThreshold** | **float32** |  | 

## Methods

### NewGetDomainHealth200ResponseBounce

`func NewGetDomainHealth200ResponseBounce(rate NullableFloat32, observedAt NullableString, state string, reviewThreshold float32, ) *GetDomainHealth200ResponseBounce`

NewGetDomainHealth200ResponseBounce instantiates a new GetDomainHealth200ResponseBounce object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetDomainHealth200ResponseBounceWithDefaults

`func NewGetDomainHealth200ResponseBounceWithDefaults() *GetDomainHealth200ResponseBounce`

NewGetDomainHealth200ResponseBounceWithDefaults instantiates a new GetDomainHealth200ResponseBounce object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRate

`func (o *GetDomainHealth200ResponseBounce) GetRate() float32`

GetRate returns the Rate field if non-nil, zero value otherwise.

### GetRateOk

`func (o *GetDomainHealth200ResponseBounce) GetRateOk() (*float32, bool)`

GetRateOk returns a tuple with the Rate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRate

`func (o *GetDomainHealth200ResponseBounce) SetRate(v float32)`

SetRate sets Rate field to given value.


### SetRateNil

`func (o *GetDomainHealth200ResponseBounce) SetRateNil(b bool)`

 SetRateNil sets the value for Rate to be an explicit nil

### UnsetRate
`func (o *GetDomainHealth200ResponseBounce) UnsetRate()`

UnsetRate ensures that no value is present for Rate, not even an explicit nil
### GetObservedAt

`func (o *GetDomainHealth200ResponseBounce) GetObservedAt() string`

GetObservedAt returns the ObservedAt field if non-nil, zero value otherwise.

### GetObservedAtOk

`func (o *GetDomainHealth200ResponseBounce) GetObservedAtOk() (*string, bool)`

GetObservedAtOk returns a tuple with the ObservedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObservedAt

`func (o *GetDomainHealth200ResponseBounce) SetObservedAt(v string)`

SetObservedAt sets ObservedAt field to given value.


### SetObservedAtNil

`func (o *GetDomainHealth200ResponseBounce) SetObservedAtNil(b bool)`

 SetObservedAtNil sets the value for ObservedAt to be an explicit nil

### UnsetObservedAt
`func (o *GetDomainHealth200ResponseBounce) UnsetObservedAt()`

UnsetObservedAt ensures that no value is present for ObservedAt, not even an explicit nil
### GetState

`func (o *GetDomainHealth200ResponseBounce) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *GetDomainHealth200ResponseBounce) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *GetDomainHealth200ResponseBounce) SetState(v string)`

SetState sets State field to given value.


### GetReviewThreshold

`func (o *GetDomainHealth200ResponseBounce) GetReviewThreshold() float32`

GetReviewThreshold returns the ReviewThreshold field if non-nil, zero value otherwise.

### GetReviewThresholdOk

`func (o *GetDomainHealth200ResponseBounce) GetReviewThresholdOk() (*float32, bool)`

GetReviewThresholdOk returns a tuple with the ReviewThreshold field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewThreshold

`func (o *GetDomainHealth200ResponseBounce) SetReviewThreshold(v float32)`

SetReviewThreshold sets ReviewThreshold field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


