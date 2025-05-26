# Adapter for reportbase
from clio_sdk.models.reportbase import ReportBaseIn, ReportbaseOut, ReportbaseUpdate, ReportbaseDb
from clio_client.models.report import Report

def convert_sdk_to_reportbaseout(src: Report) -> ReportbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportbaseOut(**src.model_dump())

def convert_reportbasein_to_sdk(src: ReportBaseIn) -> Report:
    """Converts a clio_sdk model to clio_client model."""
    return Report(**src.model_dump())
