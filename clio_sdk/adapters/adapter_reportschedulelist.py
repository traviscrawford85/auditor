# Adapter for reportschedulelist
from clio_sdk.models.reportschedulelist import ReportschedulelistIn, ReportschedulelistOut, ReportschedulelistUpdate, ReportschedulelistDb
from clio_client.models import report_schedule_list

def convert_sdk_to_reportschedulelistout(src: report_schedule_list) -> ReportschedulelistOut:
    return ReportschedulelistOut(**src.dict())

def convert_reportschedulelistin_to_sdk(src: ReportschedulelistIn) -> report_schedule_list:
    return report_schedule_list(**src.dict())
