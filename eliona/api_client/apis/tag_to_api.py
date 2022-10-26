import typing_extensions

from eliona.api_client.apis.tags import TagValues
from eliona.api_client.apis.tags.nodes_api import NodesApi
from eliona.api_client.apis.tags.agents_api import AgentsApi
from eliona.api_client.apis.tags.alarms_api import AlarmsApi
from eliona.api_client.apis.tags.alarm_rules_api import AlarmRulesApi
from eliona.api_client.apis.tags.apps_api import AppsApi
from eliona.api_client.apis.tags.asset_types_api import AssetTypesApi
from eliona.api_client.apis.tags.assets_api import AssetsApi
from eliona.api_client.apis.tags.aggregations_api import AggregationsApi
from eliona.api_client.apis.tags.data_api import DataApi
from eliona.api_client.apis.tags.dashboards_api import DashboardsApi
from eliona.api_client.apis.tags.widgets_types_api import WidgetsTypesApi
from eliona.api_client.apis.tags.widgets_api import WidgetsApi
from eliona.api_client.apis.tags.version_api import VersionApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.NODES: NodesApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.ALARMS: AlarmsApi,
        TagValues.ALARM_RULES: AlarmRulesApi,
        TagValues.APPS: AppsApi,
        TagValues.ASSET_TYPES: AssetTypesApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.AGGREGATIONS: AggregationsApi,
        TagValues.DATA: DataApi,
        TagValues.DASHBOARDS: DashboardsApi,
        TagValues.WIDGETS_TYPES: WidgetsTypesApi,
        TagValues.WIDGETS: WidgetsApi,
        TagValues.VERSION: VersionApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.NODES: NodesApi,
        TagValues.AGENTS: AgentsApi,
        TagValues.ALARMS: AlarmsApi,
        TagValues.ALARM_RULES: AlarmRulesApi,
        TagValues.APPS: AppsApi,
        TagValues.ASSET_TYPES: AssetTypesApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.AGGREGATIONS: AggregationsApi,
        TagValues.DATA: DataApi,
        TagValues.DASHBOARDS: DashboardsApi,
        TagValues.WIDGETS_TYPES: WidgetsTypesApi,
        TagValues.WIDGETS: WidgetsApi,
        TagValues.VERSION: VersionApi,
    }
)
