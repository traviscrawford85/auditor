import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.document_base_type import DocumentBaseType, check_document_base_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_contact import DocumentContact
    from ..models.document_creator import DocumentCreator
    from ..models.document_document_category import DocumentDocumentCategory
    from ..models.document_group import DocumentGroup
    from ..models.document_latest_document_version import DocumentLatestDocumentVersion
    from ..models.document_matter import DocumentMatter
    from ..models.document_parent import DocumentParent
    from ..models.document_version_base import DocumentVersionBase
    from ..models.external_property_base import ExternalPropertyBase


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Document*
        etag (Union[Unset, str]): ETag for the *Document*
        created_at (Union[Unset, datetime.datetime]): The time the *Document* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Document* was last updated (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, datetime.datetime]): The time the *Document* was deleted (as a ISO-8601 timestamp)
        type_ (Union[Unset, DocumentBaseType]): The type of the *Document*
        locked (Union[Unset, bool]): Whether or not the Document is locked. Locked Document cannot be modified
        name (Union[Unset, str]): The name of the Document
        received_at (Union[Unset, datetime.datetime]): The time the last document version was received (as an ISO-8601
            timestamp)
        filename (Union[Unset, str]): The uploaded file name of the latest document version.
        size (Union[Unset, int]): The file size
        content_type (Union[Unset, str]): The uploaded file content type
        parent (Union[Unset, DocumentParent]):
        matter (Union[Unset, DocumentMatter]):
        contact (Union[Unset, DocumentContact]):
        document_category (Union[Unset, DocumentDocumentCategory]):
        creator (Union[Unset, DocumentCreator]):
        latest_document_version (Union[Unset, DocumentLatestDocumentVersion]):
        group (Union[Unset, DocumentGroup]):
        external_properties (Union[Unset, list['ExternalPropertyBase']]): ExternalProperty
        document_versions (Union[Unset, list['DocumentVersionBase']]): DocumentVersion
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    type_: Union[Unset, DocumentBaseType] = UNSET
    locked: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    filename: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    parent: Union[Unset, "DocumentParent"] = UNSET
    matter: Union[Unset, "DocumentMatter"] = UNSET
    contact: Union[Unset, "DocumentContact"] = UNSET
    document_category: Union[Unset, "DocumentDocumentCategory"] = UNSET
    creator: Union[Unset, "DocumentCreator"] = UNSET
    latest_document_version: Union[Unset, "DocumentLatestDocumentVersion"] = UNSET
    group: Union[Unset, "DocumentGroup"] = UNSET
    external_properties: Union[Unset, list["ExternalPropertyBase"]] = UNSET
    document_versions: Union[Unset, list["DocumentVersionBase"]] = UNSET
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

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        filename = self.filename

        size = self.size

        content_type = self.content_type

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

        document_versions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.document_versions, Unset):
            document_versions = []
            for document_versions_item_data in self.document_versions:
                document_versions_item = document_versions_item_data.to_dict()
                document_versions.append(document_versions_item)

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
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if filename is not UNSET:
            field_dict["filename"] = filename
        if size is not UNSET:
            field_dict["size"] = size
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
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
        if document_versions is not UNSET:
            field_dict["document_versions"] = document_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_contact import DocumentContact
        from ..models.document_creator import DocumentCreator
        from ..models.document_document_category import DocumentDocumentCategory
        from ..models.document_group import DocumentGroup
        from ..models.document_latest_document_version import DocumentLatestDocumentVersion
        from ..models.document_matter import DocumentMatter
        from ..models.document_parent import DocumentParent
        from ..models.document_version_base import DocumentVersionBase
        from ..models.external_property_base import ExternalPropertyBase

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
        type_: Union[Unset, DocumentBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_document_base_type(_type_)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        filename = d.pop("filename", UNSET)

        size = d.pop("size", UNSET)

        content_type = d.pop("content_type", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, DocumentParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = DocumentParent.from_dict(_parent)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, DocumentMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = DocumentMatter.from_dict(_matter)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, DocumentContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = DocumentContact.from_dict(_contact)

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, DocumentDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = DocumentDocumentCategory.from_dict(_document_category)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, DocumentCreator]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = DocumentCreator.from_dict(_creator)

        _latest_document_version = d.pop("latest_document_version", UNSET)
        latest_document_version: Union[Unset, DocumentLatestDocumentVersion]
        if isinstance(_latest_document_version, Unset):
            latest_document_version = UNSET
        else:
            latest_document_version = DocumentLatestDocumentVersion.from_dict(_latest_document_version)

        _group = d.pop("group", UNSET)
        group: Union[Unset, DocumentGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = DocumentGroup.from_dict(_group)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = ExternalPropertyBase.from_dict(external_properties_item_data)

            external_properties.append(external_properties_item)

        document_versions = []
        _document_versions = d.pop("document_versions", UNSET)
        for document_versions_item_data in _document_versions or []:
            document_versions_item = DocumentVersionBase.from_dict(document_versions_item_data)

            document_versions.append(document_versions_item)

        document = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            type_=type_,
            locked=locked,
            name=name,
            received_at=received_at,
            filename=filename,
            size=size,
            content_type=content_type,
            parent=parent,
            matter=matter,
            contact=contact,
            document_category=document_category,
            creator=creator,
            latest_document_version=latest_document_version,
            group=group,
            external_properties=external_properties,
            document_versions=document_versions,
        )

        document.additional_properties = d
        return document

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
