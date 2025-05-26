# Adapter for cascadingtasktemplatebase
from clio_sdk.models.cascadingtasktemplatebase import CascadingtasktemplatebaseIn, CascadingtasktemplatebaseOut, CascadingtasktemplatebaseUpdate, CascadingtasktemplatebaseDb
from clio_client.models import cascading_task_template_base

def convert_sdk_to_cascadingtasktemplatebaseout(src: cascading_task_template_base) -> CascadingtasktemplatebaseOut:
    return CascadingtasktemplatebaseOut(**src.dict())

def convert_cascadingtasktemplatebasein_to_sdk(src: CascadingtasktemplatebaseIn) -> cascading_task_template_base:
    return cascading_task_template_base(**src.dict())
