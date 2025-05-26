from typing import Literal, cast

ContactcreateJsonBodyDataAddressesItemName = Literal["Billing", "Home", "Other", "Work"]

CONTACTCREATE_JSON_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES: set[ContactcreateJsonBodyDataAddressesItemName] = {
    "Billing",
    "Home",
    "Other",
    "Work",
}


def check_contactcreate_json_body_data_addresses_item_name(value: str) -> ContactcreateJsonBodyDataAddressesItemName:
    if value in CONTACTCREATE_JSON_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactcreateJsonBodyDataAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_JSON_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
