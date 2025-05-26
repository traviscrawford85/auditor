from typing import Literal, cast

TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType = Literal["Email", "Popup"]

TASK_TEMPLATEUPDATE_DATA_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType
] = {
    "Email",
    "Popup",
}


def check_task_templateupdate_data_body_data_reminder_templates_item_notification_type(
    value: str,
) -> TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType:
    if value in TASK_TEMPLATEUPDATE_DATA_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES:
        return cast(TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_DATA_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
