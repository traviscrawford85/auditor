from typing import Literal, cast

CommunicationupdateFilesBodyDataReceiversItemType = Literal["Contact", "User"]

COMMUNICATIONUPDATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[
    CommunicationupdateFilesBodyDataReceiversItemType
] = {
    "Contact",
    "User",
}


def check_communicationupdate_files_body_data_receivers_item_type(
    value: str,
) -> CommunicationupdateFilesBodyDataReceiversItemType:
    if value in COMMUNICATIONUPDATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(CommunicationupdateFilesBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
