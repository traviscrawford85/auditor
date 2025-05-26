from typing import Literal, cast

MedicalRecordsRequestBaseBillsStatus = Literal["certified", "incomplete", "not_yet_requested", "received", "requested"]

MEDICAL_RECORDS_REQUEST_BASE_BILLS_STATUS_VALUES: set[MedicalRecordsRequestBaseBillsStatus] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_request_base_bills_status(value: str) -> MedicalRecordsRequestBaseBillsStatus:
    if value in MEDICAL_RECORDS_REQUEST_BASE_BILLS_STATUS_VALUES:
        return cast(MedicalRecordsRequestBaseBillsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUEST_BASE_BILLS_STATUS_VALUES!r}")
