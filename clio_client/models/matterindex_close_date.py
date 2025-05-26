from typing import Literal, cast

MatterindexCloseDate = Literal["<=DATE", "<DATE", "=DATE", ">=DATE", ">DATE"]

MATTERINDEX_CLOSE_DATE_VALUES: set[MatterindexCloseDate] = {
    "<=DATE",
    "<DATE",
    "=DATE",
    ">=DATE",
    ">DATE",
}


def check_matterindex_close_date(value: str) -> MatterindexCloseDate:
    if value in MATTERINDEX_CLOSE_DATE_VALUES:
        return cast(MatterindexCloseDate, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERINDEX_CLOSE_DATE_VALUES!r}")
