from typing import Literal, cast

TrustRequestcreateDataBodyDataTrustType = Literal["client", "matter"]

TRUST_REQUESTCREATE_DATA_BODY_DATA_TRUST_TYPE_VALUES: set[TrustRequestcreateDataBodyDataTrustType] = {
    "client",
    "matter",
}


def check_trust_requestcreate_data_body_data_trust_type(value: str) -> TrustRequestcreateDataBodyDataTrustType:
    if value in TRUST_REQUESTCREATE_DATA_BODY_DATA_TRUST_TYPE_VALUES:
        return cast(TrustRequestcreateDataBodyDataTrustType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRUST_REQUESTCREATE_DATA_BODY_DATA_TRUST_TYPE_VALUES!r}"
    )
