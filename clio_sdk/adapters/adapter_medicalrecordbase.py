# Adapter for medicalrecordbase
from clio_sdk.models.medicalrecordbase import MedicalrecordBaseIn, MedicalrecordbaseOut, MedicalrecordbaseUpdate, MedicalrecordbaseDb
from clio_client.models.medical_record import MedicalRecord

def convert_sdk_to_medicalrecordbaseout(src: MedicalRecord) -> MedicalrecordbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MedicalrecordbaseOut(**src.model_dump())

def convert_medicalrecordbasein_to_sdk(src: MedicalrecordBaseIn) -> MedicalRecord:
    """Converts a clio_sdk model to clio_client model."""
    return MedicalRecord(**src.model_dump())
