from typing import Literal, cast

TaskTemplatecreateJsonBodyDataCascadingOffsetPolarity = Literal["After", "Before"]

TASK_TEMPLATECREATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[
    TaskTemplatecreateJsonBodyDataCascadingOffsetPolarity
] = {
    "After",
    "Before",
}


def check_task_templatecreate_json_body_data_cascading_offset_polarity(
    value: str,
) -> TaskTemplatecreateJsonBodyDataCascadingOffsetPolarity:
    if value in TASK_TEMPLATECREATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskTemplatecreateJsonBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
