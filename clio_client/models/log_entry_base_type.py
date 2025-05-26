from typing import Literal, cast

LogEntryBaseType = Literal["ContactLogEntry", "MatterLogEntry"]

LOG_ENTRY_BASE_TYPE_VALUES: set[LogEntryBaseType] = {
    "ContactLogEntry",
    "MatterLogEntry",
}


def check_log_entry_base_type(value: str) -> LogEntryBaseType:
    if value in LOG_ENTRY_BASE_TYPE_VALUES:
        return cast(LogEntryBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOG_ENTRY_BASE_TYPE_VALUES!r}")
