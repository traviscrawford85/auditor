from typing import Literal, cast

MedicalRecordsRequestcreateDataBodyDataRecordsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTCREATE_DATA_BODY_DATA_RECORDS_STATUS_VALUES: set[
    MedicalRecordsRequestcreateDataBodyDataRecordsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestcreate_data_body_data_records_status(
    value: str,
) -> MedicalRecordsRequestcreateDataBodyDataRecordsStatus:
    if value in MEDICAL_RECORDS_REQUESTCREATE_DATA_BODY_DATA_RECORDS_STATUS_VALUES:
        return cast(MedicalRecordsRequestcreateDataBodyDataRecordsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTCREATE_DATA_BODY_DATA_RECORDS_STATUS_VALUES!r}"
    )
