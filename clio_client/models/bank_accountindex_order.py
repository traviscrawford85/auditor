from typing import Literal, cast

BankAccountindexOrder = Literal[
    "account_number(asc)",
    "account_number(desc)",
    "currency(asc)",
    "currency(desc)",
    "id(asc)",
    "id(desc)",
    "institution(asc)",
    "institution(desc)",
    "name(asc)",
    "name(desc)",
    "transit_number(asc)",
    "transit_number(desc)",
    "type(asc)",
    "type(desc)",
    "updated_at(asc)",
    "updated_at(desc)",
]

BANK_ACCOUNTINDEX_ORDER_VALUES: set[BankAccountindexOrder] = {
    "account_number(asc)",
    "account_number(desc)",
    "currency(asc)",
    "currency(desc)",
    "id(asc)",
    "id(desc)",
    "institution(asc)",
    "institution(desc)",
    "name(asc)",
    "name(desc)",
    "transit_number(asc)",
    "transit_number(desc)",
    "type(asc)",
    "type(desc)",
    "updated_at(asc)",
    "updated_at(desc)",
}


def check_bank_accountindex_order(value: str) -> BankAccountindexOrder:
    if value in BANK_ACCOUNTINDEX_ORDER_VALUES:
        return cast(BankAccountindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNTINDEX_ORDER_VALUES!r}")
