from typing import Literal, cast

RemindercreateJsonBodyDataSubjectType = Literal["CalendarEntry", "Task"]

REMINDERCREATE_JSON_BODY_DATA_SUBJECT_TYPE_VALUES: set[RemindercreateJsonBodyDataSubjectType] = {
    "CalendarEntry",
    "Task",
}


def check_remindercreate_json_body_data_subject_type(value: str) -> RemindercreateJsonBodyDataSubjectType:
    if value in REMINDERCREATE_JSON_BODY_DATA_SUBJECT_TYPE_VALUES:
        return cast(RemindercreateJsonBodyDataSubjectType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERCREATE_JSON_BODY_DATA_SUBJECT_TYPE_VALUES!r}"
    )
