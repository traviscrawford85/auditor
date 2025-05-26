from typing import Literal, cast

NotificationMethodBaseType = Literal["Email", "Popup", "SMS"]

NOTIFICATION_METHOD_BASE_TYPE_VALUES: set[NotificationMethodBaseType] = {
    "Email",
    "Popup",
    "SMS",
}


def check_notification_method_base_type(value: str) -> NotificationMethodBaseType:
    if value in NOTIFICATION_METHOD_BASE_TYPE_VALUES:
        return cast(NotificationMethodBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_METHOD_BASE_TYPE_VALUES!r}")
