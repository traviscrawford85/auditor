from typing import Literal, cast

PolymorphicObjectBaseType = Literal[
    "CalendarEntry", "Contact", "ContactNote", "CreditMemo", "Matter", "MatterNote", "Payment", "Task", "User"
]

POLYMORPHIC_OBJECT_BASE_TYPE_VALUES: set[PolymorphicObjectBaseType] = {
    "CalendarEntry",
    "Contact",
    "ContactNote",
    "CreditMemo",
    "Matter",
    "MatterNote",
    "Payment",
    "Task",
    "User",
}


def check_polymorphic_object_base_type(value: str) -> PolymorphicObjectBaseType:
    if value in POLYMORPHIC_OBJECT_BASE_TYPE_VALUES:
        return cast(PolymorphicObjectBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLYMORPHIC_OBJECT_BASE_TYPE_VALUES!r}")
