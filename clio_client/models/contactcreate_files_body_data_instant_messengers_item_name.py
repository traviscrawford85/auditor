from typing import Literal, cast

ContactcreateFilesBodyDataInstantMessengersItemName = Literal["Other", "Personal", "Work"]

CONTACTCREATE_FILES_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES: set[
    ContactcreateFilesBodyDataInstantMessengersItemName
] = {
    "Other",
    "Personal",
    "Work",
}


def check_contactcreate_files_body_data_instant_messengers_item_name(
    value: str,
) -> ContactcreateFilesBodyDataInstantMessengersItemName:
    if value in CONTACTCREATE_FILES_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES:
        return cast(ContactcreateFilesBodyDataInstantMessengersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_FILES_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES!r}"
    )
