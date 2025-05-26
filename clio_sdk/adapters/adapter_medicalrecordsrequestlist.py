# Adapter for medicalrecordsrequestlist
from clio_sdk.models.medicalrecordsrequestlist import MedicalrecordsrequestlistIn, MedicalrecordsrequestlistOut, MedicalrecordsrequestlistUpdate, MedicalrecordsrequestlistDb
from clio_client.models.medical_records_request_list import MedicalRecordsRequestList

def convert_sdk_to_medicalrecordsrequestlistout(src: MedicalRecordsRequestList) -> MedicalrecordsrequestlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return MedicalrecordsrequestlistOut(**src.model_dump())

def convert_medicalrecordsrequestlistin_to_sdk(src: MedicalrecordsrequestlistIn) -> MedicalRecordsRequestList:
    """Converts a clio_sdk model to clio_client model."""
    return MedicalRecordsRequestList(**src.model_dump())
