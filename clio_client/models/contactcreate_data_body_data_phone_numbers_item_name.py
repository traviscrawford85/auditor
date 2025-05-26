from typing import Literal, cast

ContactcreateDataBodyDataPhoneNumbersItemName = Literal["Fax", "Home", "Mobile", "Other", "Pager", "Skype", "Work"]

CONTACTCREATE_DATA_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES: set[ContactcreateDataBodyDataPhoneNumbersItemName] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Pager",
    "Skype",
    "Work",
}


def check_contactcreate_data_body_data_phone_numbers_item_name(
    value: str,
) -> ContactcreateDataBodyDataPhoneNumbersItemName:
    if value in CONTACTCREATE_DATA_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES:
        return cast(ContactcreateDataBodyDataPhoneNumbersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_DATA_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES!r}"
    )
