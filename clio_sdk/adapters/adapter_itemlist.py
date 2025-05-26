# Adapter for itemlist
from clio_sdk.models.itemlist import ItemlistIn, ItemlistOut, ItemlistUpdate, ItemlistDb
from clio_client.models.item_list import ItemList

def convert_sdk_to_itemlistout(src: ItemList) -> ItemlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ItemlistOut(**src.model_dump())

def convert_itemlistin_to_sdk(src: ItemlistIn) -> ItemList:
    """Converts a clio_sdk model to clio_client model."""
    return ItemList(**src.model_dump())
