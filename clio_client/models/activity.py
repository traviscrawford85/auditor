import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_base_tax_setting import ActivityBaseTaxSetting, check_activity_base_tax_setting
from ..models.activity_base_type import ActivityBaseType, check_activity_base_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_activity_description import ActivityActivityDescription
    from ..models.activity_bill import ActivityBill
    from ..models.activity_calendar_entry import ActivityCalendarEntry
    from ..models.activity_client_portal import ActivityClientPortal
    from ..models.activity_communication import ActivityCommunication
    from ..models.activity_contact_note import ActivityContactNote
    from ..models.activity_document_version import ActivityDocumentVersion
    from ..models.activity_expense_category import ActivityExpenseCategory
    from ..models.activity_legal_aid_uk_activity import ActivityLegalAidUkActivity
    from ..models.activity_matter import ActivityMatter
    from ..models.activity_matter_note import ActivityMatterNote
    from ..models.activity_subject import ActivitySubject
    from ..models.activity_task import ActivityTask
    from ..models.activity_text_message_conversation import ActivityTextMessageConversation
    from ..models.activity_timer import ActivityTimer
    from ..models.activity_user import ActivityUser
    from ..models.activity_utbms_expense import ActivityUtbmsExpense
    from ..models.activity_vendor import ActivityVendor


T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Activity*
        etag (Union[Unset, str]): ETag for the *Activity*
        type_ (Union[Unset, ActivityBaseType]): The type of the *Activity*
        date (Union[Unset, datetime.date]): The date the *Activity* was performed (as a ISO-8601 date)
        quantity_in_hours (Union[Unset, float]): The number of hours the TimeEntry took.
        rounded_quantity_in_hours (Union[Unset, float]): The number of hours rounded accordingly to the billing
            settings.
            The rounded value is used to calculate the total.
        quantity (Union[Unset, float]): The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.

            **Version <= 4.0.3:**
            The number of hours the TimeEntry took.

            **Latest version:**
            The number of seconds the TimeEntry took.
        rounded_quantity (Union[Unset, float]): The field is applicable to time entries only.

            **Version <= 4.0.3:**
            The number of hours rounded accordingly to the billing settings.
            The rounded value is used to calculate the total.

            **Latest version:**
            The number of seconds rounded accordingly to the billing settings.
            The rounded value is used to calculate the total.
        quantity_redacted (Union[Unset, bool]): Is `true` if any of the following fields are redacted:
            `quantity`, `rounded_quantity`, `rounded_quantity_in_hours`, `quantity_in_hours`, `total`, `non_billable_total`
        price (Union[Unset, float]): The hourly or flat rate of the *Activity*
        note (Union[Unset, str]): The details about the *Activity*
        flat_rate (Union[Unset, bool]): Whether the *Activity* is a flat rate
        billed (Union[Unset, bool]): Whether the *Activity* has been added to an active bill that is in the state of
            `awaiting_payment` or `paid`
        on_bill (Union[Unset, bool]): Whether the *Activity* has been added to an active bill that is in the state of
            `draft`, `awaiting_approval`, `awaiting_payment` or `paid`
        total (Union[Unset, float]): The total cost of draft, billable and billed items in the *Activity*
        contingency_fee (Union[Unset, bool]): Whether or not the *Activity* is a contingency fee
        created_at (Union[Unset, datetime.datetime]): The time the *Activity* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Activity* was last updated (as a ISO-8601 timestamp)
        reference (Union[Unset, str]): A check reference for a HardCostEntry.
        non_billable (Union[Unset, bool]): Whether the *Activity* is non-billable
        non_billable_total (Union[Unset, float]): The total cost of non-billable items in the *Activity*
        no_charge (Union[Unset, bool]): Whether the non-billable *Activity* is shown on the bill.
        tax_setting (Union[Unset, ActivityBaseTaxSetting]): The option denoting whether primary tax, secondary tax, or
            both is applied to an expense entry.
        activity_description (Union[Unset, ActivityActivityDescription]):
        expense_category (Union[Unset, ActivityExpenseCategory]):
        bill (Union[Unset, ActivityBill]):
        communication (Union[Unset, ActivityCommunication]):
        client_portal (Union[Unset, ActivityClientPortal]):
        matter (Union[Unset, ActivityMatter]):
        matter_note (Union[Unset, ActivityMatterNote]):
        contact_note (Union[Unset, ActivityContactNote]):
        subject (Union[Unset, ActivitySubject]):
        timer (Union[Unset, ActivityTimer]):
        user (Union[Unset, ActivityUser]):
        utbms_expense (Union[Unset, ActivityUtbmsExpense]):
        vendor (Union[Unset, ActivityVendor]):
        calendar_entry (Union[Unset, ActivityCalendarEntry]):
        task (Union[Unset, ActivityTask]):
        text_message_conversation (Union[Unset, ActivityTextMessageConversation]):
        document_version (Union[Unset, ActivityDocumentVersion]):
        legal_aid_uk_activity (Union[Unset, ActivityLegalAidUkActivity]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    type_: Union[Unset, ActivityBaseType] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    quantity_in_hours: Union[Unset, float] = UNSET
    rounded_quantity_in_hours: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    rounded_quantity: Union[Unset, float] = UNSET
    quantity_redacted: Union[Unset, bool] = UNSET
    price: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    flat_rate: Union[Unset, bool] = UNSET
    billed: Union[Unset, bool] = UNSET
    on_bill: Union[Unset, bool] = UNSET
    total: Union[Unset, float] = UNSET
    contingency_fee: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    reference: Union[Unset, str] = UNSET
    non_billable: Union[Unset, bool] = UNSET
    non_billable_total: Union[Unset, float] = UNSET
    no_charge: Union[Unset, bool] = UNSET
    tax_setting: Union[Unset, ActivityBaseTaxSetting] = UNSET
    activity_description: Union[Unset, "ActivityActivityDescription"] = UNSET
    expense_category: Union[Unset, "ActivityExpenseCategory"] = UNSET
    bill: Union[Unset, "ActivityBill"] = UNSET
    communication: Union[Unset, "ActivityCommunication"] = UNSET
    client_portal: Union[Unset, "ActivityClientPortal"] = UNSET
    matter: Union[Unset, "ActivityMatter"] = UNSET
    matter_note: Union[Unset, "ActivityMatterNote"] = UNSET
    contact_note: Union[Unset, "ActivityContactNote"] = UNSET
    subject: Union[Unset, "ActivitySubject"] = UNSET
    timer: Union[Unset, "ActivityTimer"] = UNSET
    user: Union[Unset, "ActivityUser"] = UNSET
    utbms_expense: Union[Unset, "ActivityUtbmsExpense"] = UNSET
    vendor: Union[Unset, "ActivityVendor"] = UNSET
    calendar_entry: Union[Unset, "ActivityCalendarEntry"] = UNSET
    task: Union[Unset, "ActivityTask"] = UNSET
    text_message_conversation: Union[Unset, "ActivityTextMessageConversation"] = UNSET
    document_version: Union[Unset, "ActivityDocumentVersion"] = UNSET
    legal_aid_uk_activity: Union[Unset, "ActivityLegalAidUkActivity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        quantity_in_hours = self.quantity_in_hours

        rounded_quantity_in_hours = self.rounded_quantity_in_hours

        quantity = self.quantity

        rounded_quantity = self.rounded_quantity

        quantity_redacted = self.quantity_redacted

        price = self.price

        note = self.note

        flat_rate = self.flat_rate

        billed = self.billed

        on_bill = self.on_bill

        total = self.total

        contingency_fee = self.contingency_fee

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        reference = self.reference

        non_billable = self.non_billable

        non_billable_total = self.non_billable_total

        no_charge = self.no_charge

        tax_setting: Union[Unset, str] = UNSET
        if not isinstance(self.tax_setting, Unset):
            tax_setting = self.tax_setting

        activity_description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

        expense_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.expense_category, Unset):
            expense_category = self.expense_category.to_dict()

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        communication: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.communication, Unset):
            communication = self.communication.to_dict()

        client_portal: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client_portal, Unset):
            client_portal = self.client_portal.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        matter_note: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter_note, Unset):
            matter_note = self.matter_note.to_dict()

        contact_note: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact_note, Unset):
            contact_note = self.contact_note.to_dict()

        subject: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        timer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timer, Unset):
            timer = self.timer.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        utbms_expense: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.utbms_expense, Unset):
            utbms_expense = self.utbms_expense.to_dict()

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        calendar_entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.calendar_entry, Unset):
            calendar_entry = self.calendar_entry.to_dict()

        task: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()

        text_message_conversation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.text_message_conversation, Unset):
            text_message_conversation = self.text_message_conversation.to_dict()

        document_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_version, Unset):
            document_version = self.document_version.to_dict()

        legal_aid_uk_activity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legal_aid_uk_activity, Unset):
            legal_aid_uk_activity = self.legal_aid_uk_activity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if type_ is not UNSET:
            field_dict["type"] = type_
        if date is not UNSET:
            field_dict["date"] = date
        if quantity_in_hours is not UNSET:
            field_dict["quantity_in_hours"] = quantity_in_hours
        if rounded_quantity_in_hours is not UNSET:
            field_dict["rounded_quantity_in_hours"] = rounded_quantity_in_hours
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if rounded_quantity is not UNSET:
            field_dict["rounded_quantity"] = rounded_quantity
        if quantity_redacted is not UNSET:
            field_dict["quantity_redacted"] = quantity_redacted
        if price is not UNSET:
            field_dict["price"] = price
        if note is not UNSET:
            field_dict["note"] = note
        if flat_rate is not UNSET:
            field_dict["flat_rate"] = flat_rate
        if billed is not UNSET:
            field_dict["billed"] = billed
        if on_bill is not UNSET:
            field_dict["on_bill"] = on_bill
        if total is not UNSET:
            field_dict["total"] = total
        if contingency_fee is not UNSET:
            field_dict["contingency_fee"] = contingency_fee
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if reference is not UNSET:
            field_dict["reference"] = reference
        if non_billable is not UNSET:
            field_dict["non_billable"] = non_billable
        if non_billable_total is not UNSET:
            field_dict["non_billable_total"] = non_billable_total
        if no_charge is not UNSET:
            field_dict["no_charge"] = no_charge
        if tax_setting is not UNSET:
            field_dict["tax_setting"] = tax_setting
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description
        if expense_category is not UNSET:
            field_dict["expense_category"] = expense_category
        if bill is not UNSET:
            field_dict["bill"] = bill
        if communication is not UNSET:
            field_dict["communication"] = communication
        if client_portal is not UNSET:
            field_dict["client_portal"] = client_portal
        if matter is not UNSET:
            field_dict["matter"] = matter
        if matter_note is not UNSET:
            field_dict["matter_note"] = matter_note
        if contact_note is not UNSET:
            field_dict["contact_note"] = contact_note
        if subject is not UNSET:
            field_dict["subject"] = subject
        if timer is not UNSET:
            field_dict["timer"] = timer
        if user is not UNSET:
            field_dict["user"] = user
        if utbms_expense is not UNSET:
            field_dict["utbms_expense"] = utbms_expense
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if calendar_entry is not UNSET:
            field_dict["calendar_entry"] = calendar_entry
        if task is not UNSET:
            field_dict["task"] = task
        if text_message_conversation is not UNSET:
            field_dict["text_message_conversation"] = text_message_conversation
        if document_version is not UNSET:
            field_dict["document_version"] = document_version
        if legal_aid_uk_activity is not UNSET:
            field_dict["legal_aid_uk_activity"] = legal_aid_uk_activity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_activity_description import ActivityActivityDescription
        from ..models.activity_bill import ActivityBill
        from ..models.activity_calendar_entry import ActivityCalendarEntry
        from ..models.activity_client_portal import ActivityClientPortal
        from ..models.activity_communication import ActivityCommunication
        from ..models.activity_contact_note import ActivityContactNote
        from ..models.activity_document_version import ActivityDocumentVersion
        from ..models.activity_expense_category import ActivityExpenseCategory
        from ..models.activity_legal_aid_uk_activity import ActivityLegalAidUkActivity
        from ..models.activity_matter import ActivityMatter
        from ..models.activity_matter_note import ActivityMatterNote
        from ..models.activity_subject import ActivitySubject
        from ..models.activity_task import ActivityTask
        from ..models.activity_text_message_conversation import ActivityTextMessageConversation
        from ..models.activity_timer import ActivityTimer
        from ..models.activity_user import ActivityUser
        from ..models.activity_utbms_expense import ActivityUtbmsExpense
        from ..models.activity_vendor import ActivityVendor

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ActivityBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_activity_base_type(_type_)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        quantity_in_hours = d.pop("quantity_in_hours", UNSET)

        rounded_quantity_in_hours = d.pop("rounded_quantity_in_hours", UNSET)

        quantity = d.pop("quantity", UNSET)

        rounded_quantity = d.pop("rounded_quantity", UNSET)

        quantity_redacted = d.pop("quantity_redacted", UNSET)

        price = d.pop("price", UNSET)

        note = d.pop("note", UNSET)

        flat_rate = d.pop("flat_rate", UNSET)

        billed = d.pop("billed", UNSET)

        on_bill = d.pop("on_bill", UNSET)

        total = d.pop("total", UNSET)

        contingency_fee = d.pop("contingency_fee", UNSET)

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

        reference = d.pop("reference", UNSET)

        non_billable = d.pop("non_billable", UNSET)

        non_billable_total = d.pop("non_billable_total", UNSET)

        no_charge = d.pop("no_charge", UNSET)

        _tax_setting = d.pop("tax_setting", UNSET)
        tax_setting: Union[Unset, ActivityBaseTaxSetting]
        if isinstance(_tax_setting, Unset):
            tax_setting = UNSET
        else:
            tax_setting = check_activity_base_tax_setting(_tax_setting)

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: Union[Unset, ActivityActivityDescription]
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = ActivityActivityDescription.from_dict(_activity_description)

        _expense_category = d.pop("expense_category", UNSET)
        expense_category: Union[Unset, ActivityExpenseCategory]
        if isinstance(_expense_category, Unset):
            expense_category = UNSET
        else:
            expense_category = ActivityExpenseCategory.from_dict(_expense_category)

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, ActivityBill]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = ActivityBill.from_dict(_bill)

        _communication = d.pop("communication", UNSET)
        communication: Union[Unset, ActivityCommunication]
        if isinstance(_communication, Unset):
            communication = UNSET
        else:
            communication = ActivityCommunication.from_dict(_communication)

        _client_portal = d.pop("client_portal", UNSET)
        client_portal: Union[Unset, ActivityClientPortal]
        if isinstance(_client_portal, Unset):
            client_portal = UNSET
        else:
            client_portal = ActivityClientPortal.from_dict(_client_portal)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, ActivityMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ActivityMatter.from_dict(_matter)

        _matter_note = d.pop("matter_note", UNSET)
        matter_note: Union[Unset, ActivityMatterNote]
        if isinstance(_matter_note, Unset):
            matter_note = UNSET
        else:
            matter_note = ActivityMatterNote.from_dict(_matter_note)

        _contact_note = d.pop("contact_note", UNSET)
        contact_note: Union[Unset, ActivityContactNote]
        if isinstance(_contact_note, Unset):
            contact_note = UNSET
        else:
            contact_note = ActivityContactNote.from_dict(_contact_note)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, ActivitySubject]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = ActivitySubject.from_dict(_subject)

        _timer = d.pop("timer", UNSET)
        timer: Union[Unset, ActivityTimer]
        if isinstance(_timer, Unset):
            timer = UNSET
        else:
            timer = ActivityTimer.from_dict(_timer)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ActivityUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ActivityUser.from_dict(_user)

        _utbms_expense = d.pop("utbms_expense", UNSET)
        utbms_expense: Union[Unset, ActivityUtbmsExpense]
        if isinstance(_utbms_expense, Unset):
            utbms_expense = UNSET
        else:
            utbms_expense = ActivityUtbmsExpense.from_dict(_utbms_expense)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, ActivityVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = ActivityVendor.from_dict(_vendor)

        _calendar_entry = d.pop("calendar_entry", UNSET)
        calendar_entry: Union[Unset, ActivityCalendarEntry]
        if isinstance(_calendar_entry, Unset):
            calendar_entry = UNSET
        else:
            calendar_entry = ActivityCalendarEntry.from_dict(_calendar_entry)

        _task = d.pop("task", UNSET)
        task: Union[Unset, ActivityTask]
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = ActivityTask.from_dict(_task)

        _text_message_conversation = d.pop("text_message_conversation", UNSET)
        text_message_conversation: Union[Unset, ActivityTextMessageConversation]
        if isinstance(_text_message_conversation, Unset):
            text_message_conversation = UNSET
        else:
            text_message_conversation = ActivityTextMessageConversation.from_dict(_text_message_conversation)

        _document_version = d.pop("document_version", UNSET)
        document_version: Union[Unset, ActivityDocumentVersion]
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = ActivityDocumentVersion.from_dict(_document_version)

        _legal_aid_uk_activity = d.pop("legal_aid_uk_activity", UNSET)
        legal_aid_uk_activity: Union[Unset, ActivityLegalAidUkActivity]
        if isinstance(_legal_aid_uk_activity, Unset):
            legal_aid_uk_activity = UNSET
        else:
            legal_aid_uk_activity = ActivityLegalAidUkActivity.from_dict(_legal_aid_uk_activity)

        activity = cls(
            id=id,
            etag=etag,
            type_=type_,
            date=date,
            quantity_in_hours=quantity_in_hours,
            rounded_quantity_in_hours=rounded_quantity_in_hours,
            quantity=quantity,
            rounded_quantity=rounded_quantity,
            quantity_redacted=quantity_redacted,
            price=price,
            note=note,
            flat_rate=flat_rate,
            billed=billed,
            on_bill=on_bill,
            total=total,
            contingency_fee=contingency_fee,
            created_at=created_at,
            updated_at=updated_at,
            reference=reference,
            non_billable=non_billable,
            non_billable_total=non_billable_total,
            no_charge=no_charge,
            tax_setting=tax_setting,
            activity_description=activity_description,
            expense_category=expense_category,
            bill=bill,
            communication=communication,
            client_portal=client_portal,
            matter=matter,
            matter_note=matter_note,
            contact_note=contact_note,
            subject=subject,
            timer=timer,
            user=user,
            utbms_expense=utbms_expense,
            vendor=vendor,
            calendar_entry=calendar_entry,
            task=task,
            text_message_conversation=text_message_conversation,
            document_version=document_version,
            legal_aid_uk_activity=legal_aid_uk_activity,
        )

        activity.additional_properties = d
        return activity

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
