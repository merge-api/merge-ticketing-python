# MergeTicketingClient.CommentsApi

All URIs are relative to *https://api.merge.dev/api/ticketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_create**](CommentsApi.md#comments_create) | **POST** /comments | 
[**comments_list**](CommentsApi.md#comments_list) | **GET** /comments | 
[**comments_meta_post_retrieve**](CommentsApi.md#comments_meta_post_retrieve) | **GET** /comments/meta/post | 
[**comments_retrieve**](CommentsApi.md#comments_retrieve) | **GET** /comments/{id} | 


# **comments_create**
> CommentResponse comments_create(x_account_token, comment_endpoint_request)



Creates a `Comment` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeTicketingClient
from MergeTicketingClient.api import comments_api
from MergeTicketingClient.model.comment_response import CommentResponse
from MergeTicketingClient.model.comment_endpoint_request import CommentEndpointRequest
from pprint import pprint
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
    api_instance = comments_api.CommentsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    comment_endpoint_request = CommentEndpointRequest(
        model=CommentRequest(
            remote_id="19202938",
            user="17a54124-287f-494d-965e-3c5b330c9a68",
            contact="dde3fb16-b8eb-483d-81c4-b78100816f15",
            body="When will these integrations be done? You all should use Merge.",
            html_body="When will these integrations be done? You all should use <b>Merge<b>.",
            ticket="fb8c55b6-1cb8-4b4c-9fb6-17924231619d",
            is_private=True,
            remote_created_at=dateutil_parser('1990-11-10T00:00:00Z'),
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # CommentEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.comments_create(x_account_token, comment_endpoint_request)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling CommentsApi->comments_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.comments_create(x_account_token, comment_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling CommentsApi->comments_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **comment_endpoint_request** | [**CommentEndpointRequest**](CommentEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**CommentResponse**](CommentResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_list**
> PaginatedCommentList comments_list(x_account_token)



Returns a list of `Comment` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeTicketingClient
from MergeTicketingClient.api import comments_api
from MergeTicketingClient.model.paginated_comment_list import PaginatedCommentList
from pprint import pprint
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
    api_instance = comments_api.CommentsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "user,contact,ticket" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    ticket_id = "ticket_id_example" # str | If provided, will only return comments for this ticket. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.comments_list(x_account_token)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling CommentsApi->comments_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.comments_list(x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, ticket_id=ticket_id)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling CommentsApi->comments_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **ticket_id** | **str**| If provided, will only return comments for this ticket. | [optional]

### Return type

[**PaginatedCommentList**](PaginatedCommentList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_meta_post_retrieve**
> MetaResponse comments_meta_post_retrieve(x_account_token)



Returns metadata for `Comment` POSTs.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeTicketingClient
from MergeTicketingClient.api import comments_api
from MergeTicketingClient.model.meta_response import MetaResponse
from pprint import pprint
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
    api_instance = comments_api.CommentsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.comments_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling CommentsApi->comments_meta_post_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |

### Return type

[**MetaResponse**](MetaResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_retrieve**
> Comment comments_retrieve(x_account_token, id)



Returns a `Comment` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeTicketingClient
from MergeTicketingClient.api import comments_api
from MergeTicketingClient.model.comment import Comment
from pprint import pprint
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
    api_instance = comments_api.CommentsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "user,contact,ticket" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.comments_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling CommentsApi->comments_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.comments_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeTicketingClient.ApiException as e:
        print("Exception when calling CommentsApi->comments_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

