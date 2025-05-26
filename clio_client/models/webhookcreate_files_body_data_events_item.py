from typing import Literal, cast

WebhookcreateFilesBodyDataEventsItem = Literal[
    "created", "deleted", "matter_closed", "matter_opened", "matter_pended", "updated"
]

WEBHOOKCREATE_FILES_BODY_DATA_EVENTS_ITEM_VALUES: set[WebhookcreateFilesBodyDataEventsItem] = {
    "created",
    "deleted",
    "matter_closed",
    "matter_opened",
    "matter_pended",
    "updated",
}


def check_webhookcreate_files_body_data_events_item(value: str) -> WebhookcreateFilesBodyDataEventsItem:
    if value in WEBHOOKCREATE_FILES_BODY_DATA_EVENTS_ITEM_VALUES:
        return cast(WebhookcreateFilesBodyDataEventsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKCREATE_FILES_BODY_DATA_EVENTS_ITEM_VALUES!r}")
