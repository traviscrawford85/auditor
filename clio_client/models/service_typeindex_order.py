from typing import Literal, cast

ServiceTypeindexOrder = Literal["description(asc)", "description(desc)", "id(asc)", "id(desc)"]

SERVICE_TYPEINDEX_ORDER_VALUES: set[ServiceTypeindexOrder] = {
    "description(asc)",
    "description(desc)",
    "id(asc)",
    "id(desc)",
}


def check_service_typeindex_order(value: str) -> ServiceTypeindexOrder:
    if value in SERVICE_TYPEINDEX_ORDER_VALUES:
        return cast(ServiceTypeindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_TYPEINDEX_ORDER_VALUES!r}")
