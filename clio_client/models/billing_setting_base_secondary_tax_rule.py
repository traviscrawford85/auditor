from typing import Literal, cast

BillingSettingBaseSecondaryTaxRule = Literal["Post", "Pre"]

BILLING_SETTING_BASE_SECONDARY_TAX_RULE_VALUES: set[BillingSettingBaseSecondaryTaxRule] = {
    "Post",
    "Pre",
}


def check_billing_setting_base_secondary_tax_rule(value: str) -> BillingSettingBaseSecondaryTaxRule:
    if value in BILLING_SETTING_BASE_SECONDARY_TAX_RULE_VALUES:
        return cast(BillingSettingBaseSecondaryTaxRule, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLING_SETTING_BASE_SECONDARY_TAX_RULE_VALUES!r}")
