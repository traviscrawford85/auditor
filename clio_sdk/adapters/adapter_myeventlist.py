# Adapter for myeventlist
from clio_sdk.models.myeventlist import MyeventlistIn, MyeventlistOut, MyeventlistUpdate, MyeventlistDb
from clio_client.models import my_event_list

def convert_sdk_to_myeventlistout(src: my_event_list) -> MyeventlistOut:
    return MyeventlistOut(**src.dict())

def convert_myeventlistin_to_sdk(src: MyeventlistIn) -> my_event_list:
    return my_event_list(**src.dict())
