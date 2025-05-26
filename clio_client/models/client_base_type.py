from typing import Literal, cast

ClientBaseType = Literal["Company", "Person"]

CLIENT_BASE_TYPE_VALUES: set[ClientBaseType] = {
    "Company",
    "Person",
}


def check_client_base_type(value: str) -> ClientBaseType:
    if value in CLIENT_BASE_TYPE_VALUES:
        return cast(ClientBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLIENT_BASE_TYPE_VALUES!r}")
