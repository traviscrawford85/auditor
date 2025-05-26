from typing import Literal, cast

DocumentAutomationBaseExportFormats = Literal["original", "pdf"]

DOCUMENT_AUTOMATION_BASE_EXPORT_FORMATS_VALUES: set[DocumentAutomationBaseExportFormats] = {
    "original",
    "pdf",
}


def check_document_automation_base_export_formats(value: str) -> DocumentAutomationBaseExportFormats:
    if value in DOCUMENT_AUTOMATION_BASE_EXPORT_FORMATS_VALUES:
        return cast(DocumentAutomationBaseExportFormats, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_AUTOMATION_BASE_EXPORT_FORMATS_VALUES!r}")
