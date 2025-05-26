from typing import Literal, cast

BillupdateFilesBodyDataInterestType = Literal["compound", "simple"]

BILLUPDATE_FILES_BODY_DATA_INTEREST_TYPE_VALUES: set[BillupdateFilesBodyDataInterestType] = {
    "compound",
    "simple",
}


def check_billupdate_files_body_data_interest_type(value: str) -> BillupdateFilesBodyDataInterestType:
    if value in BILLUPDATE_FILES_BODY_DATA_INTEREST_TYPE_VALUES:
        return cast(BillupdateFilesBodyDataInterestType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_FILES_BODY_DATA_INTEREST_TYPE_VALUES!r}")
