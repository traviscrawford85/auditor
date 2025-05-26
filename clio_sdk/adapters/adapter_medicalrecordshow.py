# Adapter for medicalrecordshow
from clio_sdk.models.medicalrecordshow import MedicalrecordshowIn, MedicalrecordshowOut, MedicalrecordshowUpdate, MedicalrecordshowDb
from clio_client.models.medical_record_show import MedicalRecordShow

def convert_sdk_to_medicalrecordshowout(src: MedicalRecordShow) -> MedicalrecordshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return MedicalrecordshowOut(**src.model_dump())

def convert_medicalrecordshowin_to_sdk(src: MedicalrecordshowIn) -> MedicalRecordShow:
    """Converts a clio_sdk model to clio_client model."""
    return MedicalRecordShow(**src.model_dump())
