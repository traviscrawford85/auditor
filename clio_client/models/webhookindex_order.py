from typing import Literal, cast

WebhookindexOrder = Literal["id(asc)", "id(desc)"]

WEBHOOKINDEX_ORDER_VALUES: set[WebhookindexOrder] = {
    "id(asc)",
    "id(desc)",
}


def check_webhookindex_order(value: str) -> WebhookindexOrder:
    if value in WEBHOOKINDEX_ORDER_VALUES:
        return cast(WebhookindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKINDEX_ORDER_VALUES!r}")
