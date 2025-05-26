from typing import Literal, cast

ReportPresetindexCategory = Literal[
    "billing", "client", "compliance", "financial", "matter", "online_payments", "productivity", "revenue", "task"
]

REPORT_PRESETINDEX_CATEGORY_VALUES: set[ReportPresetindexCategory] = {
    "billing",
    "client",
    "compliance",
    "financial",
    "matter",
    "online_payments",
    "productivity",
    "revenue",
    "task",
}


def check_report_presetindex_category(value: str) -> ReportPresetindexCategory:
    if value in REPORT_PRESETINDEX_CATEGORY_VALUES:
        return cast(ReportPresetindexCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESETINDEX_CATEGORY_VALUES!r}")
