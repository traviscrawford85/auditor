from typing import Literal, cast

ClioPaymentsLinkcreateJsonBodyDataSubjectType = Literal["BankAccount", "Bill", "Contact"]

CLIO_PAYMENTS_LINKCREATE_JSON_BODY_DATA_SUBJECT_TYPE_VALUES: set[ClioPaymentsLinkcreateJsonBodyDataSubjectType] = {
    "BankAccount",
    "Bill",
    "Contact",
}


def check_clio_payments_linkcreate_json_body_data_subject_type(
    value: str,
) -> ClioPaymentsLinkcreateJsonBodyDataSubjectType:
    if value in CLIO_PAYMENTS_LINKCREATE_JSON_BODY_DATA_SUBJECT_TYPE_VALUES:
        return cast(ClioPaymentsLinkcreateJsonBodyDataSubjectType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLIO_PAYMENTS_LINKCREATE_JSON_BODY_DATA_SUBJECT_TYPE_VALUES!r}"
    )
