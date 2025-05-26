from typing import Literal, cast

ActivityDescriptionRateBaseHierarchy = Literal["Activity", "Client", "Default", "Matter"]

ACTIVITY_DESCRIPTION_RATE_BASE_HIERARCHY_VALUES: set[ActivityDescriptionRateBaseHierarchy] = {
    "Activity",
    "Client",
    "Default",
    "Matter",
}


def check_activity_description_rate_base_hierarchy(value: str) -> ActivityDescriptionRateBaseHierarchy:
    if value in ACTIVITY_DESCRIPTION_RATE_BASE_HIERARCHY_VALUES:
        return cast(ActivityDescriptionRateBaseHierarchy, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTION_RATE_BASE_HIERARCHY_VALUES!r}")
