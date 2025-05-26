from typing import Literal, cast

ReportcreateDataBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORTCREATE_DATA_BODY_DATA_FORMAT_VALUES: set[ReportcreateDataBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_reportcreate_data_body_data_format(value: str) -> ReportcreateDataBodyDataFormat:
    if value in REPORTCREATE_DATA_BODY_DATA_FORMAT_VALUES:
        return cast(ReportcreateDataBodyDataFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORTCREATE_DATA_BODY_DATA_FORMAT_VALUES!r}")
