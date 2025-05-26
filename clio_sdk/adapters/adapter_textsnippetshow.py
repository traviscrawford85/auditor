# Adapter for textsnippetshow
from clio_sdk.models.textsnippetshow import TextsnippetshowIn, TextsnippetshowOut, TextsnippetshowUpdate, TextsnippetshowDb
from clio_client.models import text_snippet_show

def convert_sdk_to_textsnippetshowout(src: text_snippet_show) -> TextsnippetshowOut:
    return TextsnippetshowOut(**src.dict())

def convert_textsnippetshowin_to_sdk(src: TextsnippetshowIn) -> text_snippet_show:
    return text_snippet_show(**src.dict())
