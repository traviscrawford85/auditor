from typing import Literal, cast

ReminderTemplateBaseNotificationType = Literal["Email", "Popup"]

REMINDER_TEMPLATE_BASE_NOTIFICATION_TYPE_VALUES: set[ReminderTemplateBaseNotificationType] = {
    "Email",
    "Popup",
}


def check_reminder_template_base_notification_type(value: str) -> ReminderTemplateBaseNotificationType:
    if value in REMINDER_TEMPLATE_BASE_NOTIFICATION_TYPE_VALUES:
        return cast(ReminderTemplateBaseNotificationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REMINDER_TEMPLATE_BASE_NOTIFICATION_TYPE_VALUES!r}")
