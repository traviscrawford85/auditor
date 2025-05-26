from typing import Literal, cast

WebhookBaseStatus = Literal["enabled", "pending", "suspended"]

WEBHOOK_BASE_STATUS_VALUES: set[WebhookBaseStatus] = {
    "enabled",
    "pending",
    "suspended",
}


def check_webhook_base_status(value: str) -> WebhookBaseStatus:
    if value in WEBHOOK_BASE_STATUS_VALUES:
        return cast(WebhookBaseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_BASE_STATUS_VALUES!r}")
