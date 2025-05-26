from typing import Literal, cast

ReminderindexSubjectType = Literal["calendar_entry", "task"]

REMINDERINDEX_SUBJECT_TYPE_VALUES: set[ReminderindexSubjectType] = {
    "calendar_entry",
    "task",
}


def check_reminderindex_subject_type(value: str) -> ReminderindexSubjectType:
    if value in REMINDERINDEX_SUBJECT_TYPE_VALUES:
        return cast(ReminderindexSubjectType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REMINDERINDEX_SUBJECT_TYPE_VALUES!r}")
