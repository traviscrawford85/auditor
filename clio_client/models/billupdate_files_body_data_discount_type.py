from typing import Literal, cast

BillupdateFilesBodyDataDiscountType = Literal["money", "percentage"]

BILLUPDATE_FILES_BODY_DATA_DISCOUNT_TYPE_VALUES: set[BillupdateFilesBodyDataDiscountType] = {
    "money",
    "percentage",
}


def check_billupdate_files_body_data_discount_type(value: str) -> BillupdateFilesBodyDataDiscountType:
    if value in BILLUPDATE_FILES_BODY_DATA_DISCOUNT_TYPE_VALUES:
        return cast(BillupdateFilesBodyDataDiscountType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_FILES_BODY_DATA_DISCOUNT_TYPE_VALUES!r}")
