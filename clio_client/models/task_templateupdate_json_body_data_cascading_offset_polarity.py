from typing import Literal, cast

TaskTemplateupdateJsonBodyDataCascadingOffsetPolarity = Literal["After", "Before"]

TASK_TEMPLATEUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[
    TaskTemplateupdateJsonBodyDataCascadingOffsetPolarity
] = {
    "After",
    "Before",
}


def check_task_templateupdate_json_body_data_cascading_offset_polarity(
    value: str,
) -> TaskTemplateupdateJsonBodyDataCascadingOffsetPolarity:
    if value in TASK_TEMPLATEUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskTemplateupdateJsonBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
