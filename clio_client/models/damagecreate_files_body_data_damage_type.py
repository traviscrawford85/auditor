from typing import Literal, cast

DamagecreateFilesBodyDataDamageType = Literal["general", "other", "special"]

DAMAGECREATE_FILES_BODY_DATA_DAMAGE_TYPE_VALUES: set[DamagecreateFilesBodyDataDamageType] = {
    "general",
    "other",
    "special",
}


def check_damagecreate_files_body_data_damage_type(value: str) -> DamagecreateFilesBodyDataDamageType:
    if value in DAMAGECREATE_FILES_BODY_DATA_DAMAGE_TYPE_VALUES:
        return cast(DamagecreateFilesBodyDataDamageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAMAGECREATE_FILES_BODY_DATA_DAMAGE_TYPE_VALUES!r}")
