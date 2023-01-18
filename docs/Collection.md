# Collection

# The Collection Object ### Description The `Collection` object is used to represent collections of tickets. Collections may include other collections as sub collections.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The collection&#39;s name. | [optional] 
**description** | **str, none_type** | The collection&#39;s description. | [optional] 
**collection_type** | **object, none_type** | The collection&#39;s type. | [optional] 
**parent_collection** | **str, none_type** | The parent collection for this collection. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


