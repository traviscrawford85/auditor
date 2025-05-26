from typing import Literal, cast

TaskTemplateupdateFilesBodyDataReminderTemplatesItemNotificationType = Literal["Email", "Popup"]

TASK_TEMPLATEUPDATE_FILES_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    TaskTemplateupdateFilesBodyDataReminderTemplatesItemNotificationType
] = {
    "Email",
    "Popup",
}


def check_task_templateupdate_files_body_data_reminder_templates_item_notification_type(
    value: str,
) -> TaskTemplateupdateFilesBodyDataReminderTemplatesItemNotificationType:
    if value in TASK_TEMPLATEUPDATE_FILES_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES:
        return cast(TaskTemplateupdateFilesBodyDataReminderTemplatesItemNotificationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_FILES_BODY_DATA_REMINDER_TEMPLATES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
