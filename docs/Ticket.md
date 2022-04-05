# Ticket

# The Ticket Object ### Description The `Ticket` object is used to represent a ticket or a task within a system.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The ticket&#39;s name. | [optional] 
**assignees** | **[str, none_type]** |  | [optional] 
**due_date** | **datetime, none_type** | The ticket&#39;s due date. | [optional] 
**status** | **object, none_type** | The current status of the ticket. | [optional] 
**description** | **str, none_type** | The ticket&#39;s description. | [optional] 
**project** | **str, none_type** |  | [optional] 
**ticket_type** | **str, none_type** | The ticket&#39;s type. | [optional] 
**account** | **str, none_type** |  | [optional] 
**contact** | **str, none_type** |  | [optional] 
**parent_ticket** | **str, none_type** |  | [optional] 
**attachments** | **[str, none_type]** |  | [optional] 
**tags** | **[str]** |  | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s ticket was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s ticket was updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


