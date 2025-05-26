# Adapter for medicalbillshow
from clio_sdk.models.medicalbillshow import MedicalbillshowIn, MedicalbillshowOut, MedicalbillshowUpdate, MedicalbillshowDb
from clio_client.models.medical_bill_show import MedicalBillShow

def convert_sdk_to_medicalbillshowout(src: MedicalBillShow) -> MedicalbillshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return MedicalbillshowOut(**src.model_dump())

def convert_medicalbillshowin_to_sdk(src: MedicalbillshowIn) -> MedicalBillShow:
    """Converts a clio_sdk model to clio_client model."""
    return MedicalBillShow(**src.model_dump())
