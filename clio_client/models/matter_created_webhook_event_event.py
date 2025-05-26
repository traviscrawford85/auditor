from typing import Literal, cast

MatterCreatedWebhookEventEvent = Literal["matter.created"]

MATTER_CREATED_WEBHOOK_EVENT_EVENT_VALUES: set[MatterCreatedWebhookEventEvent] = {
    "matter.created",
}


def check_matter_created_webhook_event_event(value: str) -> MatterCreatedWebhookEventEvent:
    if value in MATTER_CREATED_WEBHOOK_EVENT_EVENT_VALUES:
        return cast(MatterCreatedWebhookEventEvent, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_CREATED_WEBHOOK_EVENT_EVENT_VALUES!r}")
