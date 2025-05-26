from typing import Literal, cast

TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType = Literal["Email", "Popup"]

TASK_TEMPLATECREATE_JSON_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType
] = {
    "Email",
    "Popup",
}


def check_task_templatecreate_json_body_data_reminder_templates_item_notification_type(
    value: str,
) -> TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType:
    if value in TASK_TEMPLATECREATE_JSON_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES:
        return cast(TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_JSON_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
