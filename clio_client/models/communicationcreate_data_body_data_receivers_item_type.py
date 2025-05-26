from typing import Literal, cast

CommunicationcreateDataBodyDataReceiversItemType = Literal["Contact", "User"]

COMMUNICATIONCREATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[CommunicationcreateDataBodyDataReceiversItemType] = {
    "Contact",
    "User",
}


def check_communicationcreate_data_body_data_receivers_item_type(
    value: str,
) -> CommunicationcreateDataBodyDataReceiversItemType:
    if value in COMMUNICATIONCREATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(CommunicationcreateDataBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_DATA_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
