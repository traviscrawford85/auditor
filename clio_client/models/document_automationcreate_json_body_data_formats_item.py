from typing import Literal, cast

DocumentAutomationcreateJsonBodyDataFormatsItem = Literal["original", "pdf"]

DOCUMENT_AUTOMATIONCREATE_JSON_BODY_DATA_FORMATS_ITEM_VALUES: set[DocumentAutomationcreateJsonBodyDataFormatsItem] = {
    "original",
    "pdf",
}


def check_document_automationcreate_json_body_data_formats_item(
    value: str,
) -> DocumentAutomationcreateJsonBodyDataFormatsItem:
    if value in DOCUMENT_AUTOMATIONCREATE_JSON_BODY_DATA_FORMATS_ITEM_VALUES:
        return cast(DocumentAutomationcreateJsonBodyDataFormatsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENT_AUTOMATIONCREATE_JSON_BODY_DATA_FORMATS_ITEM_VALUES!r}"
    )
