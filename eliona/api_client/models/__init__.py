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
from eliona.api_client.model.alarm import Alarm
from eliona.api_client.model.alarm_priority import AlarmPriority
from eliona.api_client.model.alarm_rule import AlarmRule
from eliona.api_client.model.app import App
from eliona.api_client.model.asset import Asset
from eliona.api_client.model.asset_type import AssetType
from eliona.api_client.model.asset_type_attribute import AssetTypeAttribute
from eliona.api_client.model.dashboard import Dashboard
from eliona.api_client.model.heap import Heap
from eliona.api_client.model.heap_subtype import HeapSubtype
from eliona.api_client.model.iosys_agent_device import IosysAgentDevice
from eliona.api_client.model.iosys_agent_device_mapping import IosysAgentDeviceMapping
from eliona.api_client.model.iosys_agent_device_mapping_specific import IosysAgentDeviceMappingSpecific
from eliona.api_client.model.iosys_agent_device_specific import IosysAgentDeviceSpecific
from eliona.api_client.model.mbus_agent_device import MbusAgentDevice
from eliona.api_client.model.mbus_agent_device_mapping import MbusAgentDeviceMapping
from eliona.api_client.model.mbus_agent_device_mapping_specific import MbusAgentDeviceMappingSpecific
from eliona.api_client.model.mbus_agent_device_specific import MbusAgentDeviceSpecific
from eliona.api_client.model.node import Node
from eliona.api_client.model.patch import Patch
from eliona.api_client.model.pipeline import Pipeline
from eliona.api_client.model.translation import Translation
from eliona.api_client.model.widget import Widget
from eliona.api_client.model.widget_data import WidgetData
from eliona.api_client.model.widget_type import WidgetType
from eliona.api_client.model.widget_type_element import WidgetTypeElement
