import os
import json
import uuid
from PyQt5.QtCore import QDate

class CalendarControl:
    def __init__(self, year):
        self.year = year
        self.file_path = os.path.join("data", f"calendar_{year}.json")
        self.events = self.load_events()

    def load_events(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_events(self):
        os.makedirs("data", exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump(self.events, f, indent=4)

    def add_event(self, event):
        # 'event' should be a dict with keys: title, description, date (yyyy-MM-dd),
        # start_time, end_time (in 12‑hour format), color, and repeating (a dict with 'frequency'
        # and optionally 'end_date'). A "completion" dict will be added to track per-occurrence status.
        event["id"] = str(uuid.uuid4())
        if "completion" not in event:
            event["completion"] = {}  # key: occurrence date as string, value: bool
        self.events.append(event)
        self.save_events()
        return event["id"]

    def update_event(self, event_id, updated_event):
        for idx, ev in enumerate(self.events):
            if ev["id"] == event_id:
                self.events[idx].update(updated_event)
                self.save_events()
                return True
        return False

    def delete_event(self, event_id):
        """Delete an event by its ID."""
        for idx, ev in enumerate(self.events):
            if ev["id"] == event_id:
                del self.events[idx]
                self.save_events()
                return True
        return False

    def mark_event_complete(self, event_id, occurrence_date_str, complete=True):
        for ev in self.events:
            if ev["id"] == event_id:
                ev.setdefault("completion", {})[occurrence_date_str] = complete
                self.save_events()
                return True
        return False

    def occurs_on(self, ev, qdate):
        # qdate is a QDate. Determine if the event occurs on this date.
        event_date = QDate.fromString(ev["date"], "yyyy-MM-dd")
        if not event_date.isValid():
            return False

        frequency = ev.get("repeating", {}).get("frequency", "none").lower()
        if frequency == "none":
            return event_date == qdate

        # Determine repeating end date; if not set, assume a far future date.
        repeat_end_str = ev.get("repeating", {}).get("end_date", None)
        if repeat_end_str:
            repeat_end = QDate.fromString(repeat_end_str, "yyyy-MM-dd")
        else:
            repeat_end = QDate(3000, 1, 1)

        if qdate < event_date or qdate > repeat_end:
            return False

        days_diff = event_date.daysTo(qdate)
        if frequency == "daily":
            return True  # occurs every day within the valid range
        elif frequency == "weekly":
            return days_diff % 7 == 0
        elif frequency == "biweekly":
            return days_diff % 14 == 0
        elif frequency == "monthly":
            # Occurs on the same day of the month
            return event_date.day() == qdate.day()
        elif frequency == "yearly":
            return event_date.day() == qdate.day() and event_date.month() == qdate.month()
        return False

    def get_events_for_date(self, qdate):
        # Returns a list of events (with occurrence details) that occur on qdate.
        result = []
        for ev in self.events:
            if self.occurs_on(ev, qdate):
                ev_copy = ev.copy()
                occ_date_str = qdate.toString("yyyy-MM-dd")
                ev_copy["occurrence_date"] = occ_date_str
                ev_copy["completed"] = ev.get("completion", {}).get(occ_date_str, False)
                result.append(ev_copy)
        return result
