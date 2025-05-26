from typing import Literal, cast

MedicalRecordsRequestcreateJsonBodyDataBillsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTCREATE_JSON_BODY_DATA_BILLS_STATUS_VALUES: set[
    MedicalRecordsRequestcreateJsonBodyDataBillsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestcreate_json_body_data_bills_status(
    value: str,
) -> MedicalRecordsRequestcreateJsonBodyDataBillsStatus:
    if value in MEDICAL_RECORDS_REQUESTCREATE_JSON_BODY_DATA_BILLS_STATUS_VALUES:
        return cast(MedicalRecordsRequestcreateJsonBodyDataBillsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTCREATE_JSON_BODY_DATA_BILLS_STATUS_VALUES!r}"
    )
