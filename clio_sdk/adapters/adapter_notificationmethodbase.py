# Adapter for notificationmethodbase
from clio_sdk.models.notificationmethodbase import NotificationmethodBaseIn, NotificationmethodbaseOut, NotificationmethodbaseUpdate, NotificationmethodbaseDb
from clio_client.models.notification_method_base import NotificationMethodBase

def convert_sdk_to_notificationmethodbaseout(src: NotificationMethodBase) -> NotificationmethodbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return NotificationmethodbaseOut(**src.model_dump())

def convert_notificationmethodbasein_to_sdk(src: NotificationmethodBaseIn) -> NotificationMethodBase:
    """Converts a clio_sdk model to clio_client model."""
    return NotificationMethodBase(**src.model_dump())
