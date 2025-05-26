from typing import Literal, cast

MedicalRecordsRequestupdateDataBodyDataRecordsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTUPDATE_DATA_BODY_DATA_RECORDS_STATUS_VALUES: set[
    MedicalRecordsRequestupdateDataBodyDataRecordsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestupdate_data_body_data_records_status(
    value: str,
) -> MedicalRecordsRequestupdateDataBodyDataRecordsStatus:
    if value in MEDICAL_RECORDS_REQUESTUPDATE_DATA_BODY_DATA_RECORDS_STATUS_VALUES:
        return cast(MedicalRecordsRequestupdateDataBodyDataRecordsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTUPDATE_DATA_BODY_DATA_RECORDS_STATUS_VALUES!r}"
    )
