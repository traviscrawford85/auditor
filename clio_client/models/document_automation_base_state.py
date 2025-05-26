from typing import Literal, cast

DocumentAutomationBaseState = Literal["completed", "empty", "failed", "in_progress", "not_started", "queued"]

DOCUMENT_AUTOMATION_BASE_STATE_VALUES: set[DocumentAutomationBaseState] = {
    "completed",
    "empty",
    "failed",
    "in_progress",
    "not_started",
    "queued",
}


def check_document_automation_base_state(value: str) -> DocumentAutomationBaseState:
    if value in DOCUMENT_AUTOMATION_BASE_STATE_VALUES:
        return cast(DocumentAutomationBaseState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_AUTOMATION_BASE_STATE_VALUES!r}")
