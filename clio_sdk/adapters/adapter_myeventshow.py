# Adapter for myeventshow
from clio_sdk.models.myeventshow import MyeventshowIn, MyeventshowOut, MyeventshowUpdate, MyeventshowDb
from clio_client.models.my_event_show import MyEventShow

def convert_sdk_to_myeventshowout(src: MyEventShow) -> MyeventshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return MyeventshowOut(**src.model_dump())

def convert_myeventshowin_to_sdk(src: MyeventshowIn) -> MyEventShow:
    """Converts a clio_sdk model to clio_client model."""
    return MyEventShow(**src.model_dump())
