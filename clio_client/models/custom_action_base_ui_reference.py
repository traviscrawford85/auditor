from typing import Literal, cast

CustomActionBaseUiReference = Literal[
    "activities/show", "contacts/show", "documents/show", "folders/show", "matters/show"
]

CUSTOM_ACTION_BASE_UI_REFERENCE_VALUES: set[CustomActionBaseUiReference] = {
    "activities/show",
    "contacts/show",
    "documents/show",
    "folders/show",
    "matters/show",
}


def check_custom_action_base_ui_reference(value: str) -> CustomActionBaseUiReference:
    if value in CUSTOM_ACTION_BASE_UI_REFERENCE_VALUES:
        return cast(CustomActionBaseUiReference, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_ACTION_BASE_UI_REFERENCE_VALUES!r}")
