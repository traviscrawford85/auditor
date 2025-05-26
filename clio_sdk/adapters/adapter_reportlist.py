# Adapter for reportlist
from clio_sdk.models.reportlist import ReportlistIn, ReportlistOut, ReportlistUpdate, ReportlistDb
from clio_client.models import report_list

def convert_sdk_to_reportlistout(src: report_list) -> ReportlistOut:
    return ReportlistOut(**src.dict())

def convert_reportlistin_to_sdk(src: ReportlistIn) -> report_list:
    return report_list(**src.dict())
