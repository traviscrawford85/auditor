from typing import Literal, cast

UserindexOrder = Literal[
    "email(asc)",
    "email(desc)",
    "enabled(asc)",
    "enabled(desc)",
    "first_name(asc)",
    "first_name(desc)",
    "id(asc)",
    "id(desc)",
    "initials(asc)",
    "initials(desc)",
    "last_name(asc)",
    "last_name(desc)",
    "name(asc)",
    "name(desc)",
    "subscription_type(asc)",
    "subscription_type(desc)",
]

USERINDEX_ORDER_VALUES: set[UserindexOrder] = {
    "email(asc)",
    "email(desc)",
    "enabled(asc)",
    "enabled(desc)",
    "first_name(asc)",
    "first_name(desc)",
    "id(asc)",
    "id(desc)",
    "initials(asc)",
    "initials(desc)",
    "last_name(asc)",
    "last_name(desc)",
    "name(asc)",
    "name(desc)",
    "subscription_type(asc)",
    "subscription_type(desc)",
}


def check_userindex_order(value: str) -> UserindexOrder:
    if value in USERINDEX_ORDER_VALUES:
        return cast(UserindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USERINDEX_ORDER_VALUES!r}")
