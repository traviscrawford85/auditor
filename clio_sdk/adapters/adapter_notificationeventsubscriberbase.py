# Adapter for notificationeventsubscriberbase
from clio_sdk.models.notificationeventsubscriberbase import NotificationeventsubscriberbaseIn, NotificationeventsubscriberbaseOut, NotificationeventsubscriberbaseUpdate, NotificationeventsubscriberbaseDb
from clio_client.models import notification_event_subscriber_base

def convert_sdk_to_notificationeventsubscriberbaseout(src: notification_event_subscriber_base) -> NotificationeventsubscriberbaseOut:
    return NotificationeventsubscriberbaseOut(**src.dict())

def convert_notificationeventsubscriberbasein_to_sdk(src: NotificationeventsubscriberbaseIn) -> notification_event_subscriber_base:
    return notification_event_subscriber_base(**src.dict())
