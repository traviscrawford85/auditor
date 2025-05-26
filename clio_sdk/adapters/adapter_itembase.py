# Adapter for itembase
from clio_sdk.models.itembase import ItembaseIn, ItembaseOut, ItembaseUpdate, ItembaseDb
from clio_client.models import item

def convert_sdk_to_itembaseout(src: item) -> ItembaseOut:
    return ItembaseOut(**src.dict())

def convert_itembasein_to_sdk(src: ItembaseIn) -> item:
    return item(**src.dict())
