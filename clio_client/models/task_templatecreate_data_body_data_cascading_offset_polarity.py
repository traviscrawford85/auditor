from typing import Literal, cast

TaskTemplatecreateDataBodyDataCascadingOffsetPolarity = Literal["After", "Before"]

TASK_TEMPLATECREATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[
    TaskTemplatecreateDataBodyDataCascadingOffsetPolarity
] = {
    "After",
    "Before",
}


def check_task_templatecreate_data_body_data_cascading_offset_polarity(
    value: str,
) -> TaskTemplatecreateDataBodyDataCascadingOffsetPolarity:
    if value in TASK_TEMPLATECREATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskTemplatecreateDataBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
