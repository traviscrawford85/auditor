from typing import Literal, cast

CommunicationupdateDataBodyDataSendersItemType = Literal["Contact", "User"]

COMMUNICATIONUPDATE_DATA_BODY_DATA_SENDERS_ITEM_TYPE_VALUES: set[CommunicationupdateDataBodyDataSendersItemType] = {
    "Contact",
    "User",
}


def check_communicationupdate_data_body_data_senders_item_type(
    value: str,
) -> CommunicationupdateDataBodyDataSendersItemType:
    if value in COMMUNICATIONUPDATE_DATA_BODY_DATA_SENDERS_ITEM_TYPE_VALUES:
        return cast(CommunicationupdateDataBodyDataSendersItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_DATA_BODY_DATA_SENDERS_ITEM_TYPE_VALUES!r}"
    )
