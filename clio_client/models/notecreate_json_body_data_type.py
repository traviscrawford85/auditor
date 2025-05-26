from typing import Literal, cast

NotecreateJsonBodyDataType = Literal["Contact", "Matter"]

NOTECREATE_JSON_BODY_DATA_TYPE_VALUES: set[NotecreateJsonBodyDataType] = {
    "Contact",
    "Matter",
}


def check_notecreate_json_body_data_type(value: str) -> NotecreateJsonBodyDataType:
    if value in NOTECREATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(NotecreateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTECREATE_JSON_BODY_DATA_TYPE_VALUES!r}")
