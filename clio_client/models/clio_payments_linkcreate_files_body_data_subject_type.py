from typing import Literal, cast

ClioPaymentsLinkcreateFilesBodyDataSubjectType = Literal["BankAccount", "Bill", "Contact"]

CLIO_PAYMENTS_LINKCREATE_FILES_BODY_DATA_SUBJECT_TYPE_VALUES: set[ClioPaymentsLinkcreateFilesBodyDataSubjectType] = {
    "BankAccount",
    "Bill",
    "Contact",
}


def check_clio_payments_linkcreate_files_body_data_subject_type(
    value: str,
) -> ClioPaymentsLinkcreateFilesBodyDataSubjectType:
    if value in CLIO_PAYMENTS_LINKCREATE_FILES_BODY_DATA_SUBJECT_TYPE_VALUES:
        return cast(ClioPaymentsLinkcreateFilesBodyDataSubjectType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLIO_PAYMENTS_LINKCREATE_FILES_BODY_DATA_SUBJECT_TYPE_VALUES!r}"
    )
