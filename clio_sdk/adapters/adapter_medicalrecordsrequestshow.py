# Adapter for medicalrecordsrequestshow
from clio_sdk.models.medicalrecordsrequestshow import MedicalrecordsrequestshowIn, MedicalrecordsrequestshowOut, MedicalrecordsrequestshowUpdate, MedicalrecordsrequestshowDb
from clio_client.models.medical_records_request_show import MedicalRecordsRequestShow

def convert_sdk_to_medicalrecordsrequestshowout(src: MedicalRecordsRequestShow) -> MedicalrecordsrequestshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return MedicalrecordsrequestshowOut(**src.model_dump())

def convert_medicalrecordsrequestshowin_to_sdk(src: MedicalrecordsrequestshowIn) -> MedicalRecordsRequestShow:
    """Converts a clio_sdk model to clio_client model."""
    return MedicalRecordsRequestShow(**src.model_dump())
