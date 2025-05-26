from typing import Literal, cast

ConversationMessagecreateJsonBodyDataReceiversItemType = Literal["Contact", "User"]

CONVERSATION_MESSAGECREATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[
    ConversationMessagecreateJsonBodyDataReceiversItemType
] = {
    "Contact",
    "User",
}


def check_conversation_messagecreate_json_body_data_receivers_item_type(
    value: str,
) -> ConversationMessagecreateJsonBodyDataReceiversItemType:
    if value in CONVERSATION_MESSAGECREATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(ConversationMessagecreateJsonBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERSATION_MESSAGECREATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
