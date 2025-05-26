from typing import Literal, cast

ContactcreateJsonBodyDataEmailAddressesItemName = Literal["Home", "Other", "Work"]

CONTACTCREATE_JSON_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES: set[ContactcreateJsonBodyDataEmailAddressesItemName] = {
    "Home",
    "Other",
    "Work",
}


def check_contactcreate_json_body_data_email_addresses_item_name(
    value: str,
) -> ContactcreateJsonBodyDataEmailAddressesItemName:
    if value in CONTACTCREATE_JSON_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactcreateJsonBodyDataEmailAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_JSON_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
