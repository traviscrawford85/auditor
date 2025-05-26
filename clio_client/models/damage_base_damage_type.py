from typing import Literal, cast

DamageBaseDamageType = Literal["general", "other", "special"]

DAMAGE_BASE_DAMAGE_TYPE_VALUES: set[DamageBaseDamageType] = {
    "general",
    "other",
    "special",
}


def check_damage_base_damage_type(value: str) -> DamageBaseDamageType:
    if value in DAMAGE_BASE_DAMAGE_TYPE_VALUES:
        return cast(DamageBaseDamageType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAMAGE_BASE_DAMAGE_TYPE_VALUES!r}")
