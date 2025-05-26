from typing import Literal, cast

GroupBaseType = Literal["AccountGroup", "AdhocGroup", "TeamGroup", "UserGroup"]

GROUP_BASE_TYPE_VALUES: set[GroupBaseType] = {
    "AccountGroup",
    "AdhocGroup",
    "TeamGroup",
    "UserGroup",
}


def check_group_base_type(value: str) -> GroupBaseType:
    if value in GROUP_BASE_TYPE_VALUES:
        return cast(GroupBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GROUP_BASE_TYPE_VALUES!r}")
