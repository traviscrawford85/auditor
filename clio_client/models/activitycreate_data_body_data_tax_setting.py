from typing import Literal, cast

ActivitycreateDataBodyDataTaxSetting = Literal["no_tax", "tax_1_and_tax_2", "tax_1_only", "tax_2_only"]

ACTIVITYCREATE_DATA_BODY_DATA_TAX_SETTING_VALUES: set[ActivitycreateDataBodyDataTaxSetting] = {
    "no_tax",
    "tax_1_and_tax_2",
    "tax_1_only",
    "tax_2_only",
}


def check_activitycreate_data_body_data_tax_setting(value: str) -> ActivitycreateDataBodyDataTaxSetting:
    if value in ACTIVITYCREATE_DATA_BODY_DATA_TAX_SETTING_VALUES:
        return cast(ActivitycreateDataBodyDataTaxSetting, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYCREATE_DATA_BODY_DATA_TAX_SETTING_VALUES!r}")
