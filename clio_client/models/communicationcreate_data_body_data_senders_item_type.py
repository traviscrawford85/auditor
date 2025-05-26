from typing import Literal, cast

CommunicationcreateDataBodyDataSendersItemType = Literal["Contact", "User"]

COMMUNICATIONCREATE_DATA_BODY_DATA_SENDERS_ITEM_TYPE_VALUES: set[CommunicationcreateDataBodyDataSendersItemType] = {
    "Contact",
    "User",
}


def check_communicationcreate_data_body_data_senders_item_type(
    value: str,
) -> CommunicationcreateDataBodyDataSendersItemType:
    if value in COMMUNICATIONCREATE_DATA_BODY_DATA_SENDERS_ITEM_TYPE_VALUES:
        return cast(CommunicationcreateDataBodyDataSendersItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_DATA_BODY_DATA_SENDERS_ITEM_TYPE_VALUES!r}"
    )
