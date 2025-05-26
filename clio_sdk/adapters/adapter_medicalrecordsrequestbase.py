# Adapter for medicalrecordsrequestbase
from clio_sdk.models.medicalrecordsrequestbase import MedicalrecordsrequestBaseIn, MedicalrecordsrequestbaseOut, MedicalrecordsrequestbaseUpdate, MedicalrecordsrequestbaseDb
from clio_client.models.medical_records_request import MedicalRecordsRequest

def convert_sdk_to_medicalrecordsrequestbaseout(src: MedicalRecordsRequest) -> MedicalrecordsrequestbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MedicalrecordsrequestbaseOut(**src.model_dump())

def convert_medicalrecordsrequestbasein_to_sdk(src: MedicalrecordsrequestBaseIn) -> MedicalRecordsRequest:
    """Converts a clio_sdk model to clio_client model."""
    return MedicalRecordsRequest(**src.model_dump())
