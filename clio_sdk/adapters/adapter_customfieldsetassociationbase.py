# Adapter for customfieldsetassociationbase
from clio_sdk.models.customfieldsetassociationbase import CustomfieldsetassociationbaseIn, CustomfieldsetassociationbaseOut, CustomfieldsetassociationbaseUpdate, CustomfieldsetassociationbaseDb
from clio_client.models import custom_field_set_association_base

def convert_sdk_to_customfieldsetassociationbaseout(src: custom_field_set_association_base) -> CustomfieldsetassociationbaseOut:
    return CustomfieldsetassociationbaseOut(**src.dict())

def convert_customfieldsetassociationbasein_to_sdk(src: CustomfieldsetassociationbaseIn) -> custom_field_set_association_base:
    return custom_field_set_association_base(**src.dict())
