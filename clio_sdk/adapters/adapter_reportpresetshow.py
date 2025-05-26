# Adapter for reportpresetshow
from clio_sdk.models.reportpresetshow import ReportpresetshowIn, ReportpresetshowOut, ReportpresetshowUpdate, ReportpresetshowDb
from clio_client.models import report_preset_show

def convert_sdk_to_reportpresetshowout(src: report_preset_show) -> ReportpresetshowOut:
    return ReportpresetshowOut(**src.dict())

def convert_reportpresetshowin_to_sdk(src: ReportpresetshowIn) -> report_preset_show:
    return report_preset_show(**src.dict())
