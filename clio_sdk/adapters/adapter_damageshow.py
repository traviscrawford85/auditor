# Adapter for damageshow
from clio_sdk.models.damageshow import DamageshowIn, DamageshowOut, DamageshowUpdate, DamageshowDb
from clio_client.models import damage_show

def convert_sdk_to_damageshowout(src: damage_show) -> DamageshowOut:
    return DamageshowOut(**src.dict())

def convert_damageshowin_to_sdk(src: DamageshowIn) -> damage_show:
    return damage_show(**src.dict())
