from typing import Literal, cast

RelatedContactsindexOrder = Literal["id(asc)", "id(desc)"]

RELATED_CONTACTSINDEX_ORDER_VALUES: set[RelatedContactsindexOrder] = {
    "id(asc)",
    "id(desc)",
}


def check_related_contactsindex_order(value: str) -> RelatedContactsindexOrder:
    if value in RELATED_CONTACTSINDEX_ORDER_VALUES:
        return cast(RelatedContactsindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RELATED_CONTACTSINDEX_ORDER_VALUES!r}")
