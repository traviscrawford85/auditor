# Adapter for cliocreatorbase
from clio_sdk.models.cliocreatorbase import CliocreatorbaseIn, CliocreatorbaseOut, CliocreatorbaseUpdate, CliocreatorbaseDb
from clio_client.models import clio_creator_base

def convert_sdk_to_cliocreatorbaseout(src: clio_creator_base) -> CliocreatorbaseOut:
    return CliocreatorbaseOut(**src.dict())

def convert_cliocreatorbasein_to_sdk(src: CliocreatorbaseIn) -> clio_creator_base:
    return clio_creator_base(**src.dict())
