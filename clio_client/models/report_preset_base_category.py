from typing import Literal, cast

ReportPresetBaseCategory = Literal[
    "billing", "client", "compliance", "financial", "matter", "online_payments", "productivity", "revenue", "task"
]

REPORT_PRESET_BASE_CATEGORY_VALUES: set[ReportPresetBaseCategory] = {
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


def check_report_preset_base_category(value: str) -> ReportPresetBaseCategory:
    if value in REPORT_PRESET_BASE_CATEGORY_VALUES:
        return cast(ReportPresetBaseCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESET_BASE_CATEGORY_VALUES!r}")
