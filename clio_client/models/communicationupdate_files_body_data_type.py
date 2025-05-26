from typing import Literal, cast

CommunicationupdateFilesBodyDataType = Literal["EmailCommunication", "PhoneCommunication"]

COMMUNICATIONUPDATE_FILES_BODY_DATA_TYPE_VALUES: set[CommunicationupdateFilesBodyDataType] = {
    "EmailCommunication",
    "PhoneCommunication",
}


def check_communicationupdate_files_body_data_type(value: str) -> CommunicationupdateFilesBodyDataType:
    if value in COMMUNICATIONUPDATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(CommunicationupdateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_FILES_BODY_DATA_TYPE_VALUES!r}")
