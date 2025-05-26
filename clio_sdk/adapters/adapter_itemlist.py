# Adapter for itemlist
from clio_sdk.models.itemlist import ItemlistIn, ItemlistOut, ItemlistUpdate, ItemlistDb
from clio_client.models import item_list

def convert_sdk_to_itemlistout(src: item_list) -> ItemlistOut:
    return ItemlistOut(**src.dict())

def convert_itemlistin_to_sdk(src: ItemlistIn) -> item_list:
    return item_list(**src.dict())
