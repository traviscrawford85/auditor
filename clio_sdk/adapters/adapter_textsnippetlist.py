# Adapter for textsnippetlist
from clio_sdk.models.textsnippetlist import TextsnippetlistIn, TextsnippetlistOut, TextsnippetlistUpdate, TextsnippetlistDb
from clio_client.models import text_snippet_list

def convert_sdk_to_textsnippetlistout(src: text_snippet_list) -> TextsnippetlistOut:
    return TextsnippetlistOut(**src.dict())

def convert_textsnippetlistin_to_sdk(src: TextsnippetlistIn) -> text_snippet_list:
    return text_snippet_list(**src.dict())
