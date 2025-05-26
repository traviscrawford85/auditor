from typing import Literal, cast

TaskTemplateupdateDataBodyDataCascadingOffsetPolarity = Literal["After", "Before"]

TASK_TEMPLATEUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[
    TaskTemplateupdateDataBodyDataCascadingOffsetPolarity
] = {
    "After",
    "Before",
}


def check_task_templateupdate_data_body_data_cascading_offset_polarity(
    value: str,
) -> TaskTemplateupdateDataBodyDataCascadingOffsetPolarity:
    if value in TASK_TEMPLATEUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskTemplateupdateDataBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
