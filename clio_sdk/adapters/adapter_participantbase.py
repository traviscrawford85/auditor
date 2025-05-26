# Adapter for participantbase
from clio_sdk.models.participantbase import ParticipantbaseIn, ParticipantbaseOut, ParticipantbaseUpdate, ParticipantbaseDb
from clio_client.models import participant

def convert_sdk_to_participantbaseout(src: participant) -> ParticipantbaseOut:
    return ParticipantbaseOut(**src.dict())

def convert_participantbasein_to_sdk(src: ParticipantbaseIn) -> participant:
    return participant(**src.dict())
