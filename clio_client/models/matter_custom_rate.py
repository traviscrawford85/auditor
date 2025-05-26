from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymorphic_rate import PolymorphicRate


T = TypeVar("T", bound="MatterCustomRate")


@_attrs_define
class MatterCustomRate:
    """
    Attributes:
        type_ (Union[None, Unset, str]): The type of the *MatterCustomRate*
        on_invoice (Union[None, Unset, bool]): Specifies if the matter's associated activity is posted or on a bill.
        rates (Union[None, Unset, list['PolymorphicRate']]): PolymorphicCustomRate
    """

    type_: Union[None, Unset, str] = UNSET
    on_invoice: Union[None, Unset, bool] = UNSET
    rates: Union[None, Unset, list["PolymorphicRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        on_invoice: Union[None, Unset, bool]
        if isinstance(self.on_invoice, Unset):
            on_invoice = UNSET
        else:
            on_invoice = self.on_invoice

        rates: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.rates, Unset):
            rates = UNSET
        elif isinstance(self.rates, list):
            rates = []
            for rates_type_0_item_data in self.rates:
                rates_type_0_item = rates_type_0_item_data.to_dict()
                rates.append(rates_type_0_item)

        else:
            rates = self.rates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if on_invoice is not UNSET:
            field_dict["on_invoice"] = on_invoice
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymorphic_rate import PolymorphicRate

        d = dict(src_dict)

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_on_invoice(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        on_invoice = _parse_on_invoice(d.pop("on_invoice", UNSET))

        def _parse_rates(data: object) -> Union[None, Unset, list["PolymorphicRate"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rates_type_0 = []
                _rates_type_0 = data
                for rates_type_0_item_data in _rates_type_0:
                    rates_type_0_item = PolymorphicRate.from_dict(rates_type_0_item_data)

                    rates_type_0.append(rates_type_0_item)

                return rates_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["PolymorphicRate"]], data)

        rates = _parse_rates(d.pop("rates", UNSET))

        matter_custom_rate = cls(
            type_=type_,
            on_invoice=on_invoice,
            rates=rates,
        )

        matter_custom_rate.additional_properties = d
        return matter_custom_rate

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
