from typing import Literal, cast

GroupindexType = Literal["AccountGroup", "AdhocGroup", "UserGroup"]

GROUPINDEX_TYPE_VALUES: set[GroupindexType] = {
    "AccountGroup",
    "AdhocGroup",
    "UserGroup",
}


def check_groupindex_type(value: str) -> GroupindexType:
    if value in GROUPINDEX_TYPE_VALUES:
        return cast(GroupindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GROUPINDEX_TYPE_VALUES!r}")
