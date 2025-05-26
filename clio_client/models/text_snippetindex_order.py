from typing import Literal, cast

TextSnippetindexOrder = Literal[
    "id(asc)",
    "id(desc)",
    "phrase(asc)",
    "phrase(desc)",
    "snippet(asc)",
    "snippet(desc)",
    "whole_word(asc)",
    "whole_word(desc)",
]

TEXT_SNIPPETINDEX_ORDER_VALUES: set[TextSnippetindexOrder] = {
    "id(asc)",
    "id(desc)",
    "phrase(asc)",
    "phrase(desc)",
    "snippet(asc)",
    "snippet(desc)",
    "whole_word(asc)",
    "whole_word(desc)",
}


def check_text_snippetindex_order(value: str) -> TextSnippetindexOrder:
    if value in TEXT_SNIPPETINDEX_ORDER_VALUES:
        return cast(TextSnippetindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_SNIPPETINDEX_ORDER_VALUES!r}")
