from typing import Literal, cast

UtbmsCodeBaseType = Literal["UtbmsActivity", "UtbmsExpense", "UtbmsTask"]

UTBMS_CODE_BASE_TYPE_VALUES: set[UtbmsCodeBaseType] = {
    "UtbmsActivity",
    "UtbmsExpense",
    "UtbmsTask",
}


def check_utbms_code_base_type(value: str) -> UtbmsCodeBaseType:
    if value in UTBMS_CODE_BASE_TYPE_VALUES:
        return cast(UtbmsCodeBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UTBMS_CODE_BASE_TYPE_VALUES!r}")
