from typing import Literal, cast

TaskTemplatecreateFilesBodyDataReminderTemplatesItemNotificationType = Literal["Email", "Popup"]

TASK_TEMPLATECREATE_FILES_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    TaskTemplatecreateFilesBodyDataReminderTemplatesItemNotificationType
] = {
    "Email",
    "Popup",
}


def check_task_templatecreate_files_body_data_reminder_templates_item_notification_type(
    value: str,
) -> TaskTemplatecreateFilesBodyDataReminderTemplatesItemNotificationType:
    if value in TASK_TEMPLATECREATE_FILES_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES:
        return cast(TaskTemplatecreateFilesBodyDataReminderTemplatesItemNotificationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_FILES_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
