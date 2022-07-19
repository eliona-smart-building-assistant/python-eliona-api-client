# Python Eliona API client
API to access Eliona Smart Building Assistant

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import io.eliona.api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import io.eliona.api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import io.eliona.api_client
from pprint import pprint
from io.eliona.api_client.api import app_api
from io.eliona.api_client.model.app import App
from io.eliona.api_client.model.patch import Patch
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = io.eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)



# Enter a context with an instance of the API client
with io.eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = app_api.AppApi(api_client)
    app_name = "weather" # str | The name of the app
    patch_name = "2.0.0" # str | The name of the patch

    try:
        # Marks a patch in eliona as applied
        api_instance.apply_patch_by_name(app_name, patch_name)
    except io.eliona.api_client.ApiException as e:
        print("Exception when calling AppApi->apply_patch_by_name: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api.eliona.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppApi* | [**apply_patch_by_name**](docs/AppApi.md#apply_patch_by_name) | **PUT** /patch/{app-name}/{patch-name}/apply | Marks a patch in eliona as applied
*AppApi* | [**get_app_by_name**](docs/AppApi.md#get_app_by_name) | **GET** /app/{app-name} | Information about an app
*AppApi* | [**get_patch_by_name**](docs/AppApi.md#get_patch_by_name) | **GET** /patch/{app-name}/{patch-name} | Information about a patch for an app
*AppApi* | [**register_app_by_name**](docs/AppApi.md#register_app_by_name) | **PUT** /app/{app-name}/register | Marks an app in eliona as registered
*AssetApi* | [**get_asset_by_id**](docs/AssetApi.md#get_asset_by_id) | **GET** /asset/{asset-id} | Information about an Asset
*AssetApi* | [**get_asset_children**](docs/AssetApi.md#get_asset_children) | **GET** /asset/{asset-id}/children | Get children for an asset
*AssetApi* | [**get_asset_parents**](docs/AssetApi.md#get_asset_parents) | **GET** /asset/{asset-id}/parents | Get the parents for an asset
*AssetApi* | [**post_asset**](docs/AssetApi.md#post_asset) | **POST** /asset | Create or update an asset
*AssetApi* | [**set_asset_parents**](docs/AssetApi.md#set_asset_parents) | **PUT** /asset/{asset-id}/parents | Set or replace parents for an asset
*AssetTypeApi* | [**get_asset_types**](docs/AssetTypeApi.md#get_asset_types) | **GET** /asset-type | List of asset types
*AssetTypeApi* | [**post_asset_type**](docs/AssetTypeApi.md#post_asset_type) | **POST** /asset-type | Create or update an asset type
*AssetTypeApi* | [**post_asset_type_attribute**](docs/AssetTypeApi.md#post_asset_type_attribute) | **POST** /asset-type-attribute | Create or update an asset type attribute
*DashboardApi* | [**post_dashboard**](docs/DashboardApi.md#post_dashboard) | **POST** /dashboard | Creates a new dashboard
*DashboardApi* | [**post_widget_type**](docs/DashboardApi.md#post_widget_type) | **POST** /widget-type | Adds a new widget type
*DashboardApi* | [**put_dashboard_widget**](docs/DashboardApi.md#put_dashboard_widget) | **PUT** /dashboard/{dashboard-id}/widget | Adds widget to dashboard
*HeapApi* | [**post_heap**](docs/HeapApi.md#post_heap) | **POST** /heap | Create or update heap data


## Documentation For Models

 - [App](docs/App.md)
 - [Asset](docs/Asset.md)
 - [AssetRelation](docs/AssetRelation.md)
 - [AssetType](docs/AssetType.md)
 - [Attribute](docs/Attribute.md)
 - [AttributePipeline](docs/AttributePipeline.md)
 - [Dashboard](docs/Dashboard.md)
 - [Heap](docs/Heap.md)
 - [HeapSubtype](docs/HeapSubtype.md)
 - [Patch](docs/Patch.md)
 - [Translation](docs/Translation.md)
 - [Widget](docs/Widget.md)
 - [WidgetData](docs/WidgetData.md)
 - [WidgetType](docs/WidgetType.md)
 - [WidgetTypeElement](docs/WidgetTypeElement.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in io.eliona.api_client.apis and io.eliona.api_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from io.eliona.api_client.api.default_api import DefaultApi`
- `from io.eliona.api_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import io.eliona.api_client
from io.eliona.api_client.apis import *
from io.eliona.api_client.models import *
```

