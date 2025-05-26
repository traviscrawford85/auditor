from typing import Literal, cast

ContactupdateJsonBodyDataAddressesItemName = Literal["Billing", "Home", "Other", "Work"]

CONTACTUPDATE_JSON_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES: set[ContactupdateJsonBodyDataAddressesItemName] = {
    "Billing",
    "Home",
    "Other",
    "Work",
}


def check_contactupdate_json_body_data_addresses_item_name(value: str) -> ContactupdateJsonBodyDataAddressesItemName:
    if value in CONTACTUPDATE_JSON_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactupdateJsonBodyDataAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_JSON_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
