from typing import Literal, cast

ClioPaymentsLinkcreateDataBodyDataSubjectType = Literal["BankAccount", "Bill", "Contact"]

CLIO_PAYMENTS_LINKCREATE_DATA_BODY_DATA_SUBJECT_TYPE_VALUES: set[ClioPaymentsLinkcreateDataBodyDataSubjectType] = {
    "BankAccount",
    "Bill",
    "Contact",
}


def check_clio_payments_linkcreate_data_body_data_subject_type(
    value: str,
) -> ClioPaymentsLinkcreateDataBodyDataSubjectType:
    if value in CLIO_PAYMENTS_LINKCREATE_DATA_BODY_DATA_SUBJECT_TYPE_VALUES:
        return cast(ClioPaymentsLinkcreateDataBodyDataSubjectType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLIO_PAYMENTS_LINKCREATE_DATA_BODY_DATA_SUBJECT_TYPE_VALUES!r}"
    )
