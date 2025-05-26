from typing import Literal, cast

CommunicationcreateFilesBodyDataType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATIONCREATE_FILES_BODY_DATA_TYPE_VALUES: set[CommunicationcreateFilesBodyDataType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communicationcreate_files_body_data_type(value: str) -> CommunicationcreateFilesBodyDataType:
    if value in COMMUNICATIONCREATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(CommunicationcreateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_FILES_BODY_DATA_TYPE_VALUES!r}")
