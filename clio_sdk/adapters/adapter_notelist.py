# Adapter for notelist
from clio_sdk.models.notelist import NotelistIn, NotelistOut, NotelistUpdate, NotelistDb
from clio_client.models.note_list import NoteList

def convert_sdk_to_notelistout(src: NoteList) -> NotelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return NotelistOut(**src.model_dump())

def convert_notelistin_to_sdk(src: NotelistIn) -> NoteList:
    """Converts a clio_sdk model to clio_client model."""
    return NoteList(**src.model_dump())
