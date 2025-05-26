from typing import Literal, cast

DamagecreateDataBodyDataDamageType = Literal["general", "other", "special"]

DAMAGECREATE_DATA_BODY_DATA_DAMAGE_TYPE_VALUES: set[DamagecreateDataBodyDataDamageType] = {
    "general",
    "other",
    "special",
}


def check_damagecreate_data_body_data_damage_type(value: str) -> DamagecreateDataBodyDataDamageType:
    if value in DAMAGECREATE_DATA_BODY_DATA_DAMAGE_TYPE_VALUES:
        return cast(DamagecreateDataBodyDataDamageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAMAGECREATE_DATA_BODY_DATA_DAMAGE_TYPE_VALUES!r}")
