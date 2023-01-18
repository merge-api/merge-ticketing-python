# MergeTicketingClient
The unified API for building rich integrations with multiple Ticketing platforms.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.1.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.merge.dev/](https://www.merge.dev/)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/merge-api/merge-ticketing-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/merge-api/merge-ticketing-python.git`)

Then import the package:
```python
import MergeTicketingClient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import MergeTicketingClient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import MergeTicketingClient
from pprint import pprint
from MergeTicketingClient.api import account_details_api
from MergeTicketingClient.model.account_details import AccountDetails
# Defining the host is optional and defaults to https://api.merge.dev/api/ticketing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeTicketingClient.Configuration(
    host = "https://api.merge.dev/api/ticketing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with MergeTicketingClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_details_api.AccountDetailsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    try:
        api_response = api_instance.account_details_retrieve(x_account_token)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling AccountDetailsApi->account_details_retrieve: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.merge.dev/api/ticketing/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountDetailsApi* | [**account_details_retrieve**](docs/AccountDetailsApi.md#account_details_retrieve) | **GET** /account-details | 
*AccountTokenApi* | [**account_token_retrieve**](docs/AccountTokenApi.md#account_token_retrieve) | **GET** /account-token/{public_token} | 
*AccountsApi* | [**accounts_list**](docs/AccountsApi.md#accounts_list) | **GET** /accounts | 
*AccountsApi* | [**accounts_retrieve**](docs/AccountsApi.md#accounts_retrieve) | **GET** /accounts/{id} | 
*AttachmentsApi* | [**attachments_create**](docs/AttachmentsApi.md#attachments_create) | **POST** /attachments | 
*AttachmentsApi* | [**attachments_list**](docs/AttachmentsApi.md#attachments_list) | **GET** /attachments | 
*AttachmentsApi* | [**attachments_meta_post_retrieve**](docs/AttachmentsApi.md#attachments_meta_post_retrieve) | **GET** /attachments/meta/post | 
*AttachmentsApi* | [**attachments_retrieve**](docs/AttachmentsApi.md#attachments_retrieve) | **GET** /attachments/{id} | 
*AvailableActionsApi* | [**available_actions_retrieve**](docs/AvailableActionsApi.md#available_actions_retrieve) | **GET** /available-actions | 
*CollectionsApi* | [**collections_list**](docs/CollectionsApi.md#collections_list) | **GET** /collections | 
*CollectionsApi* | [**collections_retrieve**](docs/CollectionsApi.md#collections_retrieve) | **GET** /collections/{id} | 
*CommentsApi* | [**comments_create**](docs/CommentsApi.md#comments_create) | **POST** /comments | 
*CommentsApi* | [**comments_list**](docs/CommentsApi.md#comments_list) | **GET** /comments | 
*CommentsApi* | [**comments_meta_post_retrieve**](docs/CommentsApi.md#comments_meta_post_retrieve) | **GET** /comments/meta/post | 
*CommentsApi* | [**comments_retrieve**](docs/CommentsApi.md#comments_retrieve) | **GET** /comments/{id} | 
*ContactsApi* | [**contacts_list**](docs/ContactsApi.md#contacts_list) | **GET** /contacts | 
*ContactsApi* | [**contacts_retrieve**](docs/ContactsApi.md#contacts_retrieve) | **GET** /contacts/{id} | 
*DeleteAccountApi* | [**delete_account_create**](docs/DeleteAccountApi.md#delete_account_create) | **POST** /delete-account | 
*ForceResyncApi* | [**sync_status_resync_create**](docs/ForceResyncApi.md#sync_status_resync_create) | **POST** /sync-status/resync | 
*GenerateKeyApi* | [**generate_key_create**](docs/GenerateKeyApi.md#generate_key_create) | **POST** /generate-key | 
*IssuesApi* | [**issues_list**](docs/IssuesApi.md#issues_list) | **GET** /issues | 
*IssuesApi* | [**issues_retrieve**](docs/IssuesApi.md#issues_retrieve) | **GET** /issues/{id} | 
*LinkTokenApi* | [**link_token_create**](docs/LinkTokenApi.md#link_token_create) | **POST** /link-token | 
*LinkedAccountsApi* | [**linked_accounts_list**](docs/LinkedAccountsApi.md#linked_accounts_list) | **GET** /linked-accounts | 
*PassthroughApi* | [**passthrough_create**](docs/PassthroughApi.md#passthrough_create) | **POST** /passthrough | 
*ProjectsApi* | [**projects_list**](docs/ProjectsApi.md#projects_list) | **GET** /projects | 
*ProjectsApi* | [**projects_retrieve**](docs/ProjectsApi.md#projects_retrieve) | **GET** /projects/{id} | 
*ProjectsApi* | [**projects_users_list**](docs/ProjectsApi.md#projects_users_list) | **GET** /projects/{parent_id}/users | 
*RegenerateKeyApi* | [**regenerate_key_create**](docs/RegenerateKeyApi.md#regenerate_key_create) | **POST** /regenerate-key | 
*SelectiveSyncApi* | [**selective_sync_configurations_list**](docs/SelectiveSyncApi.md#selective_sync_configurations_list) | **GET** /selective-sync/configurations | 
*SelectiveSyncApi* | [**selective_sync_configurations_update**](docs/SelectiveSyncApi.md#selective_sync_configurations_update) | **PUT** /selective-sync/configurations | 
*SelectiveSyncApi* | [**selective_sync_meta_list**](docs/SelectiveSyncApi.md#selective_sync_meta_list) | **GET** /selective-sync/meta | 
*SyncStatusApi* | [**sync_status_list**](docs/SyncStatusApi.md#sync_status_list) | **GET** /sync-status | 
*TagsApi* | [**tags_list**](docs/TagsApi.md#tags_list) | **GET** /tags | 
*TagsApi* | [**tags_retrieve**](docs/TagsApi.md#tags_retrieve) | **GET** /tags/{id} | 
*TeamsApi* | [**teams_list**](docs/TeamsApi.md#teams_list) | **GET** /teams | 
*TeamsApi* | [**teams_retrieve**](docs/TeamsApi.md#teams_retrieve) | **GET** /teams/{id} | 
*TicketsApi* | [**tickets_collaborators_list**](docs/TicketsApi.md#tickets_collaborators_list) | **GET** /tickets/{parent_id}/collaborators | 
*TicketsApi* | [**tickets_create**](docs/TicketsApi.md#tickets_create) | **POST** /tickets | 
*TicketsApi* | [**tickets_list**](docs/TicketsApi.md#tickets_list) | **GET** /tickets | 
*TicketsApi* | [**tickets_meta_patch_retrieve**](docs/TicketsApi.md#tickets_meta_patch_retrieve) | **GET** /tickets/meta/patch/{id} | 
*TicketsApi* | [**tickets_meta_post_retrieve**](docs/TicketsApi.md#tickets_meta_post_retrieve) | **GET** /tickets/meta/post | 
*TicketsApi* | [**tickets_partial_update**](docs/TicketsApi.md#tickets_partial_update) | **PATCH** /tickets/{id} | 
*TicketsApi* | [**tickets_retrieve**](docs/TicketsApi.md#tickets_retrieve) | **GET** /tickets/{id} | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /users | 
*UsersApi* | [**users_retrieve**](docs/UsersApi.md#users_retrieve) | **GET** /users/{id} | 
*WebhookReceiversApi* | [**webhook_receivers_create**](docs/WebhookReceiversApi.md#webhook_receivers_create) | **POST** /webhook-receivers | 
*WebhookReceiversApi* | [**webhook_receivers_list**](docs/WebhookReceiversApi.md#webhook_receivers_list) | **GET** /webhook-receivers | 


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountDetails](docs/AccountDetails.md)
 - [AccountDetailsAndActions](docs/AccountDetailsAndActions.md)
 - [AccountDetailsAndActionsIntegration](docs/AccountDetailsAndActionsIntegration.md)
 - [AccountDetailsAndActionsStatusEnum](docs/AccountDetailsAndActionsStatusEnum.md)
 - [AccountIntegration](docs/AccountIntegration.md)
 - [AccountToken](docs/AccountToken.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentRequest](docs/AttachmentRequest.md)
 - [AvailableActions](docs/AvailableActions.md)
 - [CategoriesEnum](docs/CategoriesEnum.md)
 - [CategoryEnum](docs/CategoryEnum.md)
 - [Collection](docs/Collection.md)
 - [CollectionTypeEnum](docs/CollectionTypeEnum.md)
 - [Comment](docs/Comment.md)
 - [CommentEndpointRequest](docs/CommentEndpointRequest.md)
 - [CommentRequest](docs/CommentRequest.md)
 - [CommentResponse](docs/CommentResponse.md)
 - [ConditionSchema](docs/ConditionSchema.md)
 - [ConditionTypeEnum](docs/ConditionTypeEnum.md)
 - [Contact](docs/Contact.md)
 - [DataPassthroughRequest](docs/DataPassthroughRequest.md)
 - [DebugModeLog](docs/DebugModeLog.md)
 - [DebugModelLogSummary](docs/DebugModelLogSummary.md)
 - [EncodingEnum](docs/EncodingEnum.md)
 - [EndUserDetailsRequest](docs/EndUserDetailsRequest.md)
 - [ErrorValidationProblem](docs/ErrorValidationProblem.md)
 - [GenerateRemoteKeyRequest](docs/GenerateRemoteKeyRequest.md)
 - [Issue](docs/Issue.md)
 - [IssueStatusEnum](docs/IssueStatusEnum.md)
 - [LinkToken](docs/LinkToken.md)
 - [LinkedAccountCondition](docs/LinkedAccountCondition.md)
 - [LinkedAccountConditionRequest](docs/LinkedAccountConditionRequest.md)
 - [LinkedAccountSelectiveSyncConfiguration](docs/LinkedAccountSelectiveSyncConfiguration.md)
 - [LinkedAccountSelectiveSyncConfigurationListRequest](docs/LinkedAccountSelectiveSyncConfigurationListRequest.md)
 - [LinkedAccountSelectiveSyncConfigurationRequest](docs/LinkedAccountSelectiveSyncConfigurationRequest.md)
 - [LinkedAccountStatus](docs/LinkedAccountStatus.md)
 - [MetaResponse](docs/MetaResponse.md)
 - [MethodEnum](docs/MethodEnum.md)
 - [ModelOperation](docs/ModelOperation.md)
 - [MultipartFormFieldRequest](docs/MultipartFormFieldRequest.md)
 - [OperatorSchema](docs/OperatorSchema.md)
 - [PaginatedAccountDetailsAndActionsList](docs/PaginatedAccountDetailsAndActionsList.md)
 - [PaginatedAccountList](docs/PaginatedAccountList.md)
 - [PaginatedAttachmentList](docs/PaginatedAttachmentList.md)
 - [PaginatedCollectionList](docs/PaginatedCollectionList.md)
 - [PaginatedCommentList](docs/PaginatedCommentList.md)
 - [PaginatedConditionSchemaList](docs/PaginatedConditionSchemaList.md)
 - [PaginatedContactList](docs/PaginatedContactList.md)
 - [PaginatedIssueList](docs/PaginatedIssueList.md)
 - [PaginatedProjectList](docs/PaginatedProjectList.md)
 - [PaginatedSyncStatusList](docs/PaginatedSyncStatusList.md)
 - [PaginatedTagList](docs/PaginatedTagList.md)
 - [PaginatedTeamList](docs/PaginatedTeamList.md)
 - [PaginatedTicketList](docs/PaginatedTicketList.md)
 - [PaginatedUserList](docs/PaginatedUserList.md)
 - [PatchedTicketEndpointRequest](docs/PatchedTicketEndpointRequest.md)
 - [PatchedTicketRequest](docs/PatchedTicketRequest.md)
 - [PriorityEnum](docs/PriorityEnum.md)
 - [Project](docs/Project.md)
 - [RemoteData](docs/RemoteData.md)
 - [RemoteKey](docs/RemoteKey.md)
 - [RemoteKeyForRegenerationRequest](docs/RemoteKeyForRegenerationRequest.md)
 - [RemoteResponse](docs/RemoteResponse.md)
 - [RequestFormatEnum](docs/RequestFormatEnum.md)
 - [ResponseTypeEnum](docs/ResponseTypeEnum.md)
 - [SelectiveSyncConfigurationsUsageEnum](docs/SelectiveSyncConfigurationsUsageEnum.md)
 - [SyncStatus](docs/SyncStatus.md)
 - [SyncStatusStatusEnum](docs/SyncStatusStatusEnum.md)
 - [Tag](docs/Tag.md)
 - [Team](docs/Team.md)
 - [Ticket](docs/Ticket.md)
 - [TicketEndpointRequest](docs/TicketEndpointRequest.md)
 - [TicketRequest](docs/TicketRequest.md)
 - [TicketResponse](docs/TicketResponse.md)
 - [TicketStatusEnum](docs/TicketStatusEnum.md)
 - [TicketingAttachmentEndpointRequest](docs/TicketingAttachmentEndpointRequest.md)
 - [TicketingAttachmentResponse](docs/TicketingAttachmentResponse.md)
 - [User](docs/User.md)
 - [ValidationProblemSource](docs/ValidationProblemSource.md)
 - [WarningValidationProblem](docs/WarningValidationProblem.md)
 - [WebhookReceiver](docs/WebhookReceiver.md)
 - [WebhookReceiverRequest](docs/WebhookReceiverRequest.md)


## Documentation For Authorization


## tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@merge.dev


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in MergeTicketingClient.apis and MergeTicketingClient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from MergeTicketingClient.api.default_api import DefaultApi`
- `from MergeTicketingClient.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import MergeTicketingClient
from MergeTicketingClient.apis import *
from MergeTicketingClient.models import *
```

