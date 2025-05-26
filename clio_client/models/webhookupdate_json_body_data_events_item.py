from typing import Literal, cast

WebhookupdateJsonBodyDataEventsItem = Literal[
    "created", "deleted", "matter_closed", "matter_opened", "matter_pended", "updated"
]

WEBHOOKUPDATE_JSON_BODY_DATA_EVENTS_ITEM_VALUES: set[WebhookupdateJsonBodyDataEventsItem] = {
    "created",
    "deleted",
    "matter_closed",
    "matter_opened",
    "matter_pended",
    "updated",
}


def check_webhookupdate_json_body_data_events_item(value: str) -> WebhookupdateJsonBodyDataEventsItem:
    if value in WEBHOOKUPDATE_JSON_BODY_DATA_EVENTS_ITEM_VALUES:
        return cast(WebhookupdateJsonBodyDataEventsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKUPDATE_JSON_BODY_DATA_EVENTS_ITEM_VALUES!r}")
