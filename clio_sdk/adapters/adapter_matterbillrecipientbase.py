# Adapter for matterbillrecipientbase
from clio_sdk.models.matterbillrecipientbase import MatterbillrecipientBaseIn, MatterbillrecipientbaseOut, MatterbillrecipientbaseUpdate, MatterbillrecipientbaseDb
from clio_client.models.matter_bill_recipient import MatterBillRecipient

def convert_sdk_to_matterbillrecipientbaseout(src: MatterBillRecipient) -> MatterbillrecipientbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MatterbillrecipientbaseOut(**src.model_dump())

def convert_matterbillrecipientbasein_to_sdk(src: MatterbillrecipientBaseIn) -> MatterBillRecipient:
    """Converts a clio_sdk model to clio_client model."""
    return MatterBillRecipient(**src.model_dump())
