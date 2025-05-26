# Adapter for damageshow
from clio_sdk.models.damageshow import DamageshowIn, DamageshowOut, DamageshowUpdate, DamageshowDb
from clio_client.models.damage_show import DamageShow

def convert_sdk_to_damageshowout(src: DamageShow) -> DamageshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return DamageshowOut(**src.model_dump())

def convert_damageshowin_to_sdk(src: DamageshowIn) -> DamageShow:
    """Converts a clio_sdk model to clio_client model."""
    return DamageShow(**src.model_dump())
