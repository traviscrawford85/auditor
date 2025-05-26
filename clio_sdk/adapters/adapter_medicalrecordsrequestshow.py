# Adapter for medicalrecordsrequestshow
from clio_sdk.models.medicalrecordsrequestshow import MedicalrecordsrequestshowIn, MedicalrecordsrequestshowOut, MedicalrecordsrequestshowUpdate, MedicalrecordsrequestshowDb
from clio_client.models import medical_records_request_show

def convert_sdk_to_medicalrecordsrequestshowout(src: medical_records_request_show) -> MedicalrecordsrequestshowOut:
    return MedicalrecordsrequestshowOut(**src.dict())

def convert_medicalrecordsrequestshowin_to_sdk(src: MedicalrecordsrequestshowIn) -> medical_records_request_show:
    return medical_records_request_show(**src.dict())
