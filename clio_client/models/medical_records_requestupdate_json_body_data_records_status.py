from typing import Literal, cast

MedicalRecordsRequestupdateJsonBodyDataRecordsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTUPDATE_JSON_BODY_DATA_RECORDS_STATUS_VALUES: set[
    MedicalRecordsRequestupdateJsonBodyDataRecordsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestupdate_json_body_data_records_status(
    value: str,
) -> MedicalRecordsRequestupdateJsonBodyDataRecordsStatus:
    if value in MEDICAL_RECORDS_REQUESTUPDATE_JSON_BODY_DATA_RECORDS_STATUS_VALUES:
        return cast(MedicalRecordsRequestupdateJsonBodyDataRecordsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTUPDATE_JSON_BODY_DATA_RECORDS_STATUS_VALUES!r}"
    )
