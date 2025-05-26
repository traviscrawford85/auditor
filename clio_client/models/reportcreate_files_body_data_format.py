from typing import Literal, cast

ReportcreateFilesBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORTCREATE_FILES_BODY_DATA_FORMAT_VALUES: set[ReportcreateFilesBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_reportcreate_files_body_data_format(value: str) -> ReportcreateFilesBodyDataFormat:
    if value in REPORTCREATE_FILES_BODY_DATA_FORMAT_VALUES:
        return cast(ReportcreateFilesBodyDataFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORTCREATE_FILES_BODY_DATA_FORMAT_VALUES!r}")
