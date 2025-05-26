from typing import Literal, cast

ActivityupdateDataBodyDataTaxSetting = Literal["no_tax", "tax_1_and_tax_2", "tax_1_only", "tax_2_only"]

ACTIVITYUPDATE_DATA_BODY_DATA_TAX_SETTING_VALUES: set[ActivityupdateDataBodyDataTaxSetting] = {
    "no_tax",
    "tax_1_and_tax_2",
    "tax_1_only",
    "tax_2_only",
}


def check_activityupdate_data_body_data_tax_setting(value: str) -> ActivityupdateDataBodyDataTaxSetting:
    if value in ACTIVITYUPDATE_DATA_BODY_DATA_TAX_SETTING_VALUES:
        return cast(ActivityupdateDataBodyDataTaxSetting, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYUPDATE_DATA_BODY_DATA_TAX_SETTING_VALUES!r}")
