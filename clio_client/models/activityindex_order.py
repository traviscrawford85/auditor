from typing import Literal, cast

ActivityindexOrder = Literal[
    "date(asc)",
    "date(desc)",
    "display_number(asc)",
    "display_number(desc)",
    "expense_category.name(asc)",
    "expense_category.name(desc)",
    "id(asc)",
    "id(desc)",
    "non_billable(asc)",
    "non_billable(desc)",
    "non_billable_total(asc)",
    "non_billable_total(desc)",
    "note(asc)",
    "note(desc)",
    "price(asc)",
    "price(desc)",
    "total(asc)",
    "total(desc)",
    "type(asc)",
    "type(desc)",
    "updated_at(asc)",
    "updated_at(desc)",
    "user.name(asc)",
    "user.name(desc)",
    "vendor.name(asc)",
    "vendor.name(desc)",
]

ACTIVITYINDEX_ORDER_VALUES: set[ActivityindexOrder] = {
    "date(asc)",
    "date(desc)",
    "display_number(asc)",
    "display_number(desc)",
    "expense_category.name(asc)",
    "expense_category.name(desc)",
    "id(asc)",
    "id(desc)",
    "non_billable(asc)",
    "non_billable(desc)",
    "non_billable_total(asc)",
    "non_billable_total(desc)",
    "note(asc)",
    "note(desc)",
    "price(asc)",
    "price(desc)",
    "total(asc)",
    "total(desc)",
    "type(asc)",
    "type(desc)",
    "updated_at(asc)",
    "updated_at(desc)",
    "user.name(asc)",
    "user.name(desc)",
    "vendor.name(asc)",
    "vendor.name(desc)",
}


def check_activityindex_order(value: str) -> ActivityindexOrder:
    if value in ACTIVITYINDEX_ORDER_VALUES:
        return cast(ActivityindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYINDEX_ORDER_VALUES!r}")
