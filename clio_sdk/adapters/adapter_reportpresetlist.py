# Adapter for reportpresetlist
from clio_sdk.models.reportpresetlist import ReportpresetlistIn, ReportpresetlistOut, ReportpresetlistUpdate, ReportpresetlistDb
from clio_client.models import report_preset_list

def convert_sdk_to_reportpresetlistout(src: report_preset_list) -> ReportpresetlistOut:
    return ReportpresetlistOut(**src.dict())

def convert_reportpresetlistin_to_sdk(src: ReportpresetlistIn) -> report_preset_list:
    return report_preset_list(**src.dict())
