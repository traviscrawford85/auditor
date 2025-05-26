from typing import Literal, cast

CommunicationupdateJsonBodyDataSendersItemType = Literal["Contact", "User"]

COMMUNICATIONUPDATE_JSON_BODY_DATA_SENDERS_ITEM_TYPE_VALUES: set[CommunicationupdateJsonBodyDataSendersItemType] = {
    "Contact",
    "User",
}


def check_communicationupdate_json_body_data_senders_item_type(
    value: str,
) -> CommunicationupdateJsonBodyDataSendersItemType:
    if value in COMMUNICATIONUPDATE_JSON_BODY_DATA_SENDERS_ITEM_TYPE_VALUES:
        return cast(CommunicationupdateJsonBodyDataSendersItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_JSON_BODY_DATA_SENDERS_ITEM_TYPE_VALUES!r}"
    )
