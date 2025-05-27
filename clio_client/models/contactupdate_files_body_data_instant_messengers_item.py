from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_files_body_data_instant_messengers_item_name import (
    ContactupdateFilesBodyDataInstantMessengersItemName,
    check_contactupdate_files_body_data_instant_messengers_item_name)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateFilesBodyDataInstantMessengersItem")


@_attrs_define
class ContactupdateFilesBodyDataInstantMessengersItem:
    """
    Attributes:
        name (Union[Unset, ContactupdateFilesBodyDataInstantMessengersItemName]): Name of the InstantMessenger. Default:
            'Other'.
        address (Union[Unset, str]): Address of the InstantMessenger.
        id (Union[Unset, int]): The unique identifier for a single InstantMessenger associated with the Contact. The
            keyword `null` is not valid for this field.
        destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of the
            associated InstantMessenger is present, the InstantMessenger is deleted from the Contact.
    """

    name: Union[Unset, ContactupdateFilesBodyDataInstantMessengersItemName] = "Other"
    address: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name

        address = self.address

        id = self.id

        destroy = self.destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if id is not UNSET:
            field_dict["id"] = id
        if destroy is not UNSET:
            field_dict["_destroy"] = destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateFilesBodyDataInstantMessengersItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = check_contactupdate_files_body_data_instant_messengers_item_name(_name)

        address = d.pop("address", UNSET)

        id = d.pop("id", UNSET)

        destroy = d.pop("_destroy", UNSET)

        contactupdate_files_body_data_instant_messengers_item = cls(
            name=name,
            address=address,
            id=id,
            destroy=destroy,
        )

        contactupdate_files_body_data_instant_messengers_item.additional_properties = d
        return contactupdate_files_body_data_instant_messengers_item

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
