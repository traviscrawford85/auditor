# Adapter for reportpresetbase
from clio_sdk.models.reportpresetbase import ReportpresetBaseIn, ReportpresetbaseOut, ReportpresetbaseUpdate, ReportpresetbaseDb
from clio_client.models.report_preset import ReportPreset

def convert_sdk_to_reportpresetbaseout(src: ReportPreset) -> ReportpresetbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportpresetbaseOut(**src.model_dump())

def convert_reportpresetbasein_to_sdk(src: ReportpresetBaseIn) -> ReportPreset:
    """Converts a clio_sdk model to clio_client model."""
    return ReportPreset(**src.model_dump())
