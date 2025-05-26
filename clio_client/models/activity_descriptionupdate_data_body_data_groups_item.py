from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityDescriptionupdateDataBodyDataGroupsItem")


@_attrs_define
class ActivityDescriptionupdateDataBodyDataGroupsItem:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single Group associated with the ActivityDescription. The
            keyword `null` is not valid for this field.
        deleted (Union[Unset, bool]): A flag to determine if this Group should lose access to this ActivityDescription.
    """

    id: Union[Unset, int] = UNSET
    deleted: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if deleted is not UNSET:
            field_dict["_deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        deleted = d.pop("_deleted", UNSET)

        activity_descriptionupdate_data_body_data_groups_item = cls(
            id=id,
            deleted=deleted,
        )

        activity_descriptionupdate_data_body_data_groups_item.additional_properties = d
        return activity_descriptionupdate_data_body_data_groups_item

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
