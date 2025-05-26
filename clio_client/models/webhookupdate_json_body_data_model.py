from typing import Literal, cast

WebhookupdateJsonBodyDataModel = Literal[
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

WEBHOOKUPDATE_JSON_BODY_DATA_MODEL_VALUES: set[WebhookupdateJsonBodyDataModel] = {
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


def check_webhookupdate_json_body_data_model(value: str) -> WebhookupdateJsonBodyDataModel:
    if value in WEBHOOKUPDATE_JSON_BODY_DATA_MODEL_VALUES:
        return cast(WebhookupdateJsonBodyDataModel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKUPDATE_JSON_BODY_DATA_MODEL_VALUES!r}")
