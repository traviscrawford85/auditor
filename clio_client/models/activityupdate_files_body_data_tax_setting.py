from typing import Literal, cast

ActivityupdateFilesBodyDataTaxSetting = Literal["no_tax", "tax_1_and_tax_2", "tax_1_only", "tax_2_only"]

ACTIVITYUPDATE_FILES_BODY_DATA_TAX_SETTING_VALUES: set[ActivityupdateFilesBodyDataTaxSetting] = {
    "no_tax",
    "tax_1_and_tax_2",
    "tax_1_only",
    "tax_2_only",
}


def check_activityupdate_files_body_data_tax_setting(value: str) -> ActivityupdateFilesBodyDataTaxSetting:
    if value in ACTIVITYUPDATE_FILES_BODY_DATA_TAX_SETTING_VALUES:
        return cast(ActivityupdateFilesBodyDataTaxSetting, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITYUPDATE_FILES_BODY_DATA_TAX_SETTING_VALUES!r}"
    )
