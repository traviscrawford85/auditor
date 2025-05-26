from typing import Literal, cast

DamageupdateJsonBodyDataDamageType = Literal["general", "other", "special"]

DAMAGEUPDATE_JSON_BODY_DATA_DAMAGE_TYPE_VALUES: set[DamageupdateJsonBodyDataDamageType] = {
    "general",
    "other",
    "special",
}


def check_damageupdate_json_body_data_damage_type(value: str) -> DamageupdateJsonBodyDataDamageType:
    if value in DAMAGEUPDATE_JSON_BODY_DATA_DAMAGE_TYPE_VALUES:
        return cast(DamageupdateJsonBodyDataDamageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAMAGEUPDATE_JSON_BODY_DATA_DAMAGE_TYPE_VALUES!r}")
