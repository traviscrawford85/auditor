from typing import Literal, cast

LogEntryindexOrder = Literal["accessed_at(asc)", "accessed_at(desc)", "id(asc)", "id(desc)"]

LOG_ENTRYINDEX_ORDER_VALUES: set[LogEntryindexOrder] = {
    "accessed_at(asc)",
    "accessed_at(desc)",
    "id(asc)",
    "id(desc)",
}


def check_log_entryindex_order(value: str) -> LogEntryindexOrder:
    if value in LOG_ENTRYINDEX_ORDER_VALUES:
        return cast(LogEntryindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOG_ENTRYINDEX_ORDER_VALUES!r}")
