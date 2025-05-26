# Adapter for errordetail
from clio_sdk.models.errordetail import ErrordetailIn, ErrordetailOut, ErrordetailUpdate, ErrordetailDb
from clio_client.models import error_detail

def convert_sdk_to_errordetailout(src: error_detail) -> ErrordetailOut:
    return ErrordetailOut(**src.dict())

def convert_errordetailin_to_sdk(src: ErrordetailIn) -> error_detail:
    return error_detail(**src.dict())
