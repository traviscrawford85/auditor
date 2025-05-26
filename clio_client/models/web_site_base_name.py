from typing import Literal, cast

WebSiteBaseName = Literal["Facebook", "Instant Messenger", "LinkedIn", "Other", "Personal", "Twitter", "Work"]

WEB_SITE_BASE_NAME_VALUES: set[WebSiteBaseName] = {
    "Facebook",
    "Instant Messenger",
    "LinkedIn",
    "Other",
    "Personal",
    "Twitter",
    "Work",
}


def check_web_site_base_name(value: str) -> WebSiteBaseName:
    if value in WEB_SITE_BASE_NAME_VALUES:
        return cast(WebSiteBaseName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEB_SITE_BASE_NAME_VALUES!r}")
