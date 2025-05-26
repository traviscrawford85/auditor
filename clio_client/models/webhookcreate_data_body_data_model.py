from typing import Literal, cast

WebhookcreateDataBodyDataModel = Literal[
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

WEBHOOKCREATE_DATA_BODY_DATA_MODEL_VALUES: set[WebhookcreateDataBodyDataModel] = {
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


def check_webhookcreate_data_body_data_model(value: str) -> WebhookcreateDataBodyDataModel:
    if value in WEBHOOKCREATE_DATA_BODY_DATA_MODEL_VALUES:
        return cast(WebhookcreateDataBodyDataModel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKCREATE_DATA_BODY_DATA_MODEL_VALUES!r}")
