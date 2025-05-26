from typing import Literal, cast

MedicalRecordsRequestcreateFilesBodyDataRecordsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTCREATE_FILES_BODY_DATA_RECORDS_STATUS_VALUES: set[
    MedicalRecordsRequestcreateFilesBodyDataRecordsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestcreate_files_body_data_records_status(
    value: str,
) -> MedicalRecordsRequestcreateFilesBodyDataRecordsStatus:
    if value in MEDICAL_RECORDS_REQUESTCREATE_FILES_BODY_DATA_RECORDS_STATUS_VALUES:
        return cast(MedicalRecordsRequestcreateFilesBodyDataRecordsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTCREATE_FILES_BODY_DATA_RECORDS_STATUS_VALUES!r}"
    )
