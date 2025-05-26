# Adapter for participantbase
from clio_sdk.models.participantbase import ParticipantBaseIn, ParticipantbaseOut, ParticipantbaseUpdate, ParticipantbaseDb
from clio_client.models.participant import Participant

def convert_sdk_to_participantbaseout(src: Participant) -> ParticipantbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ParticipantbaseOut(**src.model_dump())

def convert_participantbasein_to_sdk(src: ParticipantBaseIn) -> Participant:
    """Converts a clio_sdk model to clio_client model."""
    return Participant(**src.model_dump())
