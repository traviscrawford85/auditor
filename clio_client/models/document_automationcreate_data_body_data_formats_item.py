from typing import Literal, cast

DocumentAutomationcreateDataBodyDataFormatsItem = Literal["original", "pdf"]

DOCUMENT_AUTOMATIONCREATE_DATA_BODY_DATA_FORMATS_ITEM_VALUES: set[DocumentAutomationcreateDataBodyDataFormatsItem] = {
    "original",
    "pdf",
}


def check_document_automationcreate_data_body_data_formats_item(
    value: str,
) -> DocumentAutomationcreateDataBodyDataFormatsItem:
    if value in DOCUMENT_AUTOMATIONCREATE_DATA_BODY_DATA_FORMATS_ITEM_VALUES:
        return cast(DocumentAutomationcreateDataBodyDataFormatsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENT_AUTOMATIONCREATE_DATA_BODY_DATA_FORMATS_ITEM_VALUES!r}"
    )
