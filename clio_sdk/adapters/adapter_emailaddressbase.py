# Adapter for emailaddressbase
from clio_sdk.models.emailaddressbase import EmailaddressbaseIn, EmailaddressbaseOut, EmailaddressbaseUpdate, EmailaddressbaseDb
from clio_client.models import email_address_base

def convert_sdk_to_emailaddressbaseout(src: email_address_base) -> EmailaddressbaseOut:
    return EmailaddressbaseOut(**src.dict())

def convert_emailaddressbasein_to_sdk(src: EmailaddressbaseIn) -> email_address_base:
    return email_address_base(**src.dict())
