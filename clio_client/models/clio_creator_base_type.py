from typing import Literal, cast

ClioCreatorBaseType = Literal["ClientUser", "ManageUser"]

CLIO_CREATOR_BASE_TYPE_VALUES: set[ClioCreatorBaseType] = {
    "ClientUser",
    "ManageUser",
}


def check_clio_creator_base_type(value: str) -> ClioCreatorBaseType:
    if value in CLIO_CREATOR_BASE_TYPE_VALUES:
        return cast(ClioCreatorBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLIO_CREATOR_BASE_TYPE_VALUES!r}")
