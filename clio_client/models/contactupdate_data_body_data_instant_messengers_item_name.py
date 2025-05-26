from typing import Literal, cast

ContactupdateDataBodyDataInstantMessengersItemName = Literal["Other", "Personal", "Work"]

CONTACTUPDATE_DATA_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES: set[
    ContactupdateDataBodyDataInstantMessengersItemName
] = {
    "Other",
    "Personal",
    "Work",
}


def check_contactupdate_data_body_data_instant_messengers_item_name(
    value: str,
) -> ContactupdateDataBodyDataInstantMessengersItemName:
    if value in CONTACTUPDATE_DATA_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES:
        return cast(ContactupdateDataBodyDataInstantMessengersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_DATA_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES!r}"
    )
