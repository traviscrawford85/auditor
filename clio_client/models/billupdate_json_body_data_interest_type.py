from typing import Literal, cast

BillupdateJsonBodyDataInterestType = Literal["compound", "simple"]

BILLUPDATE_JSON_BODY_DATA_INTEREST_TYPE_VALUES: set[BillupdateJsonBodyDataInterestType] = {
    "compound",
    "simple",
}


def check_billupdate_json_body_data_interest_type(value: str) -> BillupdateJsonBodyDataInterestType:
    if value in BILLUPDATE_JSON_BODY_DATA_INTEREST_TYPE_VALUES:
        return cast(BillupdateJsonBodyDataInterestType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_JSON_BODY_DATA_INTEREST_TYPE_VALUES!r}")
