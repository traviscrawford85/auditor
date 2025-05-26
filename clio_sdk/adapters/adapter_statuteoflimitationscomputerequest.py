# Adapter for statuteoflimitationscomputerequest
from clio_sdk.models.statuteoflimitationscomputerequest import StatuteoflimitationscomputerequestIn, StatuteoflimitationscomputerequestOut, StatuteoflimitationscomputerequestUpdate, StatuteoflimitationscomputerequestDb
from clio_client.models.statute_of_limitations_compute_request import StatuteOfLimitationsComputeRequest

def convert_sdk_to_statuteoflimitationscomputerequestout(src: StatuteOfLimitationsComputeRequest) -> StatuteoflimitationscomputerequestOut:
    """Converts a clio_client model to clio_sdk model."""
    return StatuteoflimitationscomputerequestOut(**src.model_dump())

def convert_statuteoflimitationscomputerequestin_to_sdk(src: StatuteoflimitationscomputerequestIn) -> StatuteOfLimitationsComputeRequest:
    """Converts a clio_sdk model to clio_client model."""
    return StatuteOfLimitationsComputeRequest(**src.model_dump())
