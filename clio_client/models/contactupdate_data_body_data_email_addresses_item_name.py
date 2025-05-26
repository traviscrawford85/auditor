from typing import Literal, cast

ContactupdateDataBodyDataEmailAddressesItemName = Literal["Home", "Other", "Work"]

CONTACTUPDATE_DATA_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES: set[ContactupdateDataBodyDataEmailAddressesItemName] = {
    "Home",
    "Other",
    "Work",
}


def check_contactupdate_data_body_data_email_addresses_item_name(
    value: str,
) -> ContactupdateDataBodyDataEmailAddressesItemName:
    if value in CONTACTUPDATE_DATA_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactupdateDataBodyDataEmailAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_DATA_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
