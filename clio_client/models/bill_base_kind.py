from typing import Literal, cast

BillBaseKind = Literal[
    "aggregate_all",
    "aggregate_expenses",
    "aggregate_services",
    "aggregate_split",
    "revenue_kind",
    "summary_kind",
    "trust_kind",
]

BILL_BASE_KIND_VALUES: set[BillBaseKind] = {
    "aggregate_all",
    "aggregate_expenses",
    "aggregate_services",
    "aggregate_split",
    "revenue_kind",
    "summary_kind",
    "trust_kind",
}


def check_bill_base_kind(value: str) -> BillBaseKind:
    if value in BILL_BASE_KIND_VALUES:
        return cast(BillBaseKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_BASE_KIND_VALUES!r}")
