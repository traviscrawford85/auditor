from typing import Literal, cast

MedicalRecordsRequestBaseRecordsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUEST_BASE_RECORDS_STATUS_VALUES: set[MedicalRecordsRequestBaseRecordsStatus] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_request_base_records_status(value: str) -> MedicalRecordsRequestBaseRecordsStatus:
    if value in MEDICAL_RECORDS_REQUEST_BASE_RECORDS_STATUS_VALUES:
        return cast(MedicalRecordsRequestBaseRecordsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUEST_BASE_RECORDS_STATUS_VALUES!r}"
    )
