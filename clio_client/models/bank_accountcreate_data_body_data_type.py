from typing import Literal, cast

BankAccountcreateDataBodyDataType = Literal["Operating", "Trust"]

BANK_ACCOUNTCREATE_DATA_BODY_DATA_TYPE_VALUES: set[BankAccountcreateDataBodyDataType] = {
    "Operating",
    "Trust",
}


def check_bank_accountcreate_data_body_data_type(value: str) -> BankAccountcreateDataBodyDataType:
    if value in BANK_ACCOUNTCREATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(BankAccountcreateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNTCREATE_DATA_BODY_DATA_TYPE_VALUES!r}")
