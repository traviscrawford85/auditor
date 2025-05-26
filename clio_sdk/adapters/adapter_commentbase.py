# Adapter for commentbase
from clio_sdk.models.commentbase import CommentbaseIn, CommentbaseOut, CommentbaseUpdate, CommentbaseDb
from clio_client.models import comment

def convert_sdk_to_commentbaseout(src: comment) -> CommentbaseOut:
    return CommentbaseOut(**src.dict())

def convert_commentbasein_to_sdk(src: CommentbaseIn) -> comment:
    return comment(**src.dict())
