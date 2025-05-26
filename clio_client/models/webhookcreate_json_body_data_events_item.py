from typing import Literal, cast

WebhookcreateJsonBodyDataEventsItem = Literal[
    "created", "deleted", "matter_closed", "matter_opened", "matter_pended", "updated"
]

WEBHOOKCREATE_JSON_BODY_DATA_EVENTS_ITEM_VALUES: set[WebhookcreateJsonBodyDataEventsItem] = {
    "created",
    "deleted",
    "matter_closed",
    "matter_opened",
    "matter_pended",
    "updated",
}


def check_webhookcreate_json_body_data_events_item(value: str) -> WebhookcreateJsonBodyDataEventsItem:
    if value in WEBHOOKCREATE_JSON_BODY_DATA_EVENTS_ITEM_VALUES:
        return cast(WebhookcreateJsonBodyDataEventsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKCREATE_JSON_BODY_DATA_EVENTS_ITEM_VALUES!r}")
