from typing import Literal, cast

MedicalRecordsRequestcreateFilesBodyDataBillsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTCREATE_FILES_BODY_DATA_BILLS_STATUS_VALUES: set[
    MedicalRecordsRequestcreateFilesBodyDataBillsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestcreate_files_body_data_bills_status(
    value: str,
) -> MedicalRecordsRequestcreateFilesBodyDataBillsStatus:
    if value in MEDICAL_RECORDS_REQUESTCREATE_FILES_BODY_DATA_BILLS_STATUS_VALUES:
        return cast(MedicalRecordsRequestcreateFilesBodyDataBillsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTCREATE_FILES_BODY_DATA_BILLS_STATUS_VALUES!r}"
    )
