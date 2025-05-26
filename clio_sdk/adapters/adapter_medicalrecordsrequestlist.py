# Adapter for medicalrecordsrequestlist
from clio_sdk.models.medicalrecordsrequestlist import MedicalrecordsrequestlistIn, MedicalrecordsrequestlistOut, MedicalrecordsrequestlistUpdate, MedicalrecordsrequestlistDb
from clio_client.models import medical_records_request_list

def convert_sdk_to_medicalrecordsrequestlistout(src: medical_records_request_list) -> MedicalrecordsrequestlistOut:
    return MedicalrecordsrequestlistOut(**src.dict())

def convert_medicalrecordsrequestlistin_to_sdk(src: MedicalrecordsrequestlistIn) -> medical_records_request_list:
    return medical_records_request_list(**src.dict())
