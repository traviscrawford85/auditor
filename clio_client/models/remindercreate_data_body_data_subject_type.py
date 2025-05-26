from typing import Literal, cast

RemindercreateDataBodyDataSubjectType = Literal["CalendarEntry", "Task"]

REMINDERCREATE_DATA_BODY_DATA_SUBJECT_TYPE_VALUES: set[RemindercreateDataBodyDataSubjectType] = {
    "CalendarEntry",
    "Task",
}


def check_remindercreate_data_body_data_subject_type(value: str) -> RemindercreateDataBodyDataSubjectType:
    if value in REMINDERCREATE_DATA_BODY_DATA_SUBJECT_TYPE_VALUES:
        return cast(RemindercreateDataBodyDataSubjectType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERCREATE_DATA_BODY_DATA_SUBJECT_TYPE_VALUES!r}"
    )
