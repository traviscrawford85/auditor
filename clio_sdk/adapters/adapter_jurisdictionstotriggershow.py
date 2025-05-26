# Adapter for jurisdictionstotriggershow
from clio_sdk.models.jurisdictionstotriggershow import JurisdictionstotriggershowIn, JurisdictionstotriggershowOut, JurisdictionstotriggershowUpdate, JurisdictionstotriggershowDb
from clio_client.models.jurisdictions_to_trigger_show import JurisdictionsToTriggerShow

def convert_sdk_to_jurisdictionstotriggershowout(src: JurisdictionsToTriggerShow) -> JurisdictionstotriggershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return JurisdictionstotriggershowOut(**src.model_dump())

def convert_jurisdictionstotriggershowin_to_sdk(src: JurisdictionstotriggershowIn) -> JurisdictionsToTriggerShow:
    """Converts a clio_sdk model to clio_client model."""
    return JurisdictionsToTriggerShow(**src.model_dump())
