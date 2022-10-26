import typing_extensions

from eliona.api_client.paths import PathValues
from eliona.api_client.apis.paths.version import Version
from eliona.api_client.apis.paths.apps_app_name import AppsAppName
from eliona.api_client.apis.paths.apps_app_name_patches_patch_name import AppsAppNamePatchesPatchName
from eliona.api_client.apis.paths.asset_types import AssetTypes
from eliona.api_client.apis.paths.asset_types_asset_type_name import AssetTypesAssetTypeName
from eliona.api_client.apis.paths.asset_types_asset_type_name_attributes import AssetTypesAssetTypeNameAttributes
from eliona.api_client.apis.paths.assets import Assets
from eliona.api_client.apis.paths.assets_asset_id import AssetsAssetId
from eliona.api_client.apis.paths.data import Data
from eliona.api_client.apis.paths.data_trends import DataTrends
from eliona.api_client.apis.paths.data_listener import DataListener
from eliona.api_client.apis.paths.data_aggregated import DataAggregated
from eliona.api_client.apis.paths.aggregations import Aggregations
from eliona.api_client.apis.paths.aggregations_aggregation_id import AggregationsAggregationId
from eliona.api_client.apis.paths.widget_types import WidgetTypes
from eliona.api_client.apis.paths.widget_types_widget_type_name import WidgetTypesWidgetTypeName
from eliona.api_client.apis.paths.dashboards import Dashboards
from eliona.api_client.apis.paths.dashboards_dashboard_id import DashboardsDashboardId
from eliona.api_client.apis.paths.dashboards_dashboard_id_widgets import DashboardsDashboardIdWidgets
from eliona.api_client.apis.paths.alarm_rules import AlarmRules
from eliona.api_client.apis.paths.alarm_rules_alarm_rule_id import AlarmRulesAlarmRuleId
from eliona.api_client.apis.paths.alarms import Alarms
from eliona.api_client.apis.paths.alarms_alarm_rule_id import AlarmsAlarmRuleId
from eliona.api_client.apis.paths.alarms_history import AlarmsHistory
from eliona.api_client.apis.paths.alarms_history_alarm_rule_id import AlarmsHistoryAlarmRuleId
from eliona.api_client.apis.paths.alarms_highest import AlarmsHighest
from eliona.api_client.apis.paths.nodes import Nodes
from eliona.api_client.apis.paths.nodes_node_ident import NodesNodeIdent
from eliona.api_client.apis.paths.agents import Agents
from eliona.api_client.apis.paths.agents_agent_class import AgentsAgentClass
from eliona.api_client.apis.paths.agents_agent_class_agent_id_devices import AgentsAgentClassAgentIdDevices
from eliona.api_client.apis.paths.agent_devices_agent_class_agent_device_id_mappings import AgentDevicesAgentClassAgentDeviceIdMappings

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.VERSION: Version,
        PathValues.APPS_APPNAME: AppsAppName,
        PathValues.APPS_APPNAME_PATCHES_PATCHNAME: AppsAppNamePatchesPatchName,
        PathValues.ASSETTYPES: AssetTypes,
        PathValues.ASSETTYPES_ASSETTYPENAME: AssetTypesAssetTypeName,
        PathValues.ASSETTYPES_ASSETTYPENAME_ATTRIBUTES: AssetTypesAssetTypeNameAttributes,
        PathValues.ASSETS: Assets,
        PathValues.ASSETS_ASSETID: AssetsAssetId,
        PathValues.DATA: Data,
        PathValues.DATATRENDS: DataTrends,
        PathValues.DATALISTENER: DataListener,
        PathValues.DATAAGGREGATED: DataAggregated,
        PathValues.AGGREGATIONS: Aggregations,
        PathValues.AGGREGATIONS_AGGREGATIONID: AggregationsAggregationId,
        PathValues.WIDGETTYPES: WidgetTypes,
        PathValues.WIDGETTYPES_WIDGETTYPENAME: WidgetTypesWidgetTypeName,
        PathValues.DASHBOARDS: Dashboards,
        PathValues.DASHBOARDS_DASHBOARDID: DashboardsDashboardId,
        PathValues.DASHBOARDS_DASHBOARDID_WIDGETS: DashboardsDashboardIdWidgets,
        PathValues.ALARMRULES: AlarmRules,
        PathValues.ALARMRULES_ALARMRULEID: AlarmRulesAlarmRuleId,
        PathValues.ALARMS: Alarms,
        PathValues.ALARMS_ALARMRULEID: AlarmsAlarmRuleId,
        PathValues.ALARMSHISTORY: AlarmsHistory,
        PathValues.ALARMSHISTORY_ALARMRULEID: AlarmsHistoryAlarmRuleId,
        PathValues.ALARMSHIGHEST: AlarmsHighest,
        PathValues.NODES: Nodes,
        PathValues.NODES_NODEIDENT: NodesNodeIdent,
        PathValues.AGENTS: Agents,
        PathValues.AGENTS_AGENTCLASS: AgentsAgentClass,
        PathValues.AGENTS_AGENTCLASS_AGENTID_DEVICES: AgentsAgentClassAgentIdDevices,
        PathValues.AGENTDEVICES_AGENTCLASS_AGENTDEVICEID_MAPPINGS: AgentDevicesAgentClassAgentDeviceIdMappings,
    }
)

path_to_api = PathToApi(
    {
        PathValues.VERSION: Version,
        PathValues.APPS_APPNAME: AppsAppName,
        PathValues.APPS_APPNAME_PATCHES_PATCHNAME: AppsAppNamePatchesPatchName,
        PathValues.ASSETTYPES: AssetTypes,
        PathValues.ASSETTYPES_ASSETTYPENAME: AssetTypesAssetTypeName,
        PathValues.ASSETTYPES_ASSETTYPENAME_ATTRIBUTES: AssetTypesAssetTypeNameAttributes,
        PathValues.ASSETS: Assets,
        PathValues.ASSETS_ASSETID: AssetsAssetId,
        PathValues.DATA: Data,
        PathValues.DATATRENDS: DataTrends,
        PathValues.DATALISTENER: DataListener,
        PathValues.DATAAGGREGATED: DataAggregated,
        PathValues.AGGREGATIONS: Aggregations,
        PathValues.AGGREGATIONS_AGGREGATIONID: AggregationsAggregationId,
        PathValues.WIDGETTYPES: WidgetTypes,
        PathValues.WIDGETTYPES_WIDGETTYPENAME: WidgetTypesWidgetTypeName,
        PathValues.DASHBOARDS: Dashboards,
        PathValues.DASHBOARDS_DASHBOARDID: DashboardsDashboardId,
        PathValues.DASHBOARDS_DASHBOARDID_WIDGETS: DashboardsDashboardIdWidgets,
        PathValues.ALARMRULES: AlarmRules,
        PathValues.ALARMRULES_ALARMRULEID: AlarmRulesAlarmRuleId,
        PathValues.ALARMS: Alarms,
        PathValues.ALARMS_ALARMRULEID: AlarmsAlarmRuleId,
        PathValues.ALARMSHISTORY: AlarmsHistory,
        PathValues.ALARMSHISTORY_ALARMRULEID: AlarmsHistoryAlarmRuleId,
        PathValues.ALARMSHIGHEST: AlarmsHighest,
        PathValues.NODES: Nodes,
        PathValues.NODES_NODEIDENT: NodesNodeIdent,
        PathValues.AGENTS: Agents,
        PathValues.AGENTS_AGENTCLASS: AgentsAgentClass,
        PathValues.AGENTS_AGENTCLASS_AGENTID_DEVICES: AgentsAgentClassAgentIdDevices,
        PathValues.AGENTDEVICES_AGENTCLASS_AGENTDEVICEID_MAPPINGS: AgentDevicesAgentClassAgentDeviceIdMappings,
    }
)
