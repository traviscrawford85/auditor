# Adapter for reportscheduleshow
from clio_sdk.models.reportscheduleshow import ReportscheduleshowIn, ReportscheduleshowOut, ReportscheduleshowUpdate, ReportscheduleshowDb
from clio_client.models import report_schedule_show

def convert_sdk_to_reportscheduleshowout(src: report_schedule_show) -> ReportscheduleshowOut:
    return ReportscheduleshowOut(**src.dict())

def convert_reportscheduleshowin_to_sdk(src: ReportscheduleshowIn) -> report_schedule_show:
    return report_schedule_show(**src.dict())
