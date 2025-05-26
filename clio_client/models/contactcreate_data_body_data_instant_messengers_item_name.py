from typing import Literal, cast

ContactcreateDataBodyDataInstantMessengersItemName = Literal["Other", "Personal", "Work"]

CONTACTCREATE_DATA_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES: set[
    ContactcreateDataBodyDataInstantMessengersItemName
] = {
    "Other",
    "Personal",
    "Work",
}


def check_contactcreate_data_body_data_instant_messengers_item_name(
    value: str,
) -> ContactcreateDataBodyDataInstantMessengersItemName:
    if value in CONTACTCREATE_DATA_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES:
        return cast(ContactcreateDataBodyDataInstantMessengersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_DATA_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES!r}"
    )
