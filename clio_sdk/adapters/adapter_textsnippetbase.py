# Adapter for textsnippetbase
from clio_sdk.models.textsnippetbase import TextsnippetBaseIn, TextsnippetbaseOut, TextsnippetbaseUpdate, TextsnippetbaseDb
from clio_client.models.text_snippet import TextSnippet

def convert_sdk_to_textsnippetbaseout(src: TextSnippet) -> TextsnippetbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TextsnippetbaseOut(**src.model_dump())

def convert_textsnippetbasein_to_sdk(src: TextsnippetBaseIn) -> TextSnippet:
    """Converts a clio_sdk model to clio_client model."""
    return TextSnippet(**src.model_dump())
