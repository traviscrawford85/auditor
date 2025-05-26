# Adapter for statuteoflimitationscomputeresponse
from clio_sdk.models.statuteoflimitationscomputeresponse import StatuteoflimitationscomputeresponseIn, StatuteoflimitationscomputeresponseOut, StatuteoflimitationscomputeresponseUpdate, StatuteoflimitationscomputeresponseDb
from clio_client.models.statute_of_limitations_compute_response import StatuteOfLimitationsComputeResponse

def convert_sdk_to_statuteoflimitationscomputeresponseout(src: StatuteOfLimitationsComputeResponse) -> StatuteoflimitationscomputeresponseOut:
    """Converts a clio_client model to clio_sdk model."""
    return StatuteoflimitationscomputeresponseOut(**src.model_dump())

def convert_statuteoflimitationscomputeresponsein_to_sdk(src: StatuteoflimitationscomputeresponseIn) -> StatuteOfLimitationsComputeResponse:
    """Converts a clio_sdk model to clio_client model."""
    return StatuteOfLimitationsComputeResponse(**src.model_dump())
