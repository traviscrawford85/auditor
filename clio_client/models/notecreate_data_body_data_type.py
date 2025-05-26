from typing import Literal, cast

NotecreateDataBodyDataType = Literal["Contact", "Matter"]

NOTECREATE_DATA_BODY_DATA_TYPE_VALUES: set[NotecreateDataBodyDataType] = {
    "Contact",
    "Matter",
}


def check_notecreate_data_body_data_type(value: str) -> NotecreateDataBodyDataType:
    if value in NOTECREATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(NotecreateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTECREATE_DATA_BODY_DATA_TYPE_VALUES!r}")
