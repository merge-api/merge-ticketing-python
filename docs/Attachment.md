# Attachment

# The Attachment Object ### Description The `Attachment` object is used to represent an attachment for a ticket.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**file_name** | **str, none_type** | The attachment&#39;s name. | [optional] 
**ticket** | **str, none_type** | The ticket associated with the attachment. | [optional] 
**file_url** | **str, none_type** | The attachment&#39;s url. | [optional] 
**content_type** | **str, none_type** | The attachment&#39;s file format. | [optional] 
**uploaded_by** | **str, none_type** | The user who uploaded the attachment. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s attachment was created. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


