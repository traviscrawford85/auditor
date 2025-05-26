# Adapter for damagelist
from clio_sdk.models.damagelist import DamagelistIn, DamagelistOut, DamagelistUpdate, DamagelistDb
from clio_client.models.damage_list import DamageList

def convert_sdk_to_damagelistout(src: DamageList) -> DamagelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return DamagelistOut(**src.model_dump())

def convert_damagelistin_to_sdk(src: DamagelistIn) -> DamageList:
    """Converts a clio_sdk model to clio_client model."""
    return DamageList(**src.model_dump())
