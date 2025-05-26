from typing import Literal, cast

TaskTemplateupdateJsonBodyDataReminderTemplatesItemNotificationType = Literal["Email", "Popup"]

TASK_TEMPLATEUPDATE_JSON_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    TaskTemplateupdateJsonBodyDataReminderTemplatesItemNotificationType
] = {
    "Email",
    "Popup",
}


def check_task_templateupdate_json_body_data_reminder_templates_item_notification_type(
    value: str,
) -> TaskTemplateupdateJsonBodyDataReminderTemplatesItemNotificationType:
    if value in TASK_TEMPLATEUPDATE_JSON_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES:
        return cast(TaskTemplateupdateJsonBodyDataReminderTemplatesItemNotificationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_JSON_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
