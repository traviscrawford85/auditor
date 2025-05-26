from typing import Literal, cast

ActivityDescriptionindexType = Literal["clio", "utbms"]

ACTIVITY_DESCRIPTIONINDEX_TYPE_VALUES: set[ActivityDescriptionindexType] = {
    "clio",
    "utbms",
}


def check_activity_descriptionindex_type(value: str) -> ActivityDescriptionindexType:
    if value in ACTIVITY_DESCRIPTIONINDEX_TYPE_VALUES:
        return cast(ActivityDescriptionindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTIONINDEX_TYPE_VALUES!r}")
