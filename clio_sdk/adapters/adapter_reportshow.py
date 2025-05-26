# Adapter for reportshow
from clio_sdk.models.reportshow import ReportshowIn, ReportshowOut, ReportshowUpdate, ReportshowDb
from clio_client.models import report_show

def convert_sdk_to_reportshowout(src: report_show) -> ReportshowOut:
    return ReportshowOut(**src.dict())

def convert_reportshowin_to_sdk(src: ReportshowIn) -> report_show:
    return report_show(**src.dict())
