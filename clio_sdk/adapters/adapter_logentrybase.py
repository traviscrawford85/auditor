# Adapter for logentrybase
from clio_sdk.models.logentrybase import LogentrybaseIn, LogentrybaseOut, LogentrybaseUpdate, LogentrybaseDb
from clio_client.models import log_entry

def convert_sdk_to_logentrybaseout(src: log_entry) -> LogentrybaseOut:
    return LogentrybaseOut(**src.dict())

def convert_logentrybasein_to_sdk(src: LogentrybaseIn) -> log_entry:
    return log_entry(**src.dict())
