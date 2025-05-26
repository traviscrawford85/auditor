from typing import Literal, cast

CommunicationupdateFilesBodyDataSendersItemType = Literal["Contact", "User"]

COMMUNICATIONUPDATE_FILES_BODY_DATA_SENDERS_ITEM_TYPE_VALUES: set[CommunicationupdateFilesBodyDataSendersItemType] = {
    "Contact",
    "User",
}


def check_communicationupdate_files_body_data_senders_item_type(
    value: str,
) -> CommunicationupdateFilesBodyDataSendersItemType:
    if value in COMMUNICATIONUPDATE_FILES_BODY_DATA_SENDERS_ITEM_TYPE_VALUES:
        return cast(CommunicationupdateFilesBodyDataSendersItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_FILES_BODY_DATA_SENDERS_ITEM_TYPE_VALUES!r}"
    )
