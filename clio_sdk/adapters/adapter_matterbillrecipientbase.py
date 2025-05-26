# Adapter for matterbillrecipientbase
from clio_sdk.models.matterbillrecipientbase import MatterbillrecipientbaseIn, MatterbillrecipientbaseOut, MatterbillrecipientbaseUpdate, MatterbillrecipientbaseDb
from clio_client.models import matter_bill_recipient

def convert_sdk_to_matterbillrecipientbaseout(src: matter_bill_recipient) -> MatterbillrecipientbaseOut:
    return MatterbillrecipientbaseOut(**src.dict())

def convert_matterbillrecipientbasein_to_sdk(src: MatterbillrecipientbaseIn) -> matter_bill_recipient:
    return matter_bill_recipient(**src.dict())
