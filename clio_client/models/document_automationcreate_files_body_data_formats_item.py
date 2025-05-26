from typing import Literal, cast

DocumentAutomationcreateFilesBodyDataFormatsItem = Literal["original", "pdf"]

DOCUMENT_AUTOMATIONCREATE_FILES_BODY_DATA_FORMATS_ITEM_VALUES: set[DocumentAutomationcreateFilesBodyDataFormatsItem] = {
    "original",
    "pdf",
}


def check_document_automationcreate_files_body_data_formats_item(
    value: str,
) -> DocumentAutomationcreateFilesBodyDataFormatsItem:
    if value in DOCUMENT_AUTOMATIONCREATE_FILES_BODY_DATA_FORMATS_ITEM_VALUES:
        return cast(DocumentAutomationcreateFilesBodyDataFormatsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENT_AUTOMATIONCREATE_FILES_BODY_DATA_FORMATS_ITEM_VALUES!r}"
    )
