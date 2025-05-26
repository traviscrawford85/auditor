from typing import Literal, cast

ActivitycreateFilesBodyDataTaxSetting = Literal["no_tax", "tax_1_and_tax_2", "tax_1_only", "tax_2_only"]

ACTIVITYCREATE_FILES_BODY_DATA_TAX_SETTING_VALUES: set[ActivitycreateFilesBodyDataTaxSetting] = {
    "no_tax",
    "tax_1_and_tax_2",
    "tax_1_only",
    "tax_2_only",
}


def check_activitycreate_files_body_data_tax_setting(value: str) -> ActivitycreateFilesBodyDataTaxSetting:
    if value in ACTIVITYCREATE_FILES_BODY_DATA_TAX_SETTING_VALUES:
        return cast(ActivitycreateFilesBodyDataTaxSetting, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITYCREATE_FILES_BODY_DATA_TAX_SETTING_VALUES!r}"
    )
