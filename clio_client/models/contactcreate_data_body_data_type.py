from typing import Literal, cast

ContactcreateDataBodyDataType = Literal["Company", "Person"]

CONTACTCREATE_DATA_BODY_DATA_TYPE_VALUES: set[ContactcreateDataBodyDataType] = {
    "Company",
    "Person",
}


def check_contactcreate_data_body_data_type(value: str) -> ContactcreateDataBodyDataType:
    if value in CONTACTCREATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(ContactcreateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_DATA_BODY_DATA_TYPE_VALUES!r}")
