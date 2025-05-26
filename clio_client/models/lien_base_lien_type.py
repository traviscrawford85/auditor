from typing import Literal, cast

LienBaseLienType = Literal["general", "medical_payer", "medical_provider"]

LIEN_BASE_LIEN_TYPE_VALUES: set[LienBaseLienType] = {
    "general",
    "medical_payer",
    "medical_provider",
}


def check_lien_base_lien_type(value: str) -> LienBaseLienType:
    if value in LIEN_BASE_LIEN_TYPE_VALUES:
        return cast(LienBaseLienType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIEN_BASE_LIEN_TYPE_VALUES!r}")
