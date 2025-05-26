# Adapter for customfieldmatterselectionbase
from clio_sdk.models.customfieldmatterselectionbase import CustomfieldmatterselectionBaseIn, CustomfieldmatterselectionbaseOut, CustomfieldmatterselectionbaseUpdate, CustomfieldmatterselectionbaseDb
from clio_client.models.custom_field_matter_selection_base import CustomFieldMatterSelectionBase

def convert_sdk_to_customfieldmatterselectionbaseout(src: CustomFieldMatterSelectionBase) -> CustomfieldmatterselectionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldmatterselectionbaseOut(**src.model_dump())

def convert_customfieldmatterselectionbasein_to_sdk(src: CustomfieldmatterselectionBaseIn) -> CustomFieldMatterSelectionBase:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldMatterSelectionBase(**src.model_dump())
