from typing import Literal, cast

CommunicationindexType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATIONINDEX_TYPE_VALUES: set[CommunicationindexType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communicationindex_type(value: str) -> CommunicationindexType:
    if value in COMMUNICATIONINDEX_TYPE_VALUES:
        return cast(CommunicationindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONINDEX_TYPE_VALUES!r}")
