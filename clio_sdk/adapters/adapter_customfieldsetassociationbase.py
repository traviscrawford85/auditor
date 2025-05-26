# Adapter for customfieldsetassociationbase
from clio_sdk.models.customfieldsetassociationbase import CustomfieldsetassociationBaseIn, CustomfieldsetassociationbaseOut, CustomfieldsetassociationbaseUpdate, CustomfieldsetassociationbaseDb
from clio_client.models.custom_field_set_association_base import CustomFieldSetAssociationBase

def convert_sdk_to_customfieldsetassociationbaseout(src: CustomFieldSetAssociationBase) -> CustomfieldsetassociationbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldsetassociationbaseOut(**src.model_dump())

def convert_customfieldsetassociationbasein_to_sdk(src: CustomfieldsetassociationBaseIn) -> CustomFieldSetAssociationBase:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldSetAssociationBase(**src.model_dump())
