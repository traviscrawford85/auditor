from typing import Literal, cast

WebhookBaseEventsItem = Literal["created", "deleted", "matter_closed", "matter_opened", "matter_pended", "updated"]

WEBHOOK_BASE_EVENTS_ITEM_VALUES: set[WebhookBaseEventsItem] = {
    "created",
    "deleted",
    "matter_closed",
    "matter_opened",
    "matter_pended",
    "updated",
}


def check_webhook_base_events_item(value: str) -> WebhookBaseEventsItem:
    if value in WEBHOOK_BASE_EVENTS_ITEM_VALUES:
        return cast(WebhookBaseEventsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_BASE_EVENTS_ITEM_VALUES!r}")
