# Adapter for cascadingtasktemplatebase
from clio_sdk.models.cascadingtasktemplatebase import CascadingtasktemplateBaseIn, CascadingtasktemplatebaseOut, CascadingtasktemplatebaseUpdate, CascadingtasktemplatebaseDb
from clio_client.models.cascading_task_template_base import CascadingTaskTemplateBase

def convert_sdk_to_cascadingtasktemplatebaseout(src: CascadingTaskTemplateBase) -> CascadingtasktemplatebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CascadingtasktemplatebaseOut(**src.model_dump())

def convert_cascadingtasktemplatebasein_to_sdk(src: CascadingtasktemplateBaseIn) -> CascadingTaskTemplateBase:
    """Converts a clio_sdk model to clio_client model."""
    return CascadingTaskTemplateBase(**src.model_dump())
