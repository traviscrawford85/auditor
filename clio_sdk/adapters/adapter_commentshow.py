# Adapter for commentshow
from clio_sdk.models.commentshow import CommentshowIn, CommentshowOut, CommentshowUpdate, CommentshowDb
from clio_client.models.comment_show import CommentShow

def convert_sdk_to_commentshowout(src: CommentShow) -> CommentshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CommentshowOut(**src.model_dump())

def convert_commentshowin_to_sdk(src: CommentshowIn) -> CommentShow:
    """Converts a clio_sdk model to clio_client model."""
    return CommentShow(**src.model_dump())
