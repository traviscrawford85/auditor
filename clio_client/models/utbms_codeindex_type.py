from typing import Literal, cast

UtbmsCodeindexType = Literal["UtbmsActivity", "UtbmsExpense", "UtbmsTask"]

UTBMS_CODEINDEX_TYPE_VALUES: set[UtbmsCodeindexType] = {
    "UtbmsActivity",
    "UtbmsExpense",
    "UtbmsTask",
}


def check_utbms_codeindex_type(value: str) -> UtbmsCodeindexType:
    if value in UTBMS_CODEINDEX_TYPE_VALUES:
        return cast(UtbmsCodeindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UTBMS_CODEINDEX_TYPE_VALUES!r}")
