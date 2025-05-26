# Adapter for commentshow
from clio_sdk.models.commentshow import CommentshowIn, CommentshowOut, CommentshowUpdate, CommentshowDb
from clio_client.models import comment_show

def convert_sdk_to_commentshowout(src: comment_show) -> CommentshowOut:
    return CommentshowOut(**src.dict())

def convert_commentshowin_to_sdk(src: CommentshowIn) -> comment_show:
    return comment_show(**src.dict())
