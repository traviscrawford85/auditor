from typing import Literal, cast

LineItemupdateFilesBodyDataKind = Literal["Expense", "Product", "Service"]

LINE_ITEMUPDATE_FILES_BODY_DATA_KIND_VALUES: set[LineItemupdateFilesBodyDataKind] = {
    "Expense",
    "Product",
    "Service",
}


def check_line_itemupdate_files_body_data_kind(value: str) -> LineItemupdateFilesBodyDataKind:
    if value in LINE_ITEMUPDATE_FILES_BODY_DATA_KIND_VALUES:
        return cast(LineItemupdateFilesBodyDataKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINE_ITEMUPDATE_FILES_BODY_DATA_KIND_VALUES!r}")
