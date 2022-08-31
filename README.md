# Python Eliona API client
API to access Eliona Smart Building Assistant

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.2.0
- Package version: 1.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/eliona-smart-building-assistant/python-eliona-api-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/eliona-smart-building-assistant/python-eliona-api-client.git`)

Then import the package:
```python
import eliona.api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import eliona.api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import eliona.api_client
from pprint import pprint
from eliona.api_client.api import agents_api
from eliona.api_client.model.agent import Agent
from eliona.api_client.model.agent_device import AgentDevice
from eliona.api_client.model.agent_device_mapping import AgentDeviceMapping
# Defining the host is optional and defaults to http://api.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "http://api.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agents_api.AgentsApi(api_client)
    agent_class = "iosys" # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device

    try:
        # Information about agent device mappings
        api_response = api_instance.get_agent_device_mappings_by_id(agent_class, agent_device_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AgentsApi->get_agent_device_mappings_by_id: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api.eliona.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentsApi* | [**get_agent_device_mappings_by_id**](docs/AgentsApi.md#get_agent_device_mappings_by_id) | **GET** /agent-devices/{agent-class}/{agent-device-id}/mappings | Information about agent device mappings
*AgentsApi* | [**get_agent_devices_by_id**](docs/AgentsApi.md#get_agent_devices_by_id) | **GET** /agents/{agent-class}/{agent-id}/devices | Information about agent devices
*AgentsApi* | [**get_agents**](docs/AgentsApi.md#get_agents) | **GET** /agents | Information about agents
*AgentsApi* | [**get_agents_by_class**](docs/AgentsApi.md#get_agents_by_class) | **GET** /agents/{agent-class} | Information about agents for a specific class
*AgentsApi* | [**put_agent_by_class**](docs/AgentsApi.md#put_agent_by_class) | **PUT** /agents/{agent-class} | Create or update an agent for a specific class
*AgentsApi* | [**put_agent_device_by_id**](docs/AgentsApi.md#put_agent_device_by_id) | **PUT** /agents/{agent-class}/{agent-id}/devices | Create or update an agent device
*AgentsApi* | [**put_agent_device_mapping_by_id**](docs/AgentsApi.md#put_agent_device_mapping_by_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create or update an agent device mapping
*AggregationsApi* | [**delete_aggregation_by_id**](docs/AggregationsApi.md#delete_aggregation_by_id) | **DELETE** /aggregations/{aggregation-id} | Delete an aggregation
*AggregationsApi* | [**get_aggregation_by_id**](docs/AggregationsApi.md#get_aggregation_by_id) | **GET** /aggregations/{aggregation-id} | Information about an aggregation
*AggregationsApi* | [**get_aggregations**](docs/AggregationsApi.md#get_aggregations) | **GET** /aggregations | Information about aggregations
*AggregationsApi* | [**post_aggregation**](docs/AggregationsApi.md#post_aggregation) | **POST** /aggregations | Creates an aggregation
*AlarmRulesApi* | [**get_alarm_rule_by_id**](docs/AlarmRulesApi.md#get_alarm_rule_by_id) | **GET** /alarm-rules/{alarm-rule-id} | Information about an alarm rule
*AlarmRulesApi* | [**get_alarm_rules**](docs/AlarmRulesApi.md#get_alarm_rules) | **GET** /alarm-rules | Information about alarm rules
*AlarmRulesApi* | [**put_alarm_rule**](docs/AlarmRulesApi.md#put_alarm_rule) | **PUT** /alarm-rules | Create or update an alarm rule
*AlarmsApi* | [**get_alarm_by_id**](docs/AlarmsApi.md#get_alarm_by_id) | **GET** /alarms/{alarm-rule-id} | Information about alarm
*AlarmsApi* | [**get_alarm_history_by_id**](docs/AlarmsApi.md#get_alarm_history_by_id) | **GET** /alarms-history/{alarm-rule-id} | Information about alarm history
*AlarmsApi* | [**get_alarms**](docs/AlarmsApi.md#get_alarms) | **GET** /alarms | Information about alarms
*AlarmsApi* | [**get_alarms_history**](docs/AlarmsApi.md#get_alarms_history) | **GET** /alarms-history | Information about alarms history
*AlarmsApi* | [**get_highest_alarms**](docs/AlarmsApi.md#get_highest_alarms) | **GET** /alarms-highest | Information about most prioritized alarms
*AlarmsApi* | [**patch_alarm_by_id**](docs/AlarmsApi.md#patch_alarm_by_id) | **PATCH** /alarms/{alarm-rule-id} | Update alarm
*AppsApi* | [**get_app_by_name**](docs/AppsApi.md#get_app_by_name) | **GET** /apps/{app-name} | Information about an app
*AppsApi* | [**get_patch_by_name**](docs/AppsApi.md#get_patch_by_name) | **GET** /apps/{app-name}/patches/{patch-name} | Information about a patch for an app
*AppsApi* | [**patch_app_by_name**](docs/AppsApi.md#patch_app_by_name) | **PATCH** /apps/{app-name} | Update an app
*AppsApi* | [**patch_patch_by_name**](docs/AppsApi.md#patch_patch_by_name) | **PATCH** /apps/{app-name}/patches/{patch-name} | Updates a patch
*AssetTypesApi* | [**delete_asset_type_by_name**](docs/AssetTypesApi.md#delete_asset_type_by_name) | **DELETE** /asset-types/{asset-type-name} | Delete an asset type
*AssetTypesApi* | [**get_asset_type_by_name**](docs/AssetTypesApi.md#get_asset_type_by_name) | **GET** /asset-types/{asset-type-name} | Information about an asset type
*AssetTypesApi* | [**get_asset_types**](docs/AssetTypesApi.md#get_asset_types) | **GET** /asset-types | List of asset types
*AssetTypesApi* | [**put_asset_type**](docs/AssetTypesApi.md#put_asset_type) | **PUT** /asset-types | Create or update an asset type
*AssetTypesApi* | [**put_asset_type_attribute**](docs/AssetTypesApi.md#put_asset_type_attribute) | **PUT** /asset-types/{asset-type-name}/attributes | Create or update an asset type attribute
*AssetsApi* | [**get_asset_by_id**](docs/AssetsApi.md#get_asset_by_id) | **GET** /assets/{asset-id} | Information about an asset
*AssetsApi* | [**get_assets**](docs/AssetsApi.md#get_assets) | **GET** /assets | Information about assets
*AssetsApi* | [**put_asset**](docs/AssetsApi.md#put_asset) | **PUT** /assets | Create or update an asset
*DashboardsApi* | [**post_dashboard**](docs/DashboardsApi.md#post_dashboard) | **POST** /dashboards | Creates a new dashboard
*DashboardsApi* | [**post_dashboard_widget**](docs/DashboardsApi.md#post_dashboard_widget) | **POST** /dashboards/{dashboard-id}/widgets | Adds widget to dashboard
*DashboardsApi* | [**put_widget_type**](docs/DashboardsApi.md#put_widget_type) | **PUT** /widget-types | Create or update a widget type
*DataApi* | [**get_data**](docs/DataApi.md#get_data) | **GET** /data | Gets all data
*DataApi* | [**get_data_aggregated**](docs/DataApi.md#get_data_aggregated) | **GET** /data-aggregated | Get aggregated data
*DataApi* | [**get_data_trends**](docs/DataApi.md#get_data_trends) | **GET** /data-trends | Get trend of historical data
*DataApi* | [**listen_data**](docs/DataApi.md#listen_data) | **GET** /data-listener | WebSocket connection for asset data changes
*DataApi* | [**put_data**](docs/DataApi.md#put_data) | **PUT** /data | Create or update asset data
*NodesApi* | [**get_node_by_ident**](docs/NodesApi.md#get_node_by_ident) | **GET** /nodes/{node-ident} | Information about a node
*NodesApi* | [**get_nodes**](docs/NodesApi.md#get_nodes) | **GET** /nodes | Information about nodes
*NodesApi* | [**put_node**](docs/NodesApi.md#put_node) | **PUT** /nodes | Create or update a node


## Documentation For Models

 - [Agent](docs/Agent.md)
 - [AgentClass](docs/AgentClass.md)
 - [AgentDevice](docs/AgentDevice.md)
 - [AgentDeviceGeneral](docs/AgentDeviceGeneral.md)
 - [AgentDeviceMapping](docs/AgentDeviceMapping.md)
 - [AgentDeviceMappingGeneral](docs/AgentDeviceMappingGeneral.md)
 - [Aggregation](docs/Aggregation.md)
 - [Alarm](docs/Alarm.md)
 - [AlarmPriority](docs/AlarmPriority.md)
 - [AlarmRule](docs/AlarmRule.md)
 - [App](docs/App.md)
 - [Asset](docs/Asset.md)
 - [AssetType](docs/AssetType.md)
 - [AssetTypeAttribute](docs/AssetTypeAttribute.md)
 - [Dashboard](docs/Dashboard.md)
 - [Data](docs/Data.md)
 - [DataAggregated](docs/DataAggregated.md)
 - [DataSubtype](docs/DataSubtype.md)
 - [IosysAgentDevice](docs/IosysAgentDevice.md)
 - [IosysAgentDeviceMapping](docs/IosysAgentDeviceMapping.md)
 - [IosysAgentDeviceMappingSpecific](docs/IosysAgentDeviceMappingSpecific.md)
 - [IosysAgentDeviceSpecific](docs/IosysAgentDeviceSpecific.md)
 - [MbusAgentDevice](docs/MbusAgentDevice.md)
 - [MbusAgentDeviceMapping](docs/MbusAgentDeviceMapping.md)
 - [MbusAgentDeviceMappingSpecific](docs/MbusAgentDeviceMappingSpecific.md)
 - [MbusAgentDeviceSpecific](docs/MbusAgentDeviceSpecific.md)
 - [Node](docs/Node.md)
 - [Patch](docs/Patch.md)
 - [Translation](docs/Translation.md)
 - [Widget](docs/Widget.md)
 - [WidgetData](docs/WidgetData.md)
 - [WidgetType](docs/WidgetType.md)
 - [WidgetTypeElement](docs/WidgetTypeElement.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in eliona.api_client.apis and eliona.api_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from eliona.api_client.api.default_api import DefaultApi`
- `from eliona.api_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import eliona.api_client
from eliona.api_client.apis import *
from eliona.api_client.models import *
```

