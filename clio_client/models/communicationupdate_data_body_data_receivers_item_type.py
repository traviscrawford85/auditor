from typing import Literal, cast

CommunicationupdateDataBodyDataReceiversItemType = Literal["Contact", "User"]

COMMUNICATIONUPDATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[CommunicationupdateDataBodyDataReceiversItemType] = {
    "Contact",
    "User",
}


def check_communicationupdate_data_body_data_receivers_item_type(
    value: str,
) -> CommunicationupdateDataBodyDataReceiversItemType:
    if value in COMMUNICATIONUPDATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(CommunicationupdateDataBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONUPDATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
