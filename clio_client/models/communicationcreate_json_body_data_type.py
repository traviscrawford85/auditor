from typing import Literal, cast

CommunicationcreateJsonBodyDataType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATIONCREATE_JSON_BODY_DATA_TYPE_VALUES: set[CommunicationcreateJsonBodyDataType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communicationcreate_json_body_data_type(value: str) -> CommunicationcreateJsonBodyDataType:
    if value in COMMUNICATIONCREATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(CommunicationcreateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_JSON_BODY_DATA_TYPE_VALUES!r}")
