# Adapter for notebase
from clio_sdk.models.notebase import NotebaseIn, NotebaseOut, NotebaseUpdate, NotebaseDb
from clio_client.models import note

def convert_sdk_to_notebaseout(src: note) -> NotebaseOut:
    return NotebaseOut(**src.dict())

def convert_notebasein_to_sdk(src: NotebaseIn) -> note:
    return note(**src.dict())
