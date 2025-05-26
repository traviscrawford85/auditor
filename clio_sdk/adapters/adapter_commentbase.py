# Adapter for commentbase
from clio_sdk.models.commentbase import CommentBaseIn, CommentbaseOut, CommentbaseUpdate, CommentbaseDb
from clio_client.models.comment import Comment

def convert_sdk_to_commentbaseout(src: Comment) -> CommentbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CommentbaseOut(**src.model_dump())

def convert_commentbasein_to_sdk(src: CommentBaseIn) -> Comment:
    """Converts a clio_sdk model to clio_client model."""
    return Comment(**src.model_dump())
