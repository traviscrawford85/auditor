import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_template_base_priority import (
    TaskTemplateBasePriority, check_task_template_base_priority)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTemplateBase")


@_attrs_define
class TaskTemplateBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *TaskTemplate*
        etag (Union[Unset, str]): ETag for the *TaskTemplate*
        name (Union[Unset, str]): The name of the *TaskTemplate*
        description (Union[Unset, str]): A detailed description of the *TaskTemplate*
        priority (Union[Unset, TaskTemplateBasePriority]): *TaskTemplate* priority
        private (Union[Unset, bool]): Whether the *TaskTemplate* is private.
        created_at (Union[Unset, datetime.datetime]): The time the *TaskTemplate* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *TaskTemplate* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    priority: Union[Unset, TaskTemplateBasePriority] = UNSET
    private: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        description = self.description

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        private = self.private

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if private is not UNSET:
            field_dict["private"] = private
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskTemplateBasePriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_task_template_base_priority(_priority)

        private = d.pop("private", UNSET)

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

        task_template_base = cls(
            id=id,
            etag=etag,
            name=name,
            description=description,
            priority=priority,
            private=private,
            created_at=created_at,
            updated_at=updated_at,
        )

        task_template_base.additional_properties = d
        return task_template_base

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
