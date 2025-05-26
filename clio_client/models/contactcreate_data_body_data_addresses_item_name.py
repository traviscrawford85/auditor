from typing import Literal, cast

ContactcreateDataBodyDataAddressesItemName = Literal["Billing", "Home", "Other", "Work"]

CONTACTCREATE_DATA_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES: set[ContactcreateDataBodyDataAddressesItemName] = {
    "Billing",
    "Home",
    "Other",
    "Work",
}


def check_contactcreate_data_body_data_addresses_item_name(value: str) -> ContactcreateDataBodyDataAddressesItemName:
    if value in CONTACTCREATE_DATA_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactcreateDataBodyDataAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_DATA_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
