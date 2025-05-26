from typing import Literal, cast

ContactupdateFilesBodyDataPhoneNumbersItemName = Literal["Fax", "Home", "Mobile", "Other", "Pager", "Skype", "Work"]

CONTACTUPDATE_FILES_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES: set[ContactupdateFilesBodyDataPhoneNumbersItemName] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Pager",
    "Skype",
    "Work",
}


def check_contactupdate_files_body_data_phone_numbers_item_name(
    value: str,
) -> ContactupdateFilesBodyDataPhoneNumbersItemName:
    if value in CONTACTUPDATE_FILES_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES:
        return cast(ContactupdateFilesBodyDataPhoneNumbersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_FILES_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES!r}"
    )
