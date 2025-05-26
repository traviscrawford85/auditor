from typing import Literal, cast

CommunicationcreateFilesBodyDataSendersItemType = Literal["Contact", "User"]

COMMUNICATIONCREATE_FILES_BODY_DATA_SENDERS_ITEM_TYPE_VALUES: set[CommunicationcreateFilesBodyDataSendersItemType] = {
    "Contact",
    "User",
}


def check_communicationcreate_files_body_data_senders_item_type(
    value: str,
) -> CommunicationcreateFilesBodyDataSendersItemType:
    if value in COMMUNICATIONCREATE_FILES_BODY_DATA_SENDERS_ITEM_TYPE_VALUES:
        return cast(CommunicationcreateFilesBodyDataSendersItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_FILES_BODY_DATA_SENDERS_ITEM_TYPE_VALUES!r}"
    )
