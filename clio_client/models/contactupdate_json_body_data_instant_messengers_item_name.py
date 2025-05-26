from typing import Literal, cast

ContactupdateJsonBodyDataInstantMessengersItemName = Literal["Other", "Personal", "Work"]

CONTACTUPDATE_JSON_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES: set[
    ContactupdateJsonBodyDataInstantMessengersItemName
] = {
    "Other",
    "Personal",
    "Work",
}


def check_contactupdate_json_body_data_instant_messengers_item_name(
    value: str,
) -> ContactupdateJsonBodyDataInstantMessengersItemName:
    if value in CONTACTUPDATE_JSON_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES:
        return cast(ContactupdateJsonBodyDataInstantMessengersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_JSON_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES!r}"
    )
