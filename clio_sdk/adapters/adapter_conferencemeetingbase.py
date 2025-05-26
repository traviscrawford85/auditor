# Adapter for conferencemeetingbase
from clio_sdk.models.conferencemeetingbase import ConferencemeetingbaseIn, ConferencemeetingbaseOut, ConferencemeetingbaseUpdate, ConferencemeetingbaseDb
from clio_client.models import conference_meeting_base

def convert_sdk_to_conferencemeetingbaseout(src: conference_meeting_base) -> ConferencemeetingbaseOut:
    return ConferencemeetingbaseOut(**src.dict())

def convert_conferencemeetingbasein_to_sdk(src: ConferencemeetingbaseIn) -> conference_meeting_base:
    return conference_meeting_base(**src.dict())
