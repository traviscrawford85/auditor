from typing import Literal, cast

ReportPresetupdateFilesBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_PRESETUPDATE_FILES_BODY_DATA_FORMAT_VALUES: set[ReportPresetupdateFilesBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_presetupdate_files_body_data_format(value: str) -> ReportPresetupdateFilesBodyDataFormat:
    if value in REPORT_PRESETUPDATE_FILES_BODY_DATA_FORMAT_VALUES:
        return cast(ReportPresetupdateFilesBodyDataFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_PRESETUPDATE_FILES_BODY_DATA_FORMAT_VALUES!r}"
    )
