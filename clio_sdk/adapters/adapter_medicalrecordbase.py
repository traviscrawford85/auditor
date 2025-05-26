# Adapter for medicalrecordbase
from clio_sdk.models.medicalrecordbase import MedicalrecordbaseIn, MedicalrecordbaseOut, MedicalrecordbaseUpdate, MedicalrecordbaseDb
from clio_client.models import medical_record

def convert_sdk_to_medicalrecordbaseout(src: medical_record) -> MedicalrecordbaseOut:
    return MedicalrecordbaseOut(**src.dict())

def convert_medicalrecordbasein_to_sdk(src: MedicalrecordbaseIn) -> medical_record:
    return medical_record(**src.dict())
