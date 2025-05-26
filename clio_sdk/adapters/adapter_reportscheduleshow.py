# Adapter for reportscheduleshow
from clio_sdk.models.reportscheduleshow import ReportscheduleshowIn, ReportscheduleshowOut, ReportscheduleshowUpdate, ReportscheduleshowDb
from clio_client.models.report_schedule_show import ReportScheduleShow

def convert_sdk_to_reportscheduleshowout(src: ReportScheduleShow) -> ReportscheduleshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportscheduleshowOut(**src.model_dump())

def convert_reportscheduleshowin_to_sdk(src: ReportscheduleshowIn) -> ReportScheduleShow:
    """Converts a clio_sdk model to clio_client model."""
    return ReportScheduleShow(**src.model_dump())
