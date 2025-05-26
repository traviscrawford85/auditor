from typing import Literal, cast

ContactupdateJsonBodyDataPhoneNumbersItemName = Literal["Fax", "Home", "Mobile", "Other", "Pager", "Skype", "Work"]

CONTACTUPDATE_JSON_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES: set[ContactupdateJsonBodyDataPhoneNumbersItemName] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Pager",
    "Skype",
    "Work",
}


def check_contactupdate_json_body_data_phone_numbers_item_name(
    value: str,
) -> ContactupdateJsonBodyDataPhoneNumbersItemName:
    if value in CONTACTUPDATE_JSON_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES:
        return cast(ContactupdateJsonBodyDataPhoneNumbersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_JSON_BODY_DATA_PHONE_NUMBERS_ITEM_NAME_VALUES!r}"
    )
