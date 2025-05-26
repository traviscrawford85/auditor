# Adapter for myeventbase
from clio_sdk.models.myeventbase import MyeventbaseIn, MyeventbaseOut, MyeventbaseUpdate, MyeventbaseDb
from clio_client.models import my_event

def convert_sdk_to_myeventbaseout(src: my_event) -> MyeventbaseOut:
    return MyeventbaseOut(**src.dict())

def convert_myeventbasein_to_sdk(src: MyeventbaseIn) -> my_event:
    return my_event(**src.dict())
