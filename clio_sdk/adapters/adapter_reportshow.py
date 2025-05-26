# Adapter for reportshow
from clio_sdk.models.reportshow import ReportshowIn, ReportshowOut, ReportshowUpdate, ReportshowDb
from clio_client.models.report_show import ReportShow

def convert_sdk_to_reportshowout(src: ReportShow) -> ReportshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportshowOut(**src.model_dump())

def convert_reportshowin_to_sdk(src: ReportshowIn) -> ReportShow:
    """Converts a clio_sdk model to clio_client model."""
    return ReportShow(**src.model_dump())
