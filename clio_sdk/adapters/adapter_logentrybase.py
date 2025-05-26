# Adapter for logentrybase
from clio_sdk.models.logentrybase import LogentryBaseIn, LogentrybaseOut, LogentrybaseUpdate, LogentrybaseDb
from clio_client.models.log_entry import LogEntry

def convert_sdk_to_logentrybaseout(src: LogEntry) -> LogentrybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LogentrybaseOut(**src.model_dump())

def convert_logentrybasein_to_sdk(src: LogentryBaseIn) -> LogEntry:
    """Converts a clio_sdk model to clio_client model."""
    return LogEntry(**src.model_dump())
