from typing import Literal, cast

ConversationMessagecreateFilesBodyDataReceiversItemType = Literal["Contact", "User"]

CONVERSATION_MESSAGECREATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[
    ConversationMessagecreateFilesBodyDataReceiversItemType
] = {
    "Contact",
    "User",
}


def check_conversation_messagecreate_files_body_data_receivers_item_type(
    value: str,
) -> ConversationMessagecreateFilesBodyDataReceiversItemType:
    if value in CONVERSATION_MESSAGECREATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(ConversationMessagecreateFilesBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERSATION_MESSAGECREATE_FILES_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
