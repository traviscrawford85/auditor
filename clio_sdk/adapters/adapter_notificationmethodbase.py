# Adapter for notificationmethodbase
from clio_sdk.models.notificationmethodbase import NotificationmethodbaseIn, NotificationmethodbaseOut, NotificationmethodbaseUpdate, NotificationmethodbaseDb
from clio_client.models import notification_method_base

def convert_sdk_to_notificationmethodbaseout(src: notification_method_base) -> NotificationmethodbaseOut:
    return NotificationmethodbaseOut(**src.dict())

def convert_notificationmethodbasein_to_sdk(src: NotificationmethodbaseIn) -> notification_method_base:
    return notification_method_base(**src.dict())
