from typing import Literal, cast

ReportBaseCategory = Literal[
    "billing", "client", "compliance", "financial", "matter", "online_payments", "productivity", "revenue", "task"
]

REPORT_BASE_CATEGORY_VALUES: set[ReportBaseCategory] = {
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


def check_report_base_category(value: str) -> ReportBaseCategory:
    if value in REPORT_BASE_CATEGORY_VALUES:
        return cast(ReportBaseCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_BASE_CATEGORY_VALUES!r}")
