from typing import Literal, cast

JurisdictionsToTriggerindexOrder = Literal["description(asc)", "description(desc)", "id(asc)", "id(desc)"]

JURISDICTIONS_TO_TRIGGERINDEX_ORDER_VALUES: set[JurisdictionsToTriggerindexOrder] = {
    "description(asc)",
    "description(desc)",
    "id(asc)",
    "id(desc)",
}


def check_jurisdictions_to_triggerindex_order(value: str) -> JurisdictionsToTriggerindexOrder:
    if value in JURISDICTIONS_TO_TRIGGERINDEX_ORDER_VALUES:
        return cast(JurisdictionsToTriggerindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JURISDICTIONS_TO_TRIGGERINDEX_ORDER_VALUES!r}")
