from typing import Literal, cast

ContactcreateFilesBodyDataEmailAddressesItemName = Literal["Home", "Other", "Work"]

CONTACTCREATE_FILES_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES: set[
    ContactcreateFilesBodyDataEmailAddressesItemName
] = {
    "Home",
    "Other",
    "Work",
}


def check_contactcreate_files_body_data_email_addresses_item_name(
    value: str,
) -> ContactcreateFilesBodyDataEmailAddressesItemName:
    if value in CONTACTCREATE_FILES_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactcreateFilesBodyDataEmailAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_FILES_BODY_DATA_EMAIL_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
