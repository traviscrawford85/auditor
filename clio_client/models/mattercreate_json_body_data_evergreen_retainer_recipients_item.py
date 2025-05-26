from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MattercreateJsonBodyDataEvergreenRetainerRecipientsItem")


@_attrs_define
class MattercreateJsonBodyDataEvergreenRetainerRecipientsItem:
    """
    Attributes:
        id (Union[Unset, int]): the `id` of a User who will receive the trust balance notification.
        destroy (Union[Unset, bool]): Used to remove an existing User as a recipient of the trust balance notification.
    """

    id: Union[Unset, int] = UNSET
    destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        destroy = self.destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if destroy is not UNSET:
            field_dict["_destroy"] = destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        destroy = d.pop("_destroy", UNSET)

        mattercreate_json_body_data_evergreen_retainer_recipients_item = cls(
            id=id,
            destroy=destroy,
        )

        mattercreate_json_body_data_evergreen_retainer_recipients_item.additional_properties = d
        return mattercreate_json_body_data_evergreen_retainer_recipients_item

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
