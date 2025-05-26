from typing import Literal, cast

WebhookBaseModel = Literal[
    "activity",
    "bill",
    "calendar_entry",
    "clio_payments_payment",
    "communication",
    "contact",
    "document",
    "folder",
    "matter",
    "task",
]

WEBHOOK_BASE_MODEL_VALUES: set[WebhookBaseModel] = {
    "activity",
    "bill",
    "calendar_entry",
    "clio_payments_payment",
    "communication",
    "contact",
    "document",
    "folder",
    "matter",
    "task",
}


def check_webhook_base_model(value: str) -> WebhookBaseModel:
    if value in WEBHOOK_BASE_MODEL_VALUES:
        return cast(WebhookBaseModel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_BASE_MODEL_VALUES!r}")
