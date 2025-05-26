from typing import Literal, cast

ContactupdateDataBodyDataWebSitesItemName = Literal[
    "Facebook", "Instant Messenger", "LinkedIn", "Other", "Personal", "Twitter", "Work"
]

CONTACTUPDATE_DATA_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES: set[ContactupdateDataBodyDataWebSitesItemName] = {
    "Facebook",
    "Instant Messenger",
    "LinkedIn",
    "Other",
    "Personal",
    "Twitter",
    "Work",
}


def check_contactupdate_data_body_data_web_sites_item_name(value: str) -> ContactupdateDataBodyDataWebSitesItemName:
    if value in CONTACTUPDATE_DATA_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES:
        return cast(ContactupdateDataBodyDataWebSitesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_DATA_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES!r}"
    )
