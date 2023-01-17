# TicketRequest

# The Ticket Object ### Description The `Ticket` object is used to represent a ticket or a task within a system.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The ticket&#39;s name. | [optional] 
**assignees** | **[str, none_type]** |  | [optional] 
**creator** | **str, none_type** | The user who created this ticket. | [optional] 
**due_date** | **datetime, none_type** | The ticket&#39;s due date. | [optional] 
**status** | **object, none_type** | The current status of the ticket. | [optional] 
**description** | **str, none_type** | The ticket’s description. HTML version of description is mapped if supported by the third-party platform. | [optional] 
**project** | **str, none_type** | The project the ticket belongs to. | [optional] 
**collections** | **[str, none_type]** |  | [optional] 
**ticket_type** | **str, none_type** | The ticket&#39;s type. | [optional] 
**account** | **str, none_type** | The account associated with the ticket. | [optional] 
**contact** | **str, none_type** | The contact associated with the ticket. | [optional] 
**parent_ticket** | **str, none_type** | The ticket&#39;s parent ticket. | [optional] 
**attachments** | **[str, none_type]** |  | [optional] 
**tags** | **[str]** |  | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s ticket was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s ticket was updated. | [optional] 
**completed_at** | **datetime, none_type** | When the ticket was completed. | [optional] 
**ticket_url** | **str, none_type** | The 3rd party url of the Ticket. | [optional] 
**priority** | **object, none_type** | The priority or urgency of the Ticket. Possible values include: URGENT, HIGH, NORMAL, LOW - in cases where there is no clear mapping - the original value passed through. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


