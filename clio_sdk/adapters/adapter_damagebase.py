# Adapter for damagebase
from clio_sdk.models.damagebase import DamagebaseIn, DamagebaseOut, DamagebaseUpdate, DamagebaseDb
from clio_client.models import damage

def convert_sdk_to_damagebaseout(src: damage) -> DamagebaseOut:
    return DamagebaseOut(**src.dict())

def convert_damagebasein_to_sdk(src: DamagebaseIn) -> damage:
    return damage(**src.dict())
