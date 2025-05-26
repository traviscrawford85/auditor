# Adapter for reportbase
from clio_sdk.models.reportbase import ReportbaseIn, ReportbaseOut, ReportbaseUpdate, ReportbaseDb
from clio_client.models import report

def convert_sdk_to_reportbaseout(src: report) -> ReportbaseOut:
    return ReportbaseOut(**src.dict())

def convert_reportbasein_to_sdk(src: ReportbaseIn) -> report:
    return report(**src.dict())
