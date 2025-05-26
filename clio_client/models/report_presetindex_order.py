from typing import Literal, cast

ReportPresetindexOrder = Literal[
    "created_at(asc)",
    "created_at(desc)",
    "last_generated_at(asc)",
    "last_generated_at(desc)",
    "last_modified_at(asc)",
    "last_modified_at(desc)",
    "name(asc)",
    "name(desc)",
    "next_scheduled_date(asc)",
    "next_scheduled_date(desc)",
]

REPORT_PRESETINDEX_ORDER_VALUES: set[ReportPresetindexOrder] = {
    "created_at(asc)",
    "created_at(desc)",
    "last_generated_at(asc)",
    "last_generated_at(desc)",
    "last_modified_at(asc)",
    "last_modified_at(desc)",
    "name(asc)",
    "name(desc)",
    "next_scheduled_date(asc)",
    "next_scheduled_date(desc)",
}


def check_report_presetindex_order(value: str) -> ReportPresetindexOrder:
    if value in REPORT_PRESETINDEX_ORDER_VALUES:
        return cast(ReportPresetindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESETINDEX_ORDER_VALUES!r}")
