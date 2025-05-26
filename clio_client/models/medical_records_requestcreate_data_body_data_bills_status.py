from typing import Literal, cast

MedicalRecordsRequestcreateDataBodyDataBillsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTCREATE_DATA_BODY_DATA_BILLS_STATUS_VALUES: set[
    MedicalRecordsRequestcreateDataBodyDataBillsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestcreate_data_body_data_bills_status(
    value: str,
) -> MedicalRecordsRequestcreateDataBodyDataBillsStatus:
    if value in MEDICAL_RECORDS_REQUESTCREATE_DATA_BODY_DATA_BILLS_STATUS_VALUES:
        return cast(MedicalRecordsRequestcreateDataBodyDataBillsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTCREATE_DATA_BODY_DATA_BILLS_STATUS_VALUES!r}"
    )
