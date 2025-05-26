from typing import Literal, cast

TrustRequestcreateJsonBodyDataTrustType = Literal["client", "matter"]

TRUST_REQUESTCREATE_JSON_BODY_DATA_TRUST_TYPE_VALUES: set[TrustRequestcreateJsonBodyDataTrustType] = {
    "client",
    "matter",
}


def check_trust_requestcreate_json_body_data_trust_type(value: str) -> TrustRequestcreateJsonBodyDataTrustType:
    if value in TRUST_REQUESTCREATE_JSON_BODY_DATA_TRUST_TYPE_VALUES:
        return cast(TrustRequestcreateJsonBodyDataTrustType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRUST_REQUESTCREATE_JSON_BODY_DATA_TRUST_TYPE_VALUES!r}"
    )
