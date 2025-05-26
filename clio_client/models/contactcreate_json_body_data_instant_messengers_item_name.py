from typing import Literal, cast

ContactcreateJsonBodyDataInstantMessengersItemName = Literal["Other", "Personal", "Work"]

CONTACTCREATE_JSON_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES: set[
    ContactcreateJsonBodyDataInstantMessengersItemName
] = {
    "Other",
    "Personal",
    "Work",
}


def check_contactcreate_json_body_data_instant_messengers_item_name(
    value: str,
) -> ContactcreateJsonBodyDataInstantMessengersItemName:
    if value in CONTACTCREATE_JSON_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES:
        return cast(ContactcreateJsonBodyDataInstantMessengersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_JSON_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES!r}"
    )
