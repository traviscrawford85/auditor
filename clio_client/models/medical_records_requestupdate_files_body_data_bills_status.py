from typing import Literal, cast

MedicalRecordsRequestupdateFilesBodyDataBillsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTUPDATE_FILES_BODY_DATA_BILLS_STATUS_VALUES: set[
    MedicalRecordsRequestupdateFilesBodyDataBillsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestupdate_files_body_data_bills_status(
    value: str,
) -> MedicalRecordsRequestupdateFilesBodyDataBillsStatus:
    if value in MEDICAL_RECORDS_REQUESTUPDATE_FILES_BODY_DATA_BILLS_STATUS_VALUES:
        return cast(MedicalRecordsRequestupdateFilesBodyDataBillsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTUPDATE_FILES_BODY_DATA_BILLS_STATUS_VALUES!r}"
    )
