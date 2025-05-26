from typing import Literal, cast

ContactupdateFilesBodyDataAddressesItemName = Literal["Billing", "Home", "Other", "Work"]

CONTACTUPDATE_FILES_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES: set[ContactupdateFilesBodyDataAddressesItemName] = {
    "Billing",
    "Home",
    "Other",
    "Work",
}


def check_contactupdate_files_body_data_addresses_item_name(value: str) -> ContactupdateFilesBodyDataAddressesItemName:
    if value in CONTACTUPDATE_FILES_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES:
        return cast(ContactupdateFilesBodyDataAddressesItemName, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_FILES_BODY_DATA_ADDRESSES_ITEM_NAME_VALUES!r}"
    )
