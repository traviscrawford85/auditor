from typing import Literal, cast

ContactupdateFilesBodyDataWebSitesItemName = Literal[
    "Facebook", "Instant Messenger", "LinkedIn", "Other", "Personal", "Twitter", "Work"
]

CONTACTUPDATE_FILES_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES: set[ContactupdateFilesBodyDataWebSitesItemName] = {
    "Facebook",
    "Instant Messenger",
    "LinkedIn",
    "Other",
    "Personal",
    "Twitter",
    "Work",
}


def check_contactupdate_files_body_data_web_sites_item_name(value: str) -> ContactupdateFilesBodyDataWebSitesItemName:
    if value in CONTACTUPDATE_FILES_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES:
        return cast(ContactupdateFilesBodyDataWebSitesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_FILES_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES!r}"
    )
