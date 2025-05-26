from typing import Literal, cast

ClioCreatorBaseSubscriptionType = Literal["Attorney", "NonAttorney"]

CLIO_CREATOR_BASE_SUBSCRIPTION_TYPE_VALUES: set[ClioCreatorBaseSubscriptionType] = {
    "Attorney",
    "NonAttorney",
}


def check_clio_creator_base_subscription_type(value: str) -> ClioCreatorBaseSubscriptionType:
    if value in CLIO_CREATOR_BASE_SUBSCRIPTION_TYPE_VALUES:
        return cast(ClioCreatorBaseSubscriptionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLIO_CREATOR_BASE_SUBSCRIPTION_TYPE_VALUES!r}")
