# Adapter for cliocreatorbase
from clio_sdk.models.cliocreatorbase import CliocreatorBaseIn, CliocreatorbaseOut, CliocreatorbaseUpdate, CliocreatorbaseDb
from clio_client.models.clio_creator_base import ClioCreatorBase

def convert_sdk_to_cliocreatorbaseout(src: ClioCreatorBase) -> CliocreatorbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CliocreatorbaseOut(**src.model_dump())

def convert_cliocreatorbasein_to_sdk(src: CliocreatorBaseIn) -> ClioCreatorBase:
    """Converts a clio_sdk model to clio_client model."""
    return ClioCreatorBase(**src.model_dump())
