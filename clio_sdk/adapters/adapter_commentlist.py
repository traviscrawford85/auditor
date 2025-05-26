# Adapter for commentlist
from clio_sdk.models.commentlist import CommentlistIn, CommentlistOut, CommentlistUpdate, CommentlistDb
from clio_client.models.comment_list import CommentList

def convert_sdk_to_commentlistout(src: CommentList) -> CommentlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CommentlistOut(**src.model_dump())

def convert_commentlistin_to_sdk(src: CommentlistIn) -> CommentList:
    """Converts a clio_sdk model to clio_client model."""
    return CommentList(**src.model_dump())
