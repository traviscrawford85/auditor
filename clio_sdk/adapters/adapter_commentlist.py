# Adapter for commentlist
from clio_sdk.models.commentlist import CommentlistIn, CommentlistOut, CommentlistUpdate, CommentlistDb
from clio_client.models import comment_list

def convert_sdk_to_commentlistout(src: comment_list) -> CommentlistOut:
    return CommentlistOut(**src.dict())

def convert_commentlistin_to_sdk(src: CommentlistIn) -> comment_list:
    return comment_list(**src.dict())
