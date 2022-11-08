# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from eliona.api_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    NODES = "Nodes"
    AGENTS = "Agents"
    ALARMS = "Alarms"
    ALARM_RULES = "Alarm rules"
    APPS = "Apps"
    ASSET_TYPES = "Asset types"
    ASSETS = "Assets"
    AGGREGATIONS = "Aggregations"
    DATA = "Data"
    DASHBOARDS = "Dashboards"
    WIDGETS_TYPES = "Widgets types"
    WIDGETS = "Widgets"
    MESSAGES = "Messages"
    VERSION = "Version"
