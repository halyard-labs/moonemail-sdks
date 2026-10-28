# GetDomainHealth200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CheckedAt** | **string** |  | 
**SendingEnabled** | **NullableBool** |  | 
**MetricsEnabled** | **bool** |  | 
**SendingSuspended** | **bool** |  | 
**Bounce** | [**GetDomainHealth200ResponseBounce**](GetDomainHealth200ResponseBounce.md) |  | 
**Complaint** | [**GetDomainHealth200ResponseBounce**](GetDomainHealth200ResponseBounce.md) |  | 

## Methods

### NewGetDomainHealth200Response

`func NewGetDomainHealth200Response(checkedAt string, sendingEnabled NullableBool, metricsEnabled bool, sendingSuspended bool, bounce GetDomainHealth200ResponseBounce, complaint GetDomainHealth200ResponseBounce, ) *GetDomainHealth200Response`

NewGetDomainHealth200Response instantiates a new GetDomainHealth200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetDomainHealth200ResponseWithDefaults

`func NewGetDomainHealth200ResponseWithDefaults() *GetDomainHealth200Response`

NewGetDomainHealth200ResponseWithDefaults instantiates a new GetDomainHealth200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCheckedAt

`func (o *GetDomainHealth200Response) GetCheckedAt() string`

GetCheckedAt returns the CheckedAt field if non-nil, zero value otherwise.

### GetCheckedAtOk

`func (o *GetDomainHealth200Response) GetCheckedAtOk() (*string, bool)`

GetCheckedAtOk returns a tuple with the CheckedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckedAt

`func (o *GetDomainHealth200Response) SetCheckedAt(v string)`

SetCheckedAt sets CheckedAt field to given value.


### GetSendingEnabled

`func (o *GetDomainHealth200Response) GetSendingEnabled() bool`

GetSendingEnabled returns the SendingEnabled field if non-nil, zero value otherwise.

### GetSendingEnabledOk

`func (o *GetDomainHealth200Response) GetSendingEnabledOk() (*bool, bool)`

GetSendingEnabledOk returns a tuple with the SendingEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSendingEnabled

`func (o *GetDomainHealth200Response) SetSendingEnabled(v bool)`

SetSendingEnabled sets SendingEnabled field to given value.


### SetSendingEnabledNil

`func (o *GetDomainHealth200Response) SetSendingEnabledNil(b bool)`

 SetSendingEnabledNil sets the value for SendingEnabled to be an explicit nil

### UnsetSendingEnabled
`func (o *GetDomainHealth200Response) UnsetSendingEnabled()`

UnsetSendingEnabled ensures that no value is present for SendingEnabled, not even an explicit nil
### GetMetricsEnabled

`func (o *GetDomainHealth200Response) GetMetricsEnabled() bool`

GetMetricsEnabled returns the MetricsEnabled field if non-nil, zero value otherwise.

### GetMetricsEnabledOk

`func (o *GetDomainHealth200Response) GetMetricsEnabledOk() (*bool, bool)`

GetMetricsEnabledOk returns a tuple with the MetricsEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetricsEnabled

`func (o *GetDomainHealth200Response) SetMetricsEnabled(v bool)`

SetMetricsEnabled sets MetricsEnabled field to given value.


### GetSendingSuspended

`func (o *GetDomainHealth200Response) GetSendingSuspended() bool`

GetSendingSuspended returns the SendingSuspended field if non-nil, zero value otherwise.

### GetSendingSuspendedOk

`func (o *GetDomainHealth200Response) GetSendingSuspendedOk() (*bool, bool)`

GetSendingSuspendedOk returns a tuple with the SendingSuspended field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSendingSuspended

`func (o *GetDomainHealth200Response) SetSendingSuspended(v bool)`

SetSendingSuspended sets SendingSuspended field to given value.


### GetBounce

`func (o *GetDomainHealth200Response) GetBounce() GetDomainHealth200ResponseBounce`

GetBounce returns the Bounce field if non-nil, zero value otherwise.

### GetBounceOk

`func (o *GetDomainHealth200Response) GetBounceOk() (*GetDomainHealth200ResponseBounce, bool)`

GetBounceOk returns a tuple with the Bounce field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBounce

`func (o *GetDomainHealth200Response) SetBounce(v GetDomainHealth200ResponseBounce)`

SetBounce sets Bounce field to given value.


### GetComplaint

`func (o *GetDomainHealth200Response) GetComplaint() GetDomainHealth200ResponseBounce`

GetComplaint returns the Complaint field if non-nil, zero value otherwise.

### GetComplaintOk

`func (o *GetDomainHealth200Response) GetComplaintOk() (*GetDomainHealth200ResponseBounce, bool)`

GetComplaintOk returns a tuple with the Complaint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComplaint

`func (o *GetDomainHealth200Response) SetComplaint(v GetDomainHealth200ResponseBounce)`

SetComplaint sets Complaint field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


