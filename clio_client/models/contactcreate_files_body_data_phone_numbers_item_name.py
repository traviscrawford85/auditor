from typing import Literal, cast

ContactcreateFilesBodyDataPhoneNumbersItemName = Literal["Fax", "Home", "Mobile", "Other", "Pager", "Skype", "Work"]

CONTACTCREATE_FILES_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES: set[ContactcreateFilesBodyDataPhoneNumbersItemName] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Pager",
    "Skype",
    "Work",
}


def check_contactcreate_files_body_data_phone_numbers_item_name(
    value: str,
) -> ContactcreateFilesBodyDataPhoneNumbersItemName:
    if value in CONTACTCREATE_FILES_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES:
        return cast(ContactcreateFilesBodyDataPhoneNumbersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_FILES_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES!r}"
    )
