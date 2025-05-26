from typing import Literal, cast

WebhookupdateFilesBodyDataEventsItem = Literal[
    "created", "deleted", "matter_closed", "matter_opened", "matter_pended", "updated"
]

WEBHOOKUPDATE_FILES_BODY_DATA_EVENTS_ITEM_VALUES: set[WebhookupdateFilesBodyDataEventsItem] = {
    "created",
    "deleted",
    "matter_closed",
    "matter_opened",
    "matter_pended",
    "updated",
}


def check_webhookupdate_files_body_data_events_item(value: str) -> WebhookupdateFilesBodyDataEventsItem:
    if value in WEBHOOKUPDATE_FILES_BODY_DATA_EVENTS_ITEM_VALUES:
        return cast(WebhookupdateFilesBodyDataEventsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKUPDATE_FILES_BODY_DATA_EVENTS_ITEM_VALUES!r}")
