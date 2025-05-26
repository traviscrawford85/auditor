# Adapter for reportpresetlist
from clio_sdk.models.reportpresetlist import ReportpresetlistIn, ReportpresetlistOut, ReportpresetlistUpdate, ReportpresetlistDb
from clio_client.models.report_preset_list import ReportPresetList

def convert_sdk_to_reportpresetlistout(src: ReportPresetList) -> ReportpresetlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportpresetlistOut(**src.model_dump())

def convert_reportpresetlistin_to_sdk(src: ReportpresetlistIn) -> ReportPresetList:
    """Converts a clio_sdk model to clio_client model."""
    return ReportPresetList(**src.model_dump())
