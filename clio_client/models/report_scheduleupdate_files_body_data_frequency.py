from typing import Literal, cast

ReportScheduleupdateFilesBodyDataFrequency = Literal["daily", "monthly", "weekly"]

REPORT_SCHEDULEUPDATE_FILES_BODY_DATA_FREQUENCY_VALUES: set[ReportScheduleupdateFilesBodyDataFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_scheduleupdate_files_body_data_frequency(value: str) -> ReportScheduleupdateFilesBodyDataFrequency:
    if value in REPORT_SCHEDULEUPDATE_FILES_BODY_DATA_FREQUENCY_VALUES:
        return cast(ReportScheduleupdateFilesBodyDataFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULEUPDATE_FILES_BODY_DATA_FREQUENCY_VALUES!r}"
    )
