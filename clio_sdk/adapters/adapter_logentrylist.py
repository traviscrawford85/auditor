# Adapter for logentrylist
from clio_sdk.models.logentrylist import LogentrylistIn, LogentrylistOut, LogentrylistUpdate, LogentrylistDb
from clio_client.models import log_entry_list

def convert_sdk_to_logentrylistout(src: log_entry_list) -> LogentrylistOut:
    return LogentrylistOut(**src.dict())

def convert_logentrylistin_to_sdk(src: LogentrylistIn) -> log_entry_list:
    return log_entry_list(**src.dict())
