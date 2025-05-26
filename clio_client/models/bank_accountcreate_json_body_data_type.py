from typing import Literal, cast

BankAccountcreateJsonBodyDataType = Literal["Operating", "Trust"]

BANK_ACCOUNTCREATE_JSON_BODY_DATA_TYPE_VALUES: set[BankAccountcreateJsonBodyDataType] = {
    "Operating",
    "Trust",
}


def check_bank_accountcreate_json_body_data_type(value: str) -> BankAccountcreateJsonBodyDataType:
    if value in BANK_ACCOUNTCREATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(BankAccountcreateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNTCREATE_JSON_BODY_DATA_TYPE_VALUES!r}")
