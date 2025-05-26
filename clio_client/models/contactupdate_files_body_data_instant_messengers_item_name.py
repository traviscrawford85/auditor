from typing import Literal, cast

ContactupdateFilesBodyDataInstantMessengersItemName = Literal["Other", "Personal", "Work"]

CONTACTUPDATE_FILES_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES: set[
    ContactupdateFilesBodyDataInstantMessengersItemName
] = {
    "Other",
    "Personal",
    "Work",
}


def check_contactupdate_files_body_data_instant_messengers_item_name(
    value: str,
) -> ContactupdateFilesBodyDataInstantMessengersItemName:
    if value in CONTACTUPDATE_FILES_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES:
        return cast(ContactupdateFilesBodyDataInstantMessengersItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_FILES_BODY_DATA_INSTANT_MESSENGERS_ITEM_NAME_VALUES!r}"
    )
