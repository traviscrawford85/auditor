# Adapter for notelist
from clio_sdk.models.notelist import NotelistIn, NotelistOut, NotelistUpdate, NotelistDb
from clio_client.models import note_list

def convert_sdk_to_notelistout(src: note_list) -> NotelistOut:
    return NotelistOut(**src.dict())

def convert_notelistin_to_sdk(src: NotelistIn) -> note_list:
    return note_list(**src.dict())
