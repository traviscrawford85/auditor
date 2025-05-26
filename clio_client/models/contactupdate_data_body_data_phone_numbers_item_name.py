from typing import Literal, cast

ContactupdateDataBodyDataPhoneNumbersItemName = Literal["Fax", "Home", "Mobile", "Other", "Pager", "Skype", "Work"]

CONTACTUPDATE_DATA_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES: set[ContactupdateDataBodyDataPhoneNumbersItemName] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Pager",
    "Skype",
    "Work",
}


def check_contactupdate_data_body_data_phone_numbers_item_name(
    value: str,
) -> ContactupdateDataBodyDataPhoneNumbersItemName:
    if value in CONTACTUPDATE_DATA_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES:
        return cast(ContactupdateDataBodyDataPhoneNumbersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_DATA_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES!r}"
    )
