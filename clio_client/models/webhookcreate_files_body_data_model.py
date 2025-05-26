from typing import Literal, cast

WebhookcreateFilesBodyDataModel = Literal[
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

WEBHOOKCREATE_FILES_BODY_DATA_MODEL_VALUES: set[WebhookcreateFilesBodyDataModel] = {
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


def check_webhookcreate_files_body_data_model(value: str) -> WebhookcreateFilesBodyDataModel:
    if value in WEBHOOKCREATE_FILES_BODY_DATA_MODEL_VALUES:
        return cast(WebhookcreateFilesBodyDataModel, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKCREATE_FILES_BODY_DATA_MODEL_VALUES!r}")
