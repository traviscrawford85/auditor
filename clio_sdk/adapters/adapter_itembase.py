# Adapter for itembase
from clio_sdk.models.itembase import ItemBaseIn, ItembaseOut, ItembaseUpdate, ItembaseDb
from clio_client.models.item import Item

def convert_sdk_to_itembaseout(src: Item) -> ItembaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ItembaseOut(**src.model_dump())

def convert_itembasein_to_sdk(src: ItemBaseIn) -> Item:
    """Converts a clio_sdk model to clio_client model."""
    return Item(**src.model_dump())
