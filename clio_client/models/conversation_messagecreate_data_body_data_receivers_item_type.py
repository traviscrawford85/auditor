from typing import Literal, cast

ConversationMessagecreateDataBodyDataReceiversItemType = Literal["Contact", "User"]

CONVERSATION_MESSAGECREATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[
    ConversationMessagecreateDataBodyDataReceiversItemType
] = {
    "Contact",
    "User",
}


def check_conversation_messagecreate_data_body_data_receivers_item_type(
    value: str,
) -> ConversationMessagecreateDataBodyDataReceiversItemType:
    if value in CONVERSATION_MESSAGECREATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(ConversationMessagecreateDataBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERSATION_MESSAGECREATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
