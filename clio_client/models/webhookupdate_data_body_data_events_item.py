from typing import Literal, cast

WebhookupdateDataBodyDataEventsItem = Literal[
    "created", "deleted", "matter_closed", "matter_opened", "matter_pended", "updated"
]

WEBHOOKUPDATE_DATA_BODY_DATA_EVENTS_ITEM_VALUES: set[WebhookupdateDataBodyDataEventsItem] = {
    "created",
    "deleted",
    "matter_closed",
    "matter_opened",
    "matter_pended",
    "updated",
}


def check_webhookupdate_data_body_data_events_item(value: str) -> WebhookupdateDataBodyDataEventsItem:
    if value in WEBHOOKUPDATE_DATA_BODY_DATA_EVENTS_ITEM_VALUES:
        return cast(WebhookupdateDataBodyDataEventsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKUPDATE_DATA_BODY_DATA_EVENTS_ITEM_VALUES!r}")
