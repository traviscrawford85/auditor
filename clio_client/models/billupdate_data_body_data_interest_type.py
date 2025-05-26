from typing import Literal, cast

BillupdateDataBodyDataInterestType = Literal["compound", "simple"]

BILLUPDATE_DATA_BODY_DATA_INTEREST_TYPE_VALUES: set[BillupdateDataBodyDataInterestType] = {
    "compound",
    "simple",
}


def check_billupdate_data_body_data_interest_type(value: str) -> BillupdateDataBodyDataInterestType:
    if value in BILLUPDATE_DATA_BODY_DATA_INTEREST_TYPE_VALUES:
        return cast(BillupdateDataBodyDataInterestType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_DATA_BODY_DATA_INTEREST_TYPE_VALUES!r}")
