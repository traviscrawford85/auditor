# Adapter for textsnippetbase
from clio_sdk.models.textsnippetbase import TextsnippetbaseIn, TextsnippetbaseOut, TextsnippetbaseUpdate, TextsnippetbaseDb
from clio_client.models import text_snippet

def convert_sdk_to_textsnippetbaseout(src: text_snippet) -> TextsnippetbaseOut:
    return TextsnippetbaseOut(**src.dict())

def convert_textsnippetbasein_to_sdk(src: TextsnippetbaseIn) -> text_snippet:
    return text_snippet(**src.dict())
