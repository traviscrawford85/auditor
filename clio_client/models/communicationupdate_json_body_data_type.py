from typing import Literal, cast

CommunicationupdateJsonBodyDataType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATIONUPDATE_JSON_BODY_DATA_TYPE_VALUES: set[CommunicationupdateJsonBodyDataType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communicationupdate_json_body_data_type(value: str) -> CommunicationupdateJsonBodyDataType:
    if value in COMMUNICATIONUPDATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(CommunicationupdateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_JSON_BODY_DATA_TYPE_VALUES!r}")
