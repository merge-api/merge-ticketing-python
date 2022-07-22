# User

# The User Object ### Description The `User` object is used to represent an employee within a company.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The user&#39;s name. | [optional] 
**email_address** | **str, none_type** | The user&#39;s email address. | [optional] 
**is_active** | **bool, none_type** | Whether or not the user is active. | [optional] 
**teams** | **[str, none_type]** |  | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


