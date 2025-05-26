# Adapter for medicalrecordshow
from clio_sdk.models.medicalrecordshow import MedicalrecordshowIn, MedicalrecordshowOut, MedicalrecordshowUpdate, MedicalrecordshowDb
from clio_client.models import medical_record_show

def convert_sdk_to_medicalrecordshowout(src: medical_record_show) -> MedicalrecordshowOut:
    return MedicalrecordshowOut(**src.dict())

def convert_medicalrecordshowin_to_sdk(src: MedicalrecordshowIn) -> medical_record_show:
    return medical_record_show(**src.dict())
