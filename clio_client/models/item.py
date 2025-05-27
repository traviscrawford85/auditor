import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.item_base_type import ItemBaseType, check_item_base_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_property_base import ExternalPropertyBase
    from ..models.item_contact import ItemContact
    from ..models.item_creator import ItemCreator
    from ..models.item_document_category import ItemDocumentCategory
    from ..models.item_group import ItemGroup
    from ..models.item_latest_document_version import ItemLatestDocumentVersion
    from ..models.item_matter import ItemMatter
    from ..models.item_parent import ItemParent


T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Item*
        etag (Union[Unset, str]): ETag for the *Item*
        created_at (Union[Unset, datetime.datetime]): The time the *Item* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Item* was last updated (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, datetime.datetime]): The time the *Item* was deleted (as a ISO-8601 timestamp)
        type_ (Union[Unset, ItemBaseType]): The type of the *Item*
        locked (Union[Unset, bool]): Whether or not the Item is locked. Locked Item cannot be modified
        name (Union[Unset, str]): The name of the Item
        parent (Union[Unset, ItemParent]):
        matter (Union[Unset, ItemMatter]):
        contact (Union[Unset, ItemContact]):
        document_category (Union[Unset, ItemDocumentCategory]):
        creator (Union[Unset, ItemCreator]):
        latest_document_version (Union[Unset, ItemLatestDocumentVersion]):
        group (Union[Unset, ItemGroup]):
        external_properties (Union[Unset, list['ExternalPropertyBase']]): ExternalProperty
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    type_: Union[Unset, ItemBaseType] = UNSET
    locked: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    parent: Union[Unset, "ItemParent"] = UNSET
    matter: Union[Unset, "ItemMatter"] = UNSET
    contact: Union[Unset, "ItemContact"] = UNSET
    document_category: Union[Unset, "ItemDocumentCategory"] = UNSET
    creator: Union[Unset, "ItemCreator"] = UNSET
    latest_document_version: Union[Unset, "ItemLatestDocumentVersion"] = UNSET
    group: Union[Unset, "ItemGroup"] = UNSET
    external_properties: Union[Unset, list["ExternalPropertyBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        locked = self.locked

        name = self.name

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        latest_document_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.latest_document_version, Unset):
            latest_document_version = self.latest_document_version.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

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
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if locked is not UNSET:
            field_dict["locked"] = locked
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if matter is not UNSET:
            field_dict["matter"] = matter
        if contact is not UNSET:
            field_dict["contact"] = contact
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if creator is not UNSET:
            field_dict["creator"] = creator
        if latest_document_version is not UNSET:
            field_dict["latest_document_version"] = latest_document_version
        if group is not UNSET:
            field_dict["group"] = group
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_property_base import ExternalPropertyBase
        from ..models.item_contact import ItemContact
        from ..models.item_creator import ItemCreator
        from ..models.item_document_category import ItemDocumentCategory
        from ..models.item_group import ItemGroup
        from ..models.item_latest_document_version import \
            ItemLatestDocumentVersion
        from ..models.item_matter import ItemMatter
        from ..models.item_parent import ItemParent

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

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

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ItemBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_item_base_type(_type_)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, ItemParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = ItemParent.from_dict(_parent)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, ItemMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ItemMatter.from_dict(_matter)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ItemContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ItemContact.from_dict(_contact)

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, ItemDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = ItemDocumentCategory.from_dict(_document_category)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, ItemCreator]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = ItemCreator.from_dict(_creator)

        _latest_document_version = d.pop("latest_document_version", UNSET)
        latest_document_version: Union[Unset, ItemLatestDocumentVersion]
        if isinstance(_latest_document_version, Unset):
            latest_document_version = UNSET
        else:
            latest_document_version = ItemLatestDocumentVersion.from_dict(_latest_document_version)

        _group = d.pop("group", UNSET)
        group: Union[Unset, ItemGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = ItemGroup.from_dict(_group)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = ExternalPropertyBase.from_dict(external_properties_item_data)

            external_properties.append(external_properties_item)

        item = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            type_=type_,
            locked=locked,
            name=name,
            parent=parent,
            matter=matter,
            contact=contact,
            document_category=document_category,
            creator=creator,
            latest_document_version=latest_document_version,
            group=group,
            external_properties=external_properties,
        )

        item.additional_properties = d
        return item

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
