from typing import Literal, cast

AddressBaseName = Literal["Billing", "Home", "Other", "Work"]

ADDRESS_BASE_NAME_VALUES: set[AddressBaseName] = {
    "Billing",
    "Home",
    "Other",
    "Work",
}


def check_address_base_name(value: str) -> AddressBaseName:
    if value in ADDRESS_BASE_NAME_VALUES:
        return cast(AddressBaseName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADDRESS_BASE_NAME_VALUES!r}")
