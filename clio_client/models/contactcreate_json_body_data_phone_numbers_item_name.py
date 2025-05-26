from typing import Literal, cast

ContactcreateJsonBodyDataPhoneNumbersItemName = Literal["Fax", "Home", "Mobile", "Other", "Pager", "Skype", "Work"]

CONTACTCREATE_JSON_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES: set[ContactcreateJsonBodyDataPhoneNumbersItemName] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Pager",
    "Skype",
    "Work",
}


def check_contactcreate_json_body_data_phone_numbers_item_name(
    value: str,
) -> ContactcreateJsonBodyDataPhoneNumbersItemName:
    if value in CONTACTCREATE_JSON_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES:
        return cast(ContactcreateJsonBodyDataPhoneNumbersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_JSON_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES!r}"
    )
