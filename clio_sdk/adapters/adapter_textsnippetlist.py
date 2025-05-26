# Adapter for textsnippetlist
from clio_sdk.models.textsnippetlist import TextsnippetlistIn, TextsnippetlistOut, TextsnippetlistUpdate, TextsnippetlistDb
from clio_client.models.text_snippet_list import TextSnippetList

def convert_sdk_to_textsnippetlistout(src: TextSnippetList) -> TextsnippetlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return TextsnippetlistOut(**src.model_dump())

def convert_textsnippetlistin_to_sdk(src: TextsnippetlistIn) -> TextSnippetList:
    """Converts a clio_sdk model to clio_client model."""
    return TextSnippetList(**src.model_dump())
