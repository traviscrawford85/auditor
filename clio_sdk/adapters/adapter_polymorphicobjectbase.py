# Adapter for polymorphicobjectbase
from clio_sdk.models.polymorphicobjectbase import PolymorphicobjectbaseIn, PolymorphicobjectbaseOut, PolymorphicobjectbaseUpdate, PolymorphicobjectbaseDb
from clio_client.models import polymorphic_object_base

def convert_sdk_to_polymorphicobjectbaseout(src: polymorphic_object_base) -> PolymorphicobjectbaseOut:
    return PolymorphicobjectbaseOut(**src.dict())

def convert_polymorphicobjectbasein_to_sdk(src: PolymorphicobjectbaseIn) -> polymorphic_object_base:
    return polymorphic_object_base(**src.dict())
