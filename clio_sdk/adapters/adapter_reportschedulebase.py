# Adapter for reportschedulebase
from clio_sdk.models.reportschedulebase import ReportscheduleBaseIn, ReportschedulebaseOut, ReportschedulebaseUpdate, ReportschedulebaseDb
from clio_client.models.report_schedule import ReportSchedule

def convert_sdk_to_reportschedulebaseout(src: ReportSchedule) -> ReportschedulebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportschedulebaseOut(**src.model_dump())

def convert_reportschedulebasein_to_sdk(src: ReportscheduleBaseIn) -> ReportSchedule:
    """Converts a clio_sdk model to clio_client model."""
    return ReportSchedule(**src.model_dump())
