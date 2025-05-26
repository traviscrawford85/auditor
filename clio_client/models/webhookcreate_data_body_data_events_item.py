from typing import Literal, cast

WebhookcreateDataBodyDataEventsItem = Literal[
    "created", "deleted", "matter_closed", "matter_opened", "matter_pended", "updated"
]

WEBHOOKCREATE_DATA_BODY_DATA_EVENTS_ITEM_VALUES: set[WebhookcreateDataBodyDataEventsItem] = {
    "created",
    "deleted",
    "matter_closed",
    "matter_opened",
    "matter_pended",
    "updated",
}


def check_webhookcreate_data_body_data_events_item(value: str) -> WebhookcreateDataBodyDataEventsItem:
    if value in WEBHOOKCREATE_DATA_BODY_DATA_EVENTS_ITEM_VALUES:
        return cast(WebhookcreateDataBodyDataEventsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKCREATE_DATA_BODY_DATA_EVENTS_ITEM_VALUES!r}")
