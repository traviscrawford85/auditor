# Adapter for noteshow
from clio_sdk.models.noteshow import NoteshowIn, NoteshowOut, NoteshowUpdate, NoteshowDb
from clio_client.models import note_show

def convert_sdk_to_noteshowout(src: note_show) -> NoteshowOut:
    return NoteshowOut(**src.dict())

def convert_noteshowin_to_sdk(src: NoteshowIn) -> note_show:
    return note_show(**src.dict())
