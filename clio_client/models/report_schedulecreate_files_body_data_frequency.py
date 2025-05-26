from typing import Literal, cast

ReportSchedulecreateFilesBodyDataFrequency = Literal["daily", "monthly", "weekly"]

REPORT_SCHEDULECREATE_FILES_BODY_DATA_FREQUENCY_VALUES: set[ReportSchedulecreateFilesBodyDataFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_schedulecreate_files_body_data_frequency(value: str) -> ReportSchedulecreateFilesBodyDataFrequency:
    if value in REPORT_SCHEDULECREATE_FILES_BODY_DATA_FREQUENCY_VALUES:
        return cast(ReportSchedulecreateFilesBodyDataFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULECREATE_FILES_BODY_DATA_FREQUENCY_VALUES!r}"
    )
