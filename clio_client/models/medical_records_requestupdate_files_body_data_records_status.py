from typing import Literal, cast

MedicalRecordsRequestupdateFilesBodyDataRecordsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTUPDATE_FILES_BODY_DATA_RECORDS_STATUS_VALUES: set[
    MedicalRecordsRequestupdateFilesBodyDataRecordsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestupdate_files_body_data_records_status(
    value: str,
) -> MedicalRecordsRequestupdateFilesBodyDataRecordsStatus:
    if value in MEDICAL_RECORDS_REQUESTUPDATE_FILES_BODY_DATA_RECORDS_STATUS_VALUES:
        return cast(MedicalRecordsRequestupdateFilesBodyDataRecordsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTUPDATE_FILES_BODY_DATA_RECORDS_STATUS_VALUES!r}"
    )
