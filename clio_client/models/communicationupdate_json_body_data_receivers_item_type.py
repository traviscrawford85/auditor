from typing import Literal, cast

CommunicationupdateJsonBodyDataReceiversItemType = Literal["Contact", "User"]

COMMUNICATIONUPDATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[CommunicationupdateJsonBodyDataReceiversItemType] = {
    "Contact",
    "User",
}


def check_communicationupdate_json_body_data_receivers_item_type(
    value: str,
) -> CommunicationupdateJsonBodyDataReceiversItemType:
    if value in COMMUNICATIONUPDATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(CommunicationupdateJsonBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
