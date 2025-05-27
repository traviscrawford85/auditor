import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymorphic_rate_activity_description import \
        PolymorphicRateActivityDescription
    from ..models.polymorphic_rate_group import PolymorphicRateGroup
    from ..models.polymorphic_rate_user import PolymorphicRateUser


T = TypeVar("T", bound="PolymorphicRate")


@_attrs_define
class PolymorphicRate:
    """PolymorphicCustomRate

    Attributes:
        id (Union[None, Unset, int]):
        etag (Union[None, Unset, str]):
        created_at (Union[None, Unset, datetime.datetime]):
        updated_at (Union[None, Unset, datetime.datetime]):
        rate (Union[None, Unset, float]):
        award (Union[None, Unset, float]):
        note (Union[None, Unset, str]):
        date (Union[None, Unset, datetime.date]):
        user (Union[Unset, PolymorphicRateUser]):
        group (Union[Unset, PolymorphicRateGroup]):
        activity_description (Union[Unset, PolymorphicRateActivityDescription]):
    """

    id: Union[None, Unset, int] = UNSET
    etag: Union[None, Unset, str] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    rate: Union[None, Unset, float] = UNSET
    award: Union[None, Unset, float] = UNSET
    note: Union[None, Unset, str] = UNSET
    date: Union[None, Unset, datetime.date] = UNSET
    user: Union[Unset, "PolymorphicRateUser"] = UNSET
    group: Union[Unset, "PolymorphicRateGroup"] = UNSET
    activity_description: Union[Unset, "PolymorphicRateActivityDescription"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        etag: Union[None, Unset, str]
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        rate: Union[None, Unset, float]
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        award: Union[None, Unset, float]
        if isinstance(self.award, Unset):
            award = UNSET
        else:
            award = self.award

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        activity_description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if rate is not UNSET:
            field_dict["rate"] = rate
        if award is not UNSET:
            field_dict["award"] = award
        if note is not UNSET:
            field_dict["note"] = note
        if date is not UNSET:
            field_dict["date"] = date
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymorphic_rate_activity_description import \
            PolymorphicRateActivityDescription
        from ..models.polymorphic_rate_group import PolymorphicRateGroup
        from ..models.polymorphic_rate_user import PolymorphicRateUser

        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_etag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rate = _parse_rate(d.pop("rate", UNSET))

        def _parse_award(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        award = _parse_award(d.pop("award", UNSET))

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date = _parse_date(d.pop("date", UNSET))

        _user = d.pop("user", UNSET)
        user: Union[Unset, PolymorphicRateUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PolymorphicRateUser.from_dict(_user)

        _group = d.pop("group", UNSET)
        group: Union[Unset, PolymorphicRateGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = PolymorphicRateGroup.from_dict(_group)

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: Union[Unset, PolymorphicRateActivityDescription]
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = PolymorphicRateActivityDescription.from_dict(_activity_description)

        polymorphic_rate = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            rate=rate,
            award=award,
            note=note,
            date=date,
            user=user,
            group=group,
            activity_description=activity_description,
        )

        polymorphic_rate.additional_properties = d
        return polymorphic_rate

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
