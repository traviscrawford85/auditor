from typing import Literal, cast

WebhookupdateDataBodyDataModel = Literal[
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

WEBHOOKUPDATE_DATA_BODY_DATA_MODEL_VALUES: set[WebhookupdateDataBodyDataModel] = {
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


def check_webhookupdate_data_body_data_model(value: str) -> WebhookupdateDataBodyDataModel:
    if value in WEBHOOKUPDATE_DATA_BODY_DATA_MODEL_VALUES:
        return cast(WebhookupdateDataBodyDataModel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKUPDATE_DATA_BODY_DATA_MODEL_VALUES!r}")
