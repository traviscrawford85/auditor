# Adapter for textsnippetshow
from clio_sdk.models.textsnippetshow import TextsnippetshowIn, TextsnippetshowOut, TextsnippetshowUpdate, TextsnippetshowDb
from clio_client.models.text_snippet_show import TextSnippetShow

def convert_sdk_to_textsnippetshowout(src: TextSnippetShow) -> TextsnippetshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TextsnippetshowOut(**src.model_dump())

def convert_textsnippetshowin_to_sdk(src: TextsnippetshowIn) -> TextSnippetShow:
    """Converts a clio_sdk model to clio_client model."""
    return TextSnippetShow(**src.model_dump())
