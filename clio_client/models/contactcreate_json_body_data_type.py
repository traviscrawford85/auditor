from typing import Literal, cast

ContactcreateJsonBodyDataType = Literal["Company", "Person"]

CONTACTCREATE_JSON_BODY_DATA_TYPE_VALUES: set[ContactcreateJsonBodyDataType] = {
    "Company",
    "Person",
}


def check_contactcreate_json_body_data_type(value: str) -> ContactcreateJsonBodyDataType:
    if value in CONTACTCREATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(ContactcreateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_JSON_BODY_DATA_TYPE_VALUES!r}")
