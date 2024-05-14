# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from eliona.api_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from eliona.api_client.model.agent import Agent
from eliona.api_client.model.agent_class import AgentClass
from eliona.api_client.model.agent_device import AgentDevice
from eliona.api_client.model.agent_device_general import AgentDeviceGeneral
from eliona.api_client.model.agent_device_mapping import AgentDeviceMapping
from eliona.api_client.model.agent_device_mapping_general import AgentDeviceMappingGeneral
from eliona.api_client.model.aggregation import Aggregation
from eliona.api_client.model.alarm import Alarm
from eliona.api_client.model.alarm_listen import AlarmListen
from eliona.api_client.model.alarm_listen_all_of import AlarmListenAllOf
from eliona.api_client.model.alarm_priority import AlarmPriority
from eliona.api_client.model.alarm_rule import AlarmRule
from eliona.api_client.model.app import App
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.asset_dry_run import AssetDryRun
from eliona.api_client.model.asset_dry_run1 import AssetDryRun1
from eliona.api_client.model.asset_identify_by import AssetIdentifyBy
from eliona.api_client.model.asset_listen import AssetListen
from eliona.api_client.model.asset_listen_all_of import AssetListenAllOf
from eliona.api_client.model.asset_type import AssetType
from eliona.api_client.model.asset_type_attribute import AssetTypeAttribute
from eliona.api_client.model.attachment import Attachment
from eliona.api_client.model.attribute_display import AttributeDisplay
from eliona.api_client.model.calculation_rule import CalculationRule
from eliona.api_client.model.dashboard import Dashboard
from eliona.api_client.model.data import Data
from eliona.api_client.model.data_aggregated import DataAggregated
from eliona.api_client.model.data_listen import DataListen
from eliona.api_client.model.data_listen_all_of import DataListenAllOf
from eliona.api_client.model.data_subtype import DataSubtype
from eliona.api_client.model.dry_run_general import DryRunGeneral
from eliona.api_client.model.iosys_agent_device import IosysAgentDevice
from eliona.api_client.model.iosys_agent_device1 import IosysAgentDevice1
from eliona.api_client.model.iosys_agent_device_mapping import IosysAgentDeviceMapping
from eliona.api_client.model.iosys_agent_device_mapping1 import IosysAgentDeviceMapping1
from eliona.api_client.model.mbus_agent_device import MbusAgentDevice
from eliona.api_client.model.mbus_agent_device1 import MbusAgentDevice1
from eliona.api_client.model.mbus_agent_device_mapping import MbusAgentDeviceMapping
from eliona.api_client.model.mbus_agent_device_mapping1 import MbusAgentDeviceMapping1
from eliona.api_client.model.message import Message
from eliona.api_client.model.message_receipt import MessageReceipt
from eliona.api_client.model.node import Node
from eliona.api_client.model.notification import Notification
from eliona.api_client.model.patch import Patch
from eliona.api_client.model.project import Project
from eliona.api_client.model.tag import Tag
from eliona.api_client.model.translation import Translation
from eliona.api_client.model.user import User
from eliona.api_client.model.widget import Widget
from eliona.api_client.model.widget_data import WidgetData
from eliona.api_client.model.widget_type import WidgetType
from eliona.api_client.model.widget_type_element import WidgetTypeElement
