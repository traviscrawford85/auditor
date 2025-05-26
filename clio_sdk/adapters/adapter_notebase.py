# Adapter for notebase
from clio_sdk.models.notebase import NoteBaseIn, NotebaseOut, NotebaseUpdate, NotebaseDb
from clio_client.models.note import Note

def convert_sdk_to_notebaseout(src: Note) -> NotebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return NotebaseOut(**src.model_dump())

def convert_notebasein_to_sdk(src: NoteBaseIn) -> Note:
    """Converts a clio_sdk model to clio_client model."""
    return Note(**src.model_dump())
