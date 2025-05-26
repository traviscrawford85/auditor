# Adapter for reportlist
from clio_sdk.models.reportlist import ReportlistIn, ReportlistOut, ReportlistUpdate, ReportlistDb
from clio_client.models.report_list import ReportList

def convert_sdk_to_reportlistout(src: ReportList) -> ReportlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportlistOut(**src.model_dump())

def convert_reportlistin_to_sdk(src: ReportlistIn) -> ReportList:
    """Converts a clio_sdk model to clio_client model."""
    return ReportList(**src.model_dump())
