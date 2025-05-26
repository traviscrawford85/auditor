from typing import Literal, cast

ContactcreateDataBodyDataEmailAddressesItemName = Literal["Home", "Other", "Work"]

CONTACTCREATE_DATA_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES: set[ContactcreateDataBodyDataEmailAddressesItemName] = {
    "Home",
    "Other",
    "Work",
}


def check_contactcreate_data_body_data_email_addresses_item_name(
    value: str,
) -> ContactcreateDataBodyDataEmailAddressesItemName:
    if value in CONTACTCREATE_DATA_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactcreateDataBodyDataEmailAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_DATA_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
