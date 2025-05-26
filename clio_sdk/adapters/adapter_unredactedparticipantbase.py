# Adapter for unredactedparticipantbase
from clio_sdk.models.unredactedparticipantbase import UnredactedparticipantbaseIn, UnredactedparticipantbaseOut, UnredactedparticipantbaseUpdate, UnredactedparticipantbaseDb
from clio_client.models import unredacted_participant_base

def convert_sdk_to_unredactedparticipantbaseout(src: unredacted_participant_base) -> UnredactedparticipantbaseOut:
    return UnredactedparticipantbaseOut(**src.dict())

def convert_unredactedparticipantbasein_to_sdk(src: UnredactedparticipantbaseIn) -> unredacted_participant_base:
    return unredacted_participant_base(**src.dict())
