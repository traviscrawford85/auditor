# Adapter for logentrylist
from clio_sdk.models.logentrylist import LogentrylistIn, LogentrylistOut, LogentrylistUpdate, LogentrylistDb
from clio_client.models.log_entry_list import LogEntryList

def convert_sdk_to_logentrylistout(src: LogEntryList) -> LogentrylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return LogentrylistOut(**src.model_dump())

def convert_logentrylistin_to_sdk(src: LogentrylistIn) -> LogEntryList:
    """Converts a clio_sdk model to clio_client model."""
    return LogEntryList(**src.model_dump())
