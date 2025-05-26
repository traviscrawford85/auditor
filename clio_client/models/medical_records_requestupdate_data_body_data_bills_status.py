from typing import Literal, cast

MedicalRecordsRequestupdateDataBodyDataBillsStatus = Literal[
    "certified", "incomplete", "not_yet_requested", "received", "requested"
]

MEDICAL_RECORDS_REQUESTUPDATE_DATA_BODY_DATA_BILLS_STATUS_VALUES: set[
    MedicalRecordsRequestupdateDataBodyDataBillsStatus
] = {
    "certified",
    "incomplete",
    "not_yet_requested",
    "received",
    "requested",
}


def check_medical_records_requestupdate_data_body_data_bills_status(
    value: str,
) -> MedicalRecordsRequestupdateDataBodyDataBillsStatus:
    if value in MEDICAL_RECORDS_REQUESTUPDATE_DATA_BODY_DATA_BILLS_STATUS_VALUES:
        return cast(MedicalRecordsRequestupdateDataBodyDataBillsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEDICAL_RECORDS_REQUESTUPDATE_DATA_BODY_DATA_BILLS_STATUS_VALUES!r}"
    )
