from typing import Literal, cast

ContactupdateJsonBodyDataType = Literal["Company", "Person"]

CONTACTUPDATE_JSON_BODY_DATA_TYPE_VALUES: set[ContactupdateJsonBodyDataType] = {
    "Company",
    "Person",
}


def check_contactupdate_json_body_data_type(value: str) -> ContactupdateJsonBodyDataType:
    if value in CONTACTUPDATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(ContactupdateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_JSON_BODY_DATA_TYPE_VALUES!r}")
