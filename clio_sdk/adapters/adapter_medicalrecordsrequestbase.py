# Adapter for medicalrecordsrequestbase
from clio_sdk.models.medicalrecordsrequestbase import MedicalrecordsrequestbaseIn, MedicalrecordsrequestbaseOut, MedicalrecordsrequestbaseUpdate, MedicalrecordsrequestbaseDb
from clio_client.models import medical_records_request

def convert_sdk_to_medicalrecordsrequestbaseout(src: medical_records_request) -> MedicalrecordsrequestbaseOut:
    return MedicalrecordsrequestbaseOut(**src.dict())

def convert_medicalrecordsrequestbasein_to_sdk(src: MedicalrecordsrequestbaseIn) -> medical_records_request:
    return medical_records_request(**src.dict())
