from typing import Literal, cast

CommunicationcreateDataBodyDataType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATIONCREATE_DATA_BODY_DATA_TYPE_VALUES: set[CommunicationcreateDataBodyDataType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communicationcreate_data_body_data_type(value: str) -> CommunicationcreateDataBodyDataType:
    if value in COMMUNICATIONCREATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(CommunicationcreateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_DATA_BODY_DATA_TYPE_VALUES!r}")
