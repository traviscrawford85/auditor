from typing import Literal, cast

CommunicationcreateJsonBodyDataReceiversItemType = Literal["Contact", "User"]

COMMUNICATIONCREATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES: set[CommunicationcreateJsonBodyDataReceiversItemType] = {
    "Contact",
    "User",
}


def check_communicationcreate_json_body_data_receivers_item_type(
    value: str,
) -> CommunicationcreateJsonBodyDataReceiversItemType:
    if value in COMMUNICATIONCREATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES:
        return cast(CommunicationcreateJsonBodyDataReceiversItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMMUNICATIONCREATE_JSON_BODY_DATA_RECEIVERS_ITEM_TYPE_VALUES!r}"
    )
