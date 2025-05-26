# Adapter for myeventshow
from clio_sdk.models.myeventshow import MyeventshowIn, MyeventshowOut, MyeventshowUpdate, MyeventshowDb
from clio_client.models import my_event_show

def convert_sdk_to_myeventshowout(src: my_event_show) -> MyeventshowOut:
    return MyeventshowOut(**src.dict())

def convert_myeventshowin_to_sdk(src: MyeventshowIn) -> my_event_show:
    return my_event_show(**src.dict())
