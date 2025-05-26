# Adapter for notificationeventsubscriberbase
from clio_sdk.models.notificationeventsubscriberbase import NotificationeventsubscriberBaseIn, NotificationeventsubscriberbaseOut, NotificationeventsubscriberbaseUpdate, NotificationeventsubscriberbaseDb
from clio_client.models.notification_event_subscriber_base import NotificationEventSubscriberBase

def convert_sdk_to_notificationeventsubscriberbaseout(src: NotificationEventSubscriberBase) -> NotificationeventsubscriberbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return NotificationeventsubscriberbaseOut(**src.model_dump())

def convert_notificationeventsubscriberbasein_to_sdk(src: NotificationeventsubscriberBaseIn) -> NotificationEventSubscriberBase:
    """Converts a clio_sdk model to clio_client model."""
    return NotificationEventSubscriberBase(**src.model_dump())
