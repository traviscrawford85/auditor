from typing import Literal, cast

ActivityupdateJsonBodyDataTaxSetting = Literal["no_tax", "tax_1_and_tax_2", "tax_1_only", "tax_2_only"]

ACTIVITYUPDATE_JSON_BODY_DATA_TAX_SETTING_VALUES: set[ActivityupdateJsonBodyDataTaxSetting] = {
    "no_tax",
    "tax_1_and_tax_2",
    "tax_1_only",
    "tax_2_only",
}


def check_activityupdate_json_body_data_tax_setting(value: str) -> ActivityupdateJsonBodyDataTaxSetting:
    if value in ACTIVITYUPDATE_JSON_BODY_DATA_TAX_SETTING_VALUES:
        return cast(ActivityupdateJsonBodyDataTaxSetting, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYUPDATE_JSON_BODY_DATA_TAX_SETTING_VALUES!r}")
