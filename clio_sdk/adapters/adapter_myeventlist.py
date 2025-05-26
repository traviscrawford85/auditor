# Adapter for myeventlist
from clio_sdk.models.myeventlist import MyeventlistIn, MyeventlistOut, MyeventlistUpdate, MyeventlistDb
from clio_client.models.my_event_list import MyEventList

def convert_sdk_to_myeventlistout(src: MyEventList) -> MyeventlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return MyeventlistOut(**src.model_dump())

def convert_myeventlistin_to_sdk(src: MyeventlistIn) -> MyEventList:
    """Converts a clio_sdk model to clio_client model."""
    return MyEventList(**src.model_dump())
