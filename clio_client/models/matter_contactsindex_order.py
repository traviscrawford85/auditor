from typing import Literal, cast

MatterContactsindexOrder = Literal["id(asc)", "id(desc)", "is_client(asc)", "is_client(desc)"]

MATTER_CONTACTSINDEX_ORDER_VALUES: set[MatterContactsindexOrder] = {
    "id(asc)",
    "id(desc)",
    "is_client(asc)",
    "is_client(desc)",
}


def check_matter_contactsindex_order(value: str) -> MatterContactsindexOrder:
    if value in MATTER_CONTACTSINDEX_ORDER_VALUES:
        return cast(MatterContactsindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_CONTACTSINDEX_ORDER_VALUES!r}")
