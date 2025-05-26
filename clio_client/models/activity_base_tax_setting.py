from typing import Literal, cast

ActivityBaseTaxSetting = Literal["no_tax", "tax_1_and_tax_2", "tax_1_only", "tax_2_only"]

ACTIVITY_BASE_TAX_SETTING_VALUES: set[ActivityBaseTaxSetting] = {
    "no_tax",
    "tax_1_and_tax_2",
    "tax_1_only",
    "tax_2_only",
}


def check_activity_base_tax_setting(value: str) -> ActivityBaseTaxSetting:
    if value in ACTIVITY_BASE_TAX_SETTING_VALUES:
        return cast(ActivityBaseTaxSetting, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_BASE_TAX_SETTING_VALUES!r}")
