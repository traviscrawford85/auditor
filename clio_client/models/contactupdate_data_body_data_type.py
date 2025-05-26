from typing import Literal, cast

ContactupdateDataBodyDataType = Literal["Company", "Person"]

CONTACTUPDATE_DATA_BODY_DATA_TYPE_VALUES: set[ContactupdateDataBodyDataType] = {
    "Company",
    "Person",
}


def check_contactupdate_data_body_data_type(value: str) -> ContactupdateDataBodyDataType:
    if value in CONTACTUPDATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(ContactupdateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_DATA_BODY_DATA_TYPE_VALUES!r}")
