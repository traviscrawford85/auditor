from typing import Literal, cast

BankAccountcreateFilesBodyDataType = Literal["Operating", "Trust"]

BANK_ACCOUNTCREATE_FILES_BODY_DATA_TYPE_VALUES: set[BankAccountcreateFilesBodyDataType] = {
    "Operating",
    "Trust",
}


def check_bank_accountcreate_files_body_data_type(value: str) -> BankAccountcreateFilesBodyDataType:
    if value in BANK_ACCOUNTCREATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(BankAccountcreateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNTCREATE_FILES_BODY_DATA_TYPE_VALUES!r}")
