from typing import Literal, cast

DamageupdateFilesBodyDataDamageType = Literal["general", "other", "special"]

DAMAGEUPDATE_FILES_BODY_DATA_DAMAGE_TYPE_VALUES: set[DamageupdateFilesBodyDataDamageType] = {
    "general",
    "other",
    "special",
}


def check_damageupdate_files_body_data_damage_type(value: str) -> DamageupdateFilesBodyDataDamageType:
    if value in DAMAGEUPDATE_FILES_BODY_DATA_DAMAGE_TYPE_VALUES:
        return cast(DamageupdateFilesBodyDataDamageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAMAGEUPDATE_FILES_BODY_DATA_DAMAGE_TYPE_VALUES!r}")
