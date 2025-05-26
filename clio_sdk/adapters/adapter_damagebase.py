# Adapter for damagebase
from clio_sdk.models.damagebase import DamageBaseIn, DamagebaseOut, DamagebaseUpdate, DamagebaseDb
from clio_client.models.damage import Damage

def convert_sdk_to_damagebaseout(src: Damage) -> DamagebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DamagebaseOut(**src.model_dump())

def convert_damagebasein_to_sdk(src: DamageBaseIn) -> Damage:
    """Converts a clio_sdk model to clio_client model."""
    return Damage(**src.model_dump())
