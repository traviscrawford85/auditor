from typing import Literal, cast

DocumentArchiveBaseState = Literal["completed", "failed", "in_progress", "not_started", "queued"]

DOCUMENT_ARCHIVE_BASE_STATE_VALUES: set[DocumentArchiveBaseState] = {
    "completed",
    "failed",
    "in_progress",
    "not_started",
    "queued",
}


def check_document_archive_base_state(value: str) -> DocumentArchiveBaseState:
    if value in DOCUMENT_ARCHIVE_BASE_STATE_VALUES:
        return cast(DocumentArchiveBaseState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_ARCHIVE_BASE_STATE_VALUES!r}")
