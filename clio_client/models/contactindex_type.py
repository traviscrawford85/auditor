from typing import Literal, cast

ContactindexType = Literal["Company", "Person"]

CONTACTINDEX_TYPE_VALUES: set[ContactindexType] = {
    "Company",
    "Person",
}


def check_contactindex_type(value: str) -> ContactindexType:
    if value in CONTACTINDEX_TYPE_VALUES:
        return cast(ContactindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTINDEX_TYPE_VALUES!r}")
