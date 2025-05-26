from typing import Literal, cast

ParticipantBaseType = Literal["Company", "Person", "User"]

PARTICIPANT_BASE_TYPE_VALUES: set[ParticipantBaseType] = {
    "Company",
    "Person",
    "User",
}


def check_participant_base_type(value: str) -> ParticipantBaseType:
    if value in PARTICIPANT_BASE_TYPE_VALUES:
        return cast(ParticipantBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PARTICIPANT_BASE_TYPE_VALUES!r}")
