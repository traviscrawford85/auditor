from typing import Literal, cast

ContactcreateFilesBodyDataAddressesItemName = Literal["Billing", "Home", "Other", "Work"]

CONTACTCREATE_FILES_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES: set[ContactcreateFilesBodyDataAddressesItemName] = {
    "Billing",
    "Home",
    "Other",
    "Work",
}


def check_contactcreate_files_body_data_addresses_item_name(value: str) -> ContactcreateFilesBodyDataAddressesItemName:
    if value in CONTACTCREATE_FILES_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactcreateFilesBodyDataAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_FILES_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
