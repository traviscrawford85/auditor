# Adapter for reportschedulebase
from clio_sdk.models.reportschedulebase import ReportschedulebaseIn, ReportschedulebaseOut, ReportschedulebaseUpdate, ReportschedulebaseDb
from clio_client.models import report_schedule

def convert_sdk_to_reportschedulebaseout(src: report_schedule) -> ReportschedulebaseOut:
    return ReportschedulebaseOut(**src.dict())

def convert_reportschedulebasein_to_sdk(src: ReportschedulebaseIn) -> report_schedule:
    return report_schedule(**src.dict())
