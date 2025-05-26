# Adapter for banktransferbase
from clio_sdk.models.banktransferbase import BanktransferBaseIn, BanktransferbaseOut, BanktransferbaseUpdate, BanktransferbaseDb
from clio_client.models.bank_transfer import BankTransfer

def convert_sdk_to_banktransferbaseout(src: BankTransfer) -> BanktransferbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BanktransferbaseOut(**src.model_dump())

def convert_banktransferbasein_to_sdk(src: BanktransferBaseIn) -> BankTransfer:
    """Converts a clio_sdk model to clio_client model."""
    return BankTransfer(**src.model_dump())
