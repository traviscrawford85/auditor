from typing import Literal, cast

PracticeAreaindexOrder = Literal[
    "category(asc)", "category(desc)", "code(asc)", "code(desc)", "id(asc)", "id(desc)", "name(asc)", "name(desc)"
]

PRACTICE_AREAINDEX_ORDER_VALUES: set[PracticeAreaindexOrder] = {
    "category(asc)",
    "category(desc)",
    "code(asc)",
    "code(desc)",
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_practice_areaindex_order(value: str) -> PracticeAreaindexOrder:
    if value in PRACTICE_AREAINDEX_ORDER_VALUES:
        return cast(PracticeAreaindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRACTICE_AREAINDEX_ORDER_VALUES!r}")
