# Adapter for websitebase
from clio_sdk.models.websitebase import WebsiteBaseIn, WebsitebaseOut, WebsitebaseUpdate, WebsitebaseDb
from clio_client.models.web_site_base import WebSiteBase

def convert_sdk_to_websitebaseout(src: WebSiteBase) -> WebsitebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return WebsitebaseOut(**src.model_dump())

def convert_websitebasein_to_sdk(src: WebsiteBaseIn) -> WebSiteBase:
    """Converts a clio_sdk model to clio_client model."""
    return WebSiteBase(**src.model_dump())
