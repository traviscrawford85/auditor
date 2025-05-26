# Adapter for jobtitlebase
from clio_sdk.models.jobtitlebase import JobtitlebaseIn, JobtitlebaseOut, JobtitlebaseUpdate, JobtitlebaseDb
from clio_client.models import user_job_title

def convert_sdk_to_jobtitlebaseout(src: user_job_title) -> JobtitlebaseOut:
    return JobtitlebaseOut(**src.dict())

def convert_jobtitlebasein_to_sdk(src: JobtitlebaseIn) -> user_job_title:
    return user_job_title(**src.dict())
