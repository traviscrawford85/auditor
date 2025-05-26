from typing import Literal, cast

ContactupdateFilesBodyDataEmailAddressesItemName = Literal["Home", "Other", "Work"]

CONTACTUPDATE_FILES_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES: set[
    ContactupdateFilesBodyDataEmailAddressesItemName
] = {
    "Home",
    "Other",
    "Work",
}


def check_contactupdate_files_body_data_email_addresses_item_name(
    value: str,
) -> ContactupdateFilesBodyDataEmailAddressesItemName:
    if value in CONTACTUPDATE_FILES_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactupdateFilesBodyDataEmailAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_FILES_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
