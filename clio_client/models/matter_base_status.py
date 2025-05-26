from typing import Literal, cast

MatterBaseStatus = Literal["Closed", "Open", "Pending"]

MATTER_BASE_STATUS_VALUES: set[MatterBaseStatus] = {
    "Closed",
    "Open",
    "Pending",
}


def check_matter_base_status(value: str) -> MatterBaseStatus:
    if value in MATTER_BASE_STATUS_VALUES:
        return cast(MatterBaseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_BASE_STATUS_VALUES!r}")
