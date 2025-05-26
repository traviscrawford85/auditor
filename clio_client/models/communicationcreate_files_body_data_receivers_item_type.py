from typing import Literal, cast

CommunicationcreateFilesBodyDataReceiversItemType = Literal["Contact", "User"]

COMMUNICATIONCREATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[
    CommunicationcreateFilesBodyDataReceiversItemType
] = {
    "Contact",
    "User",
}


def check_communicationcreate_files_body_data_receivers_item_type(
    value: str,
) -> CommunicationcreateFilesBodyDataReceiversItemType:
    if value in COMMUNICATIONCREATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(CommunicationcreateFilesBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
