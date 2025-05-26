from typing import Literal, cast

ContactupdateJsonBodyDataEmailAddressesItemName = Literal["Home", "Other", "Work"]

CONTACTUPDATE_JSON_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES: set[ContactupdateJsonBodyDataEmailAddressesItemName] = {
    "Home",
    "Other",
    "Work",
}


def check_contactupdate_json_body_data_email_addresses_item_name(
    value: str,
) -> ContactupdateJsonBodyDataEmailAddressesItemName:
    if value in CONTACTUPDATE_JSON_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactupdateJsonBodyDataEmailAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_JSON_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
