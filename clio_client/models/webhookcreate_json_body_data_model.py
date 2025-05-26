from typing import Literal, cast

WebhookcreateJsonBodyDataModel = Literal[
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

WEBHOOKCREATE_JSON_BODY_DATA_MODEL_VALUES: set[WebhookcreateJsonBodyDataModel] = {
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


def check_webhookcreate_json_body_data_model(value: str) -> WebhookcreateJsonBodyDataModel:
    if value in WEBHOOKCREATE_JSON_BODY_DATA_MODEL_VALUES:
        return cast(WebhookcreateJsonBodyDataModel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKCREATE_JSON_BODY_DATA_MODEL_VALUES!r}")
