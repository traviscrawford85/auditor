from typing import Literal, cast

CommunicationcreateJsonBodyDataSendersItemType = Literal["Contact", "User"]

COMMUNICATIONCREATE_JSON_BODY_DATA_SENDERS_ITEM_TYPE_VALUES: set[CommunicationcreateJsonBodyDataSendersItemType] = {
    "Contact",
    "User",
}


def check_communicationcreate_json_body_data_senders_item_type(
    value: str,
) -> CommunicationcreateJsonBodyDataSendersItemType:
    if value in COMMUNICATIONCREATE_JSON_BODY_DATA_SENDERS_ITEM_TYPE_VALUES:
        return cast(CommunicationcreateJsonBodyDataSendersItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_JSON_BODY_DATA_SENDERS_ITEM_TYPE_VALUES!r}"
    )
