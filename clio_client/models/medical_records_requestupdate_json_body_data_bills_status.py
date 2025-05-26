from typing import Literal, cast

MedicalRecordsRequestupdateJsonBodyDataBillsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTUPDATE_JSON_BODY_DATA_BILLS_STATUS_VALUES: set[
    MedicalRecordsRequestupdateJsonBodyDataBillsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestupdate_json_body_data_bills_status(
    value: str,
) -> MedicalRecordsRequestupdateJsonBodyDataBillsStatus:
    if value in MEDICAL_RECORDS_REQUESTUPDATE_JSON_BODY_DATA_BILLS_STATUS_VALUES:
        return cast(MedicalRecordsRequestupdateJsonBodyDataBillsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTUPDATE_JSON_BODY_DATA_BILLS_STATUS_VALUES!r}"
    )
