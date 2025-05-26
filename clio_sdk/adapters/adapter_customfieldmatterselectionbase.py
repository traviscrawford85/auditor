# Adapter for customfieldmatterselectionbase
from clio_sdk.models.customfieldmatterselectionbase import CustomfieldmatterselectionbaseIn, CustomfieldmatterselectionbaseOut, CustomfieldmatterselectionbaseUpdate, CustomfieldmatterselectionbaseDb
from clio_client.models import custom_field_matter_selection_base

def convert_sdk_to_customfieldmatterselectionbaseout(src: custom_field_matter_selection_base) -> CustomfieldmatterselectionbaseOut:
    return CustomfieldmatterselectionbaseOut(**src.dict())

def convert_customfieldmatterselectionbasein_to_sdk(src: CustomfieldmatterselectionbaseIn) -> custom_field_matter_selection_base:
    return custom_field_matter_selection_base(**src.dict())
