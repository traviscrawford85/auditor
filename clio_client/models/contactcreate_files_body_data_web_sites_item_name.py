from typing import Literal, cast

ContactcreateFilesBodyDataWebSitesItemName = Literal[
    "Facebook", "Instant Messenger", "LinkedIn", "Other", "Personal", "Twitter", "Work"
]

CONTACTCREATE_FILES_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES: set[ContactcreateFilesBodyDataWebSitesItemName] = {
    "Facebook",
    "Instant Messenger",
    "LinkedIn",
    "Other",
    "Personal",
    "Twitter",
    "Work",
}


def check_contactcreate_files_body_data_web_sites_item_name(value: str) -> ContactcreateFilesBodyDataWebSitesItemName:
    if value in CONTACTCREATE_FILES_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES:
        return cast(ContactcreateFilesBodyDataWebSitesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_FILES_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES!r}"
    )
