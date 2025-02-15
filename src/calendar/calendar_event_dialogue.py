from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QTextEdit, QDateEdit, QTimeEdit, QComboBox, QPushButton, QHBoxLayout
from PyQt5.QtCore import QDate, QTime

class EventDialog(QDialog):
    def __init__(self, parent=None, event=None):
        super().__init__(parent)
        self.setWindowTitle("Add Event" if event is None else "Edit Event")
        self.event = event
        self.init_ui()
        if event:
            self.load_event(event)

    def init_ui(self):
        self.layout = QFormLayout(self)

        self.title_edit = QLineEdit()
        self.layout.addRow("Title:", self.title_edit)

        self.description_edit = QTextEdit()
        self.layout.addRow("Description:", self.description_edit)

        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.layout.addRow("Date:", self.date_edit)

        self.start_time_edit = QTimeEdit()
        self.start_time_edit.setDisplayFormat("hh:mm AP")
        self.start_time_edit.setTime(QTime.currentTime())
        self.layout.addRow("Start Time:", self.start_time_edit)

        self.end_time_edit = QTimeEdit()
        self.end_time_edit.setDisplayFormat("hh:mm AP")
        self.end_time_edit.setTime(QTime.currentTime().addSecs(3600))
        self.layout.addRow("End Time:", self.end_time_edit)

        # Category Color – using a preset list of colors.
        self.color_combo = QComboBox()
        self.color_combo.addItem("Green", "#979E73")
        self.color_combo.addItem("Pink", "#F794D6")
        self.color_combo.addItem("Blue", "#4A90E2")
        self.color_combo.addItem("Red", "#D0021B")
        self.layout.addRow("Category Color:", self.color_combo)

        # Repeating options
        self.repeating_combo = QComboBox()
        self.repeating_combo.addItem("None", "none")
        self.repeating_combo.addItem("Daily", "daily")
        self.repeating_combo.addItem("Weekly", "weekly")
        self.repeating_combo.addItem("Bi-Weekly", "biweekly")
        self.repeating_combo.addItem("Monthly", "monthly")
        self.repeating_combo.addItem("Yearly", "yearly")
        self.layout.addRow("Repeat:", self.repeating_combo)

        self.repeating_end_edit = QDateEdit()
        self.repeating_end_edit.setDisplayFormat("yyyy-MM-dd")
        self.repeating_end_edit.setCalendarPopup(True)
        self.repeating_end_edit.setDate(QDate.currentDate().addDays(7))
        self.repeating_end_edit.setEnabled(False)
        self.layout.addRow("Repeat End Date:", self.repeating_end_edit)

        self.repeating_combo.currentIndexChanged.connect(self.toggle_repeating_end)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.cancel_button)
        self.layout.addRow(self.button_layout)

        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def toggle_repeating_end(self, index):
        frequency = self.repeating_combo.currentData()
        if frequency == "none":
            self.repeating_end_edit.setEnabled(False)
        else:
            self.repeating_end_edit.setEnabled(True)

    def load_event(self, event):
        self.title_edit.setText(event.get("title", ""))
        self.description_edit.setPlainText(event.get("description", ""))
        date_str = event.get("date", QDate.currentDate().toString("yyyy-MM-dd"))
        self.date_edit.setDate(QDate.fromString(date_str, "yyyy-MM-dd"))
        start_time_str = event.get("start_time", QTime.currentTime().toString("hh:mm AP"))
        self.start_time_edit.setTime(QTime.fromString(start_time_str, "hh:mm AP"))
        end_time_str = event.get("end_time", QTime.currentTime().addSecs(3600).toString("hh:mm AP"))
        self.end_time_edit.setTime(QTime.fromString(end_time_str, "hh:mm AP"))
        color = event.get("color", "#979E73")
        idx = self.color_combo.findData(color)
        if idx != -1:
            self.color_combo.setCurrentIndex(idx)
        repeating = event.get("repeating", {"frequency": "none"})
        freq = repeating.get("frequency", "none")
        idx = self.repeating_combo.findData(freq)
        if idx != -1:
            self.repeating_combo.setCurrentIndex(idx)
        if freq != "none":
            end_date = repeating.get("end_date", QDate.currentDate().addDays(7).toString("yyyy-MM-dd"))
            self.repeating_end_edit.setDate(QDate.fromString(end_date, "yyyy-MM-dd"))
            self.repeating_end_edit.setEnabled(True)
        else:
            self.repeating_end_edit.setEnabled(False)

    def get_event_data(self):
        event_data = {}
        event_data["title"] = self.title_edit.text()
        event_data["description"] = self.description_edit.toPlainText()
        event_data["date"] = self.date_edit.date().toString("yyyy-MM-dd")
        event_data["start_time"] = self.start_time_edit.time().toString("hh:mm AP")
        event_data["end_time"] = self.end_time_edit.time().toString("hh:mm AP")
        event_data["color"] = self.color_combo.currentData()
        frequency = self.repeating_combo.currentData()
        if frequency == "none":
            event_data["repeating"] = {"frequency": "none"}
        else:
            event_data["repeating"] = {
                "frequency": frequency,
                "end_date": self.repeating_end_edit.date().toString("yyyy-MM-dd")
            }
        return event_data
