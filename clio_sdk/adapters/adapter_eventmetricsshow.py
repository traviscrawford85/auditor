# Adapter for eventmetricsshow
from clio_sdk.models.eventmetricsshow import EventmetricsshowIn, EventmetricsshowOut, EventmetricsshowUpdate, EventmetricsshowDb
from clio_client.models.event_metrics_show import EventMetricsShow

def convert_sdk_to_eventmetricsshowout(src: EventMetricsShow) -> EventmetricsshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return EventmetricsshowOut(**src.model_dump())

def convert_eventmetricsshowin_to_sdk(src: EventmetricsshowIn) -> EventMetricsShow:
    """Converts a clio_sdk model to clio_client model."""
    return EventMetricsShow(**src.model_dump())
