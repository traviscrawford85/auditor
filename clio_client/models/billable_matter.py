from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billable_matter_client import BillableMatterClient


T = TypeVar("T", bound="BillableMatter")


@_attrs_define
class BillableMatter:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *BillableMatter*
        unbilled_hours (Union[Unset, float]): The unbilled number of hours for the matter
        unbilled_amount (Union[Unset, float]): The unbilled amount for the matter
        amount_in_trust (Union[Unset, float]): The trust amount available for the matter
        display_number (Union[Unset, str]): The reference to the matter
        client (Union[Unset, BillableMatterClient]):
    """

    id: Union[Unset, int] = UNSET
    unbilled_hours: Union[Unset, float] = UNSET
    unbilled_amount: Union[Unset, float] = UNSET
    amount_in_trust: Union[Unset, float] = UNSET
    display_number: Union[Unset, str] = UNSET
    client: Union[Unset, "BillableMatterClient"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        unbilled_hours = self.unbilled_hours

        unbilled_amount = self.unbilled_amount

        amount_in_trust = self.amount_in_trust

        display_number = self.display_number

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if unbilled_hours is not UNSET:
            field_dict["unbilled_hours"] = unbilled_hours
        if unbilled_amount is not UNSET:
            field_dict["unbilled_amount"] = unbilled_amount
        if amount_in_trust is not UNSET:
            field_dict["amount_in_trust"] = amount_in_trust
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if client is not UNSET:
            field_dict["client"] = client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billable_matter_client import BillableMatterClient

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        unbilled_hours = d.pop("unbilled_hours", UNSET)

        unbilled_amount = d.pop("unbilled_amount", UNSET)

        amount_in_trust = d.pop("amount_in_trust", UNSET)

        display_number = d.pop("display_number", UNSET)

        _client = d.pop("client", UNSET)
        client: Union[Unset, BillableMatterClient]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = BillableMatterClient.from_dict(_client)

        billable_matter = cls(
            id=id,
            unbilled_hours=unbilled_hours,
            unbilled_amount=unbilled_amount,
            amount_in_trust=amount_in_trust,
            display_number=display_number,
            client=client,
        )

        billable_matter.additional_properties = d
        return billable_matter

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
