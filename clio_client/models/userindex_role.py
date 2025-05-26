from typing import Literal, cast

UserindexRole = Literal["accounts", "admin", "billing", "reports"]

USERINDEX_ROLE_VALUES: set[UserindexRole] = {
    "accounts",
    "admin",
    "billing",
    "reports",
}


def check_userindex_role(value: str) -> UserindexRole:
    if value in USERINDEX_ROLE_VALUES:
        return cast(UserindexRole, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USERINDEX_ROLE_VALUES!r}")
