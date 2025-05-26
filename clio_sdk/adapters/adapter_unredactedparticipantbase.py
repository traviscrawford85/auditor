# Adapter for unredactedparticipantbase
from clio_sdk.models.unredactedparticipantbase import UnredactedparticipantBaseIn, UnredactedparticipantbaseOut, UnredactedparticipantbaseUpdate, UnredactedparticipantbaseDb
from clio_client.models.unredacted_participant_base import UnredactedParticipantBase

def convert_sdk_to_unredactedparticipantbaseout(src: UnredactedParticipantBase) -> UnredactedparticipantbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return UnredactedparticipantbaseOut(**src.model_dump())

def convert_unredactedparticipantbasein_to_sdk(src: UnredactedparticipantBaseIn) -> UnredactedParticipantBase:
    """Converts a clio_sdk model to clio_client model."""
    return UnredactedParticipantBase(**src.model_dump())
