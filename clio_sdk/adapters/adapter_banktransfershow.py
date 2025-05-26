# Adapter for banktransfershow
from clio_sdk.models.banktransfershow import BanktransfershowIn, BanktransfershowOut, BanktransfershowUpdate, BanktransfershowDb
from clio_client.models.bank_transfer_show import BankTransferShow

def convert_sdk_to_banktransfershowout(src: BankTransferShow) -> BanktransfershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return BanktransfershowOut(**src.model_dump())

def convert_banktransfershowin_to_sdk(src: BanktransfershowIn) -> BankTransferShow:
    """Converts a clio_sdk model to clio_client model."""
    return BankTransferShow(**src.model_dump())
