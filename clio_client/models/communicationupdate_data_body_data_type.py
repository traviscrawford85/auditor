from typing import Literal, cast

CommunicationupdateDataBodyDataType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATIONUPDATE_DATA_BODY_DATA_TYPE_VALUES: set[CommunicationupdateDataBodyDataType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communicationupdate_data_body_data_type(value: str) -> CommunicationupdateDataBodyDataType:
    if value in COMMUNICATIONUPDATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(CommunicationupdateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_DATA_BODY_DATA_TYPE_VALUES!r}")
