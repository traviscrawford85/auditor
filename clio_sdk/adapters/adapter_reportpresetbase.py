# Adapter for reportpresetbase
from clio_sdk.models.reportpresetbase import ReportpresetbaseIn, ReportpresetbaseOut, ReportpresetbaseUpdate, ReportpresetbaseDb
from clio_client.models import report_preset

def convert_sdk_to_reportpresetbaseout(src: report_preset) -> ReportpresetbaseOut:
    return ReportpresetbaseOut(**src.dict())

def convert_reportpresetbasein_to_sdk(src: ReportpresetbaseIn) -> report_preset:
    return report_preset(**src.dict())
