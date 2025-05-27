import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_base_priority import (TaskBasePriority,
                                         check_task_base_priority)
from ..models.task_base_status import TaskBaseStatus, check_task_base_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterStatuteOfLimitations")


@_attrs_define
class MatterStatuteOfLimitations:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Task*
        etag (Union[Unset, str]): ETag for the *Task*
        name (Union[Unset, str]): The name of the *Task*
        status (Union[Unset, TaskBaseStatus]): Status of the *Task*. (Note that users without advanced tasks can only
            have either complete or pending)
        description (Union[Unset, str]): A detailed description of the *Task*
        priority (Union[Unset, TaskBasePriority]): The priority of the *Task*
        due_at (Union[Unset, datetime.date]): The date the *Task* is due (as a ISO-8601 date)
        permission (Union[Unset, str]): The permission of the *Task*
        completed_at (Union[Unset, datetime.datetime]): The time the *Task* was completed (as a ISO-8601 timestamp)
        notify_completion (Union[Unset, bool]): Whether to notify the assigner of the task's completion
        statute_of_limitations (Union[Unset, bool]): Whether the task is a statute of limitations
        time_estimated (Union[Unset, int]): Time the *Task* should take to complete
        created_at (Union[Unset, datetime.datetime]): The time the *Task* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Task* was last updated (as a ISO-8601 timestamp)
        time_entries_count (Union[Unset, int]): The number of time entries associated with this task
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, TaskBaseStatus] = UNSET
    description: Union[Unset, str] = UNSET
    priority: Union[Unset, TaskBasePriority] = UNSET
    due_at: Union[Unset, datetime.date] = UNSET
    permission: Union[Unset, str] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    notify_completion: Union[Unset, bool] = UNSET
    statute_of_limitations: Union[Unset, bool] = UNSET
    time_estimated: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        description = self.description

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        permission = self.permission

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        notify_completion = self.notify_completion

        statute_of_limitations = self.statute_of_limitations

        time_estimated = self.time_estimated

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        time_entries_count = self.time_entries_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if permission is not UNSET:
            field_dict["permission"] = permission
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if notify_completion is not UNSET:
            field_dict["notify_completion"] = notify_completion
        if statute_of_limitations is not UNSET:
            field_dict["statute_of_limitations"] = statute_of_limitations
        if time_estimated is not UNSET:
            field_dict["time_estimated"] = time_estimated
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, TaskBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_task_base_status(_status)

        description = d.pop("description", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskBasePriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_task_base_priority(_priority)

        _due_at = d.pop("due_at", UNSET)
        due_at: Union[Unset, datetime.date]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at).date()

        permission = d.pop("permission", UNSET)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        notify_completion = d.pop("notify_completion", UNSET)

        statute_of_limitations = d.pop("statute_of_limitations", UNSET)

        time_estimated = d.pop("time_estimated", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        time_entries_count = d.pop("time_entries_count", UNSET)

        matter_statute_of_limitations = cls(
            id=id,
            etag=etag,
            name=name,
            status=status,
            description=description,
            priority=priority,
            due_at=due_at,
            permission=permission,
            completed_at=completed_at,
            notify_completion=notify_completion,
            statute_of_limitations=statute_of_limitations,
            time_estimated=time_estimated,
            created_at=created_at,
            updated_at=updated_at,
            time_entries_count=time_entries_count,
        )

        matter_statute_of_limitations.additional_properties = d
        return matter_statute_of_limitations

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
