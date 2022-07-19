# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from io.eliona.api-client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from io.eliona.api-client.model.app import App
from io.eliona.api-client.model.asset import Asset
from io.eliona.api-client.model.asset_relation import AssetRelation
from io.eliona.api-client.model.asset_type import AssetType
from io.eliona.api-client.model.attribute import Attribute
from io.eliona.api-client.model.attribute_pipeline import AttributePipeline
from io.eliona.api-client.model.dashboard import Dashboard
from io.eliona.api-client.model.heap import Heap
from io.eliona.api-client.model.heap_subtype import HeapSubtype
from io.eliona.api-client.model.patch import Patch
from io.eliona.api-client.model.translation import Translation
from io.eliona.api-client.model.widget import Widget
from io.eliona.api-client.model.widget_data import WidgetData
from io.eliona.api-client.model.widget_type import WidgetType
from io.eliona.api-client.model.widget_type_element import WidgetTypeElement
