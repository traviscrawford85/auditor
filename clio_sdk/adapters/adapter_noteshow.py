# Adapter for noteshow
from clio_sdk.models.noteshow import NoteshowIn, NoteshowOut, NoteshowUpdate, NoteshowDb
from clio_client.models.note_show import NoteShow

def convert_sdk_to_noteshowout(src: NoteShow) -> NoteshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return NoteshowOut(**src.model_dump())

def convert_noteshowin_to_sdk(src: NoteshowIn) -> NoteShow:
    """Converts a clio_sdk model to clio_client model."""
    return NoteShow(**src.model_dump())
