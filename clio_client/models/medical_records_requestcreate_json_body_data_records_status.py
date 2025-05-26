from typing import Literal, cast

MedicalRecordsRequestcreateJsonBodyDataRecordsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTCREATE_JSON_BODY_DATA_RECORDS_STATUS_VALUES: set[
    MedicalRecordsRequestcreateJsonBodyDataRecordsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestcreate_json_body_data_records_status(
    value: str,
) -> MedicalRecordsRequestcreateJsonBodyDataRecordsStatus:
    if value in MEDICAL_RECORDS_REQUESTCREATE_JSON_BODY_DATA_RECORDS_STATUS_VALUES:
        return cast(MedicalRecordsRequestcreateJsonBodyDataRecordsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTCREATE_JSON_BODY_DATA_RECORDS_STATUS_VALUES!r}"
    )
