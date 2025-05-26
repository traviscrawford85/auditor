from typing import Literal, cast

ContactupdateDataBodyDataAddressesItemName = Literal["Billing", "Home", "Other", "Work"]

CONTACTUPDATE_DATA_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES: set[ContactupdateDataBodyDataAddressesItemName] = {
    "Billing",
    "Home",
    "Other",
    "Work",
}


def check_contactupdate_data_body_data_addresses_item_name(value: str) -> ContactupdateDataBodyDataAddressesItemName:
    if value in CONTACTUPDATE_DATA_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactupdateDataBodyDataAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_DATA_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
