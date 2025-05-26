from typing import Literal, cast

WebhookupdateFilesBodyDataModel = Literal[
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

WEBHOOKUPDATE_FILES_BODY_DATA_MODEL_VALUES: set[WebhookupdateFilesBodyDataModel] = {
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


def check_webhookupdate_files_body_data_model(value: str) -> WebhookupdateFilesBodyDataModel:
    if value in WEBHOOKUPDATE_FILES_BODY_DATA_MODEL_VALUES:
        return cast(WebhookupdateFilesBodyDataModel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKUPDATE_FILES_BODY_DATA_MODEL_VALUES!r}")
