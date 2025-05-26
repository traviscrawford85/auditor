# Adapter for jobtitlebase
from clio_sdk.models.jobtitlebase import JobtitleBaseIn, JobtitlebaseOut, JobtitlebaseUpdate, JobtitlebaseDb
from clio_client.models.user_job_title import UserJobTitle

def convert_sdk_to_jobtitlebaseout(src: UserJobTitle) -> JobtitlebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return JobtitlebaseOut(**src.model_dump())

def convert_jobtitlebasein_to_sdk(src: JobtitleBaseIn) -> UserJobTitle:
    """Converts a clio_sdk model to clio_client model."""
    return UserJobTitle(**src.model_dump())
