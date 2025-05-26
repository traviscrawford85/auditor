# Adapter for reportpresetshow
from clio_sdk.models.reportpresetshow import ReportpresetshowIn, ReportpresetshowOut, ReportpresetshowUpdate, ReportpresetshowDb
from clio_client.models.report_preset_show import ReportPresetShow

def convert_sdk_to_reportpresetshowout(src: ReportPresetShow) -> ReportpresetshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ReportpresetshowOut(**src.model_dump())

def convert_reportpresetshowin_to_sdk(src: ReportpresetshowIn) -> ReportPresetShow:
    """Converts a clio_sdk model to clio_client model."""
    return ReportPresetShow(**src.model_dump())
