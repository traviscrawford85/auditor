from typing import Literal, cast

ContactupdateJsonBodyDataWebSitesItemName = Literal[
    "Facebook", "Instant Messenger", "LinkedIn", "Other", "Personal", "Twitter", "Work"
]

CONTACTUPDATE_JSON_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES: set[ContactupdateJsonBodyDataWebSitesItemName] = {
    "Facebook",
    "Instant Messenger",
    "LinkedIn",
    "Other",
    "Personal",
    "Twitter",
    "Work",
}


def check_contactupdate_json_body_data_web_sites_item_name(value: str) -> ContactupdateJsonBodyDataWebSitesItemName:
    if value in CONTACTUPDATE_JSON_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES:
        return cast(ContactupdateJsonBodyDataWebSitesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_JSON_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES!r}"
    )
