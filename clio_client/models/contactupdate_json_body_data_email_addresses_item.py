from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_json_body_data_email_addresses_item_name import (
    ContactupdateJsonBodyDataEmailAddressesItemName,
    check_contactupdate_json_body_data_email_addresses_item_name)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateJsonBodyDataEmailAddressesItem")


@_attrs_define
class ContactupdateJsonBodyDataEmailAddressesItem:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single EmailAddress associated with the Contact. The keyword
            `null` is not valid for this field.
        name (Union[Unset, ContactupdateJsonBodyDataEmailAddressesItemName]): Name of the EmailAddress. Default:
            'Other'.
        address (Union[Unset, str]): Email address.
        default_email (Union[Unset, bool]): Whether or not the Contact should be the default email for the Contact.
        destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of the
            associated EmailAddress is present, the EmailAddress is deleted from the Contact.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, ContactupdateJsonBodyDataEmailAddressesItemName] = "Other"
    address: Union[Unset, str] = UNSET
    default_email: Union[Unset, bool] = UNSET
    destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name

        address = self.address

        default_email = self.default_email

        destroy = self.destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if default_email is not UNSET:
            field_dict["default_email"] = default_email
        if destroy is not UNSET:
            field_dict["_destroy"] = destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateJsonBodyDataEmailAddressesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = check_contactupdate_json_body_data_email_addresses_item_name(_name)

        address = d.pop("address", UNSET)

        default_email = d.pop("default_email", UNSET)

        destroy = d.pop("_destroy", UNSET)

        contactupdate_json_body_data_email_addresses_item = cls(
            id=id,
            name=name,
            address=address,
            default_email=default_email,
            destroy=destroy,
        )

        contactupdate_json_body_data_email_addresses_item.additional_properties = d
        return contactupdate_json_body_data_email_addresses_item

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
