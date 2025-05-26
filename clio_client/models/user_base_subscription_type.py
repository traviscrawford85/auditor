from typing import Literal, cast

UserBaseSubscriptionType = Literal["Attorney", "NonAttorney"]

USER_BASE_SUBSCRIPTION_TYPE_VALUES: set[UserBaseSubscriptionType] = {
    "Attorney",
    "NonAttorney",
}


def check_user_base_subscription_type(value: str) -> UserBaseSubscriptionType:
    if value in USER_BASE_SUBSCRIPTION_TYPE_VALUES:
        return cast(UserBaseSubscriptionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_BASE_SUBSCRIPTION_TYPE_VALUES!r}")
