from typing import Literal, cast

ContactcreateJsonBodyDataWebSitesItemName = Literal[
    "Facebook", "Instant Messenger", "LinkedIn", "Other", "Personal", "Twitter", "Work"
]

CONTACTCREATE_JSON_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES: set[ContactcreateJsonBodyDataWebSitesItemName] = {
    "Facebook",
    "Instant Messenger",
    "LinkedIn",
    "Other",
    "Personal",
    "Twitter",
    "Work",
}


def check_contactcreate_json_body_data_web_sites_item_name(value: str) -> ContactcreateJsonBodyDataWebSitesItemName:
    if value in CONTACTCREATE_JSON_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES:
        return cast(ContactcreateJsonBodyDataWebSitesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_JSON_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES!r}"
    )
