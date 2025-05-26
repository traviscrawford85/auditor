from typing import Literal, cast

ContactcreateDataBodyDataWebSitesItemName = Literal[
    "Facebook", "Instant Messenger", "LinkedIn", "Other", "Personal", "Twitter", "Work"
]

CONTACTCREATE_DATA_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES: set[ContactcreateDataBodyDataWebSitesItemName] = {
    "Facebook",
    "Instant Messenger",
    "LinkedIn",
    "Other",
    "Personal",
    "Twitter",
    "Work",
}


def check_contactcreate_data_body_data_web_sites_item_name(value: str) -> ContactcreateDataBodyDataWebSitesItemName:
    if value in CONTACTCREATE_DATA_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES:
        return cast(ContactcreateDataBodyDataWebSitesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_DATA_BODY_DATA_WEB_SITES_ITEM_NAME_VALUES!r}"
    )
