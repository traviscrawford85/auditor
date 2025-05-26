# Adapter for conferencemeetingbase
from clio_sdk.models.conferencemeetingbase import ConferencemeetingBaseIn, ConferencemeetingbaseOut, ConferencemeetingbaseUpdate, ConferencemeetingbaseDb
from clio_client.models.conference_meeting_base import ConferenceMeetingBase

def convert_sdk_to_conferencemeetingbaseout(src: ConferenceMeetingBase) -> ConferencemeetingbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ConferencemeetingbaseOut(**src.model_dump())

def convert_conferencemeetingbasein_to_sdk(src: ConferencemeetingBaseIn) -> ConferenceMeetingBase:
    """Converts a clio_sdk model to clio_client model."""
    return ConferenceMeetingBase(**src.model_dump())
