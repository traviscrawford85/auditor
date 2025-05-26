from typing import Literal, cast

RemindercreateFilesBodyDataSubjectType = Literal["CalendarEntry", "Task"]

REMINDERCREATE_FILES_BODY_DATA_SUBJECT_TYPE_VALUES: set[RemindercreateFilesBodyDataSubjectType] = {
    "CalendarEntry",
    "Task",
}


def check_remindercreate_files_body_data_subject_type(value: str) -> RemindercreateFilesBodyDataSubjectType:
    if value in REMINDERCREATE_FILES_BODY_DATA_SUBJECT_TYPE_VALUES:
        return cast(RemindercreateFilesBodyDataSubjectType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERCREATE_FILES_BODY_DATA_SUBJECT_TYPE_VALUES!r}"
    )
