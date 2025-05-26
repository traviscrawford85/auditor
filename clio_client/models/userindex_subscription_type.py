from typing import Literal, cast

UserindexSubscriptionType = Literal["attorney", "nonattorney"]

USERINDEX_SUBSCRIPTION_TYPE_VALUES: set[UserindexSubscriptionType] = {
    "attorney",
    "nonattorney",
}


def check_userindex_subscription_type(value: str) -> UserindexSubscriptionType:
    if value in USERINDEX_SUBSCRIPTION_TYPE_VALUES:
        return cast(UserindexSubscriptionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USERINDEX_SUBSCRIPTION_TYPE_VALUES!r}")
