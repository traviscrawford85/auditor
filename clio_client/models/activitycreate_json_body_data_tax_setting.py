from typing import Literal, cast

ActivitycreateJsonBodyDataTaxSetting = Literal["no_tax", "tax_1_and_tax_2", "tax_1_only", "tax_2_only"]

ACTIVITYCREATE_JSON_BODY_DATA_TAX_SETTING_VALUES: set[ActivitycreateJsonBodyDataTaxSetting] = {
    "no_tax",
    "tax_1_and_tax_2",
    "tax_1_only",
    "tax_2_only",
}


def check_activitycreate_json_body_data_tax_setting(value: str) -> ActivitycreateJsonBodyDataTaxSetting:
    if value in ACTIVITYCREATE_JSON_BODY_DATA_TAX_SETTING_VALUES:
        return cast(ActivitycreateJsonBodyDataTaxSetting, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYCREATE_JSON_BODY_DATA_TAX_SETTING_VALUES!r}")
