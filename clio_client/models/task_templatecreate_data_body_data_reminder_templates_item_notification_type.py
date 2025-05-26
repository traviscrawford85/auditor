from typing import Literal, cast

TaskTemplatecreateDataBodyDataReminderTemplatesItemNotificationType = Literal["Email", "Popup"]

TASK_TEMPLATECREATE_DATA_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    TaskTemplatecreateDataBodyDataReminderTemplatesItemNotificationType
] = {
    "Email",
    "Popup",
}


def check_task_templatecreate_data_body_data_reminder_templates_item_notification_type(
    value: str,
) -> TaskTemplatecreateDataBodyDataReminderTemplatesItemNotificationType:
    if value in TASK_TEMPLATECREATE_DATA_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES:
        return cast(TaskTemplatecreateDataBodyDataReminderTemplatesItemNotificationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_DATA_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
