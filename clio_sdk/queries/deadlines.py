from clio_client.api.tasks import TasksApi
from clio_sdk.adapters.adapter_task import to_sdk_task, to_sdk_calendar_entry
from clio_sdk.models import Task, CalendarEntry
from datetime import datetime
from typing import List

def get_upcoming_deadlines(within_days: int = 14) -> List[Task]:
    tasks = TasksApi().list_tasks(status="pending").data
    deadline_cutoff = datetime.utcnow().date().isoformat()
    return [
        to_sdk_task(task)
        for task in tasks
        if task.due_date and task.due_date <= deadline_cutoff
    ]

def get_conflicting_calendar_events(start_date: str, end_date: str) -> List[CalendarEntry]:
    events = CalendarEntriesApi().list_calendar_entries(start_date=start_date, end_date=end_date).data
    # Conflict resolution logic could be added here
    return [to_sdk_calendar_entry(e) for e in events]
