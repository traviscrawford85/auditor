from typing import Literal, cast

MatterindexOpenDate = Literal["<=DATE", "<DATE", "=DATE", ">=DATE", ">DATE"]

MATTERINDEX_OPEN_DATE_VALUES: set[MatterindexOpenDate] = {
    "<=DATE",
    "<DATE",
    "=DATE",
    ">=DATE",
    ">DATE",
}


def check_matterindex_open_date(value: str) -> MatterindexOpenDate:
    if value in MATTERINDEX_OPEN_DATE_VALUES:
        return cast(MatterindexOpenDate, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERINDEX_OPEN_DATE_VALUES!r}")
