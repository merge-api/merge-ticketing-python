# Comment

# The Comment Object ### Description The `Comment` object is used to represent a comment on a ticket.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**user** | **str, none_type** | The author of the Comment, if the author is a User. | [optional] 
**contact** | **str, none_type** | The author of the Comment, if the author is a Contact. | [optional] 
**body** | **str, none_type** | The comment&#39;s text body. | [optional] 
**html_body** | **str, none_type** | The comment&#39;s text body formatted as html. | [optional] 
**ticket** | **str, none_type** | The ticket associated with the comment.  | [optional] 
**is_private** | **bool, none_type** | Whether or not the comment is internal. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s comment was created. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


