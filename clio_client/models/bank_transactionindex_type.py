from typing import Literal, cast

BankTransactionindexType = Literal["asset", "liability"]

BANK_TRANSACTIONINDEX_TYPE_VALUES: set[BankTransactionindexType] = {
    "asset",
    "liability",
}


def check_bank_transactionindex_type(value: str) -> BankTransactionindexType:
    if value in BANK_TRANSACTIONINDEX_TYPE_VALUES:
        return cast(BankTransactionindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BANK_TRANSACTIONINDEX_TYPE_VALUES!r}")
