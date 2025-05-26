from typing import Literal, cast

ConversationindexOrder = Literal[
    "id(asc)", "id(desc)", "last_message_id(asc)", "last_message_id(desc)", "matter_id(asc)", "matter_id(desc)"
]

CONVERSATIONINDEX_ORDER_VALUES: set[ConversationindexOrder] = {
    "id(asc)",
    "id(desc)",
    "last_message_id(asc)",
    "last_message_id(desc)",
    "matter_id(asc)",
    "matter_id(desc)",
}


def check_conversationindex_order(value: str) -> ConversationindexOrder:
    if value in CONVERSATIONINDEX_ORDER_VALUES:
        return cast(ConversationindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATIONINDEX_ORDER_VALUES!r}")
