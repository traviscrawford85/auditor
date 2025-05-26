from typing import Literal, cast

DamageupdateDataBodyDataDamageType = Literal["general", "other", "special"]

DAMAGEUPDATE_DATA_BODY_DATA_DAMAGE_TYPE_VALUES: set[DamageupdateDataBodyDataDamageType] = {
    "general",
    "other",
    "special",
}


def check_damageupdate_data_body_data_damage_type(value: str) -> DamageupdateDataBodyDataDamageType:
    if value in DAMAGEUPDATE_DATA_BODY_DATA_DAMAGE_TYPE_VALUES:
        return cast(DamageupdateDataBodyDataDamageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAMAGEUPDATE_DATA_BODY_DATA_DAMAGE_TYPE_VALUES!r}")
