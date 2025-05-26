# Adapter for websitebase
from clio_sdk.models.websitebase import WebsitebaseIn, WebsitebaseOut, WebsitebaseUpdate, WebsitebaseDb
from clio_client.models import web_site_base

def convert_sdk_to_websitebaseout(src: web_site_base) -> WebsitebaseOut:
    return WebsitebaseOut(**src.dict())

def convert_websitebasein_to_sdk(src: WebsitebaseIn) -> web_site_base:
    return web_site_base(**src.dict())
