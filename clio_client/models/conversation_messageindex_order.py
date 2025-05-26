from typing import Literal, cast

ConversationMessageindexOrder = Literal["id(asc)", "id(desc)"]

CONVERSATION_MESSAGEINDEX_ORDER_VALUES: set[ConversationMessageindexOrder] = {
    "id(asc)",
    "id(desc)",
}


def check_conversation_messageindex_order(value: str) -> ConversationMessageindexOrder:
    if value in CONVERSATION_MESSAGEINDEX_ORDER_VALUES:
        return cast(ConversationMessageindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_MESSAGEINDEX_ORDER_VALUES!r}")
