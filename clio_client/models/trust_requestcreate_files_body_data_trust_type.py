from typing import Literal, cast

TrustRequestcreateFilesBodyDataTrustType = Literal["client", "matter"]

TRUST_REQUESTCREATE_FILES_BODY_DATA_TRUST_TYPE_VALUES: set[TrustRequestcreateFilesBodyDataTrustType] = {
    "client",
    "matter",
}


def check_trust_requestcreate_files_body_data_trust_type(value: str) -> TrustRequestcreateFilesBodyDataTrustType:
    if value in TRUST_REQUESTCREATE_FILES_BODY_DATA_TRUST_TYPE_VALUES:
        return cast(TrustRequestcreateFilesBodyDataTrustType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRUST_REQUESTCREATE_FILES_BODY_DATA_TRUST_TYPE_VALUES!r}"
    )
