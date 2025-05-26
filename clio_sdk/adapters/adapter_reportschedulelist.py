# Adapter for reportschedulelist
from clio_sdk.models.reportschedulelist import ReportschedulelistIn, ReportschedulelistOut, ReportschedulelistUpdate, ReportschedulelistDb
from clio_client.models.report_schedule_list import ReportScheduleList

def convert_sdk_to_reportschedulelistout(src: ReportScheduleList) -> ReportschedulelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportschedulelistOut(**src.model_dump())

def convert_reportschedulelistin_to_sdk(src: ReportschedulelistIn) -> ReportScheduleList:
    """Converts a clio_sdk model to clio_client model."""
    return ReportScheduleList(**src.model_dump())
