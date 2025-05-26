from typing import Literal, cast

CommunicationBaseType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATION_BASE_TYPE_VALUES: set[CommunicationBaseType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communication_base_type(value: str) -> CommunicationBaseType:
    if value in COMMUNICATION_BASE_TYPE_VALUES:
        return cast(CommunicationBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATION_BASE_TYPE_VALUES!r}")
