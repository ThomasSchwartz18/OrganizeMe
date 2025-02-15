from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem, QCalendarWidget, QDialog
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from src.calendar.calendar_control import CalendarControl
from src.calendar.calendar_event_dialogue import EventDialog
from src.calendar.calendar_style import get_calendar_style

class CustomCalendarWidget(QCalendarWidget):
    def __init__(self, calendar_control, parent=None):
        super().__init__(parent)
        self.calendar_control = calendar_control
        self.setGridVisible(True)
        self.apply_styles()

    def apply_styles(self):
        """Apply styles to the calendar."""
        self.setStyleSheet(get_calendar_style())

    def paintCell(self, painter, rect, date):
        """
        Custom rendering for each calendar cell.
        Removes the default centered day number and instead places it in the top-left corner.
        Also draws event titles with colored borders.
        """

        # Get the list of events for this date
        events = self.calendar_control.get_events_for_date(date)

        # Draw the day number in the top-left corner
        painter.setFont(QFont("Segoe UI", 9, QFont.Bold))
        painter.setPen(QColor("#5F5F5E"))  # Default dark grey text
        day_text = str(date.day())
        painter.drawText(rect.left() + 4, rect.top() + 12, day_text)

        # Draw event titles below the day number
        if events:
            y_offset = rect.top() + 12 + 9  # Adjust for positioning

            for ev in events:
                painter.setFont(QFont("Segoe UI", 8))  # Slightly smaller text
                color = QColor(ev.get("color", "#979E73"))  # Default green

                if ev.get("completed", False):
                    color.setAlpha(100)  # Lighter if completed
                else:
                    color.setAlpha(255)

                painter.setPen(QPen(color))

                # Draw the event title
                painter.drawText(rect.left() + 4, y_offset, ev.get("title", ""))

                # Move y_offset for the next event
                y_offset += 9
                if y_offset > rect.bottom():
                    break


class CalendarUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_year = QDate.currentDate().year()
        self.calendar_control = CalendarControl(self.current_year)
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout(self)

        # Left side: Calendar with "Add Event" and "Delete Event" buttons
        self.calendar_widget = CustomCalendarWidget(self.calendar_control)
        self.calendar_widget.selectionChanged.connect(self.update_checklist)

        self.add_event_button = QPushButton("Add Event")
        self.add_event_button.clicked.connect(self.open_add_event_dialog)

        self.delete_event_button = QPushButton("Delete Event")
        self.delete_event_button.clicked.connect(self.delete_selected_event)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.add_event_button)
        left_layout.addWidget(self.delete_event_button)
        left_layout.addWidget(self.calendar_widget)

        # Right side: Checklist for the selected day
        self.checklist = QListWidget()
        self.checklist.itemChanged.connect(self.checklist_item_changed)
        self.checklist.itemDoubleClicked.connect(self.edit_event_from_item)

        self.layout.addLayout(left_layout, 2)
        self.layout.addWidget(self.checklist, 1)

        self.update_checklist()
        self.apply_styles()

    def apply_styles(self):
        """Apply the theme styles to the calendar UI and checklist."""
        style = get_calendar_style()
        self.setStyleSheet(style)
        self.calendar_widget.apply_styles()  # Ensure calendar gets updated
        self.checklist.setStyleSheet(style)

    def reload_theme(self):
        """Reload the theme dynamically when the theme changes."""
        self.apply_styles()
        self.calendar_widget.update()
        self.update_checklist()

    def update_checklist(self):
        self.checklist.clear()
        selected_date = self.calendar_widget.selectedDate()
        events = self.calendar_control.get_events_for_date(selected_date)
        for ev in events:
            item_text = ev.get("title", "")
            item = QListWidgetItem(item_text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            if ev.get("completed", False):
                item.setCheckState(Qt.Checked)
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
            else:
                item.setCheckState(Qt.Unchecked)
            item.setData(Qt.UserRole, ev["id"])
            item.setData(Qt.UserRole + 1, ev.get("occurrence_date"))
            self.checklist.addItem(item)
        self.calendar_widget.update()

    def checklist_item_changed(self, item):
        event_id = item.data(Qt.UserRole)
        occ_date = item.data(Qt.UserRole + 1)
        complete = (item.checkState() == Qt.Checked)
        self.calendar_control.mark_event_complete(event_id, occ_date, complete)
        font = item.font()
        font.setStrikeOut(complete)
        item.setFont(font)
        self.calendar_widget.update()

    def open_add_event_dialog(self):
        dialog = EventDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            event_data = dialog.get_event_data()
            self.calendar_control.add_event(event_data)
            self.update_checklist()
            self.calendar_widget.update()

    def edit_event_from_item(self, item):
        event_id = item.data(Qt.UserRole)
        event = next((ev for ev in self.calendar_control.events if ev["id"] == event_id), None)
        if event is None:
            return
        dialog = EventDialog(self, event=event)
        if dialog.exec_() == QDialog.Accepted:
            updated_data = dialog.get_event_data()
            self.calendar_control.update_event(event_id, updated_data)
            self.update_checklist()
            self.calendar_widget.update()
            
    def delete_selected_event(self):
        """Delete the selected event from the checklist."""
        selected_item = self.checklist.currentItem()
        if selected_item is None:
            return  # No item selected

        event_id = selected_item.data(Qt.UserRole)
        if self.calendar_control.delete_event(event_id):
            self.update_checklist()
            self.calendar_widget.update()
