from typing import Literal, cast

ReportcreateJsonBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORTCREATE_JSON_BODY_DATA_FORMAT_VALUES: set[ReportcreateJsonBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_reportcreate_json_body_data_format(value: str) -> ReportcreateJsonBodyDataFormat:
    if value in REPORTCREATE_JSON_BODY_DATA_FORMAT_VALUES:
        return cast(ReportcreateJsonBodyDataFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORTCREATE_JSON_BODY_DATA_FORMAT_VALUES!r}")
