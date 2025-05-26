# Adapter for polymorphicobjectbase
from clio_sdk.models.polymorphicobjectbase import PolymorphicobjectBaseIn, PolymorphicobjectbaseOut, PolymorphicobjectbaseUpdate, PolymorphicobjectbaseDb
from clio_client.models.polymorphic_object_base import PolymorphicObjectBase

def convert_sdk_to_polymorphicobjectbaseout(src: PolymorphicObjectBase) -> PolymorphicobjectbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PolymorphicobjectbaseOut(**src.model_dump())

def convert_polymorphicobjectbasein_to_sdk(src: PolymorphicobjectBaseIn) -> PolymorphicObjectBase:
    """Converts a clio_sdk model to clio_client model."""
    return PolymorphicObjectBase(**src.model_dump())
