# Adapter for damagelist
from clio_sdk.models.damagelist import DamagelistIn, DamagelistOut, DamagelistUpdate, DamagelistDb
from clio_client.models import damage_list

def convert_sdk_to_damagelistout(src: damage_list) -> DamagelistOut:
    return DamagelistOut(**src.dict())

def convert_damagelistin_to_sdk(src: DamagelistIn) -> damage_list:
    return damage_list(**src.dict())
