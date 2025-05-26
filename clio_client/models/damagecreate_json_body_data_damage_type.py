from typing import Literal, cast

DamagecreateJsonBodyDataDamageType = Literal["general", "other", "special"]

DAMAGECREATE_JSON_BODY_DATA_DAMAGE_TYPE_VALUES: set[DamagecreateJsonBodyDataDamageType] = {
    "general",
    "other",
    "special",
}


def check_damagecreate_json_body_data_damage_type(value: str) -> DamagecreateJsonBodyDataDamageType:
    if value in DAMAGECREATE_JSON_BODY_DATA_DAMAGE_TYPE_VALUES:
        return cast(DamagecreateJsonBodyDataDamageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAMAGECREATE_JSON_BODY_DATA_DAMAGE_TYPE_VALUES!r}")
