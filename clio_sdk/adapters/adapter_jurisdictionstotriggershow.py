# Adapter for jurisdictionstotriggershow
from clio_sdk.models.jurisdictionstotriggershow import JurisdictionstotriggershowIn, JurisdictionstotriggershowOut, JurisdictionstotriggershowUpdate, JurisdictionstotriggershowDb
from clio_client.models import jurisdictions_to_trigger_show

def convert_sdk_to_jurisdictionstotriggershowout(src: jurisdictions_to_trigger_show) -> JurisdictionstotriggershowOut:
    return JurisdictionstotriggershowOut(**src.dict())

def convert_jurisdictionstotriggershowin_to_sdk(src: JurisdictionstotriggershowIn) -> jurisdictions_to_trigger_show:
    return jurisdictions_to_trigger_show(**src.dict())
