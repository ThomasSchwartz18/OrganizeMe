from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QMessageBox, QApplication, QSlider, QTabWidget, QComboBox, QWidget
)
from PyQt5.QtCore import Qt, QTimer
from src.config import SETTINGS
from src.styles.settings_style import get_settings_style

class SettingsUI(QDialog):  # Inherit from QDialog instead of QWidget
    def __init__(self, settings_control):
        super().__init__()
        self.setObjectName("settingsWidget")  # Set an object name
        self.setAttribute(Qt.WA_StyledBackground, True)  # Ensure styles are applied

        # Make sure the widget is opaque.
        self.setAttribute(Qt.WA_TranslucentBackground, False)

        self.settings_control = settings_control
        self._is_centered = False  # Add a flag to track if the window has been centered
        self.init_ui()

    def init_ui(self):
        """Initialize the settings UI with tabs for categories and navigation buttons below."""
        self.setWindowTitle("Settings")
        
        # Apply the custom settings style.
        self.setStyleSheet(get_settings_style())

        # Retrieve current settings values
        current_width = self.settings_control.get_setting("window_width")
        current_height = self.settings_control.get_setting("window_height")

        # Set the fixed size using the current settings (using half the value as before)
        self.setFixedSize(current_width // 2, current_height // 2)

        # Main layout for the entire widget
        main_layout = QVBoxLayout()

        # Create a QTabWidget to serve as a navigation bar for different settings categories.
        self.tab_widget = QTabWidget()

        # Create tabs for each category: "General", "Display", and "Other"
        self.general_tab = QWidget()
        self.display_tab = QWidget()
        self.other_tab = QWidget()

        # Add the tabs to the QTabWidget
        self.tab_widget.addTab(self.general_tab, "General")
        self.tab_widget.addTab(self.display_tab, "Display")
        self.tab_widget.addTab(self.other_tab, "Other")

        # ---------------------------
        # Populate the General Tab
        # ---------------------------
        general_layout = QHBoxLayout()
        general_layout.addWidget(QLabel("Window Title:"))
        self.title_input = QLineEdit(self.settings_control.get_setting("window_title"))
        general_layout.addWidget(self.title_input)
        self.general_tab.setLayout(general_layout)

        # ---------------------------
        # Populate the Display Tab
        # ---------------------------
        display_layout = QVBoxLayout()

        # Window Width Layout
        width_layout = QHBoxLayout()
        width_label = QLabel("Window Width:")
        width_label.setFixedWidth(100)  # Ensures consistent label width
        width_layout.addWidget(width_label)

        self.width_input = QLineEdit(str(current_width))
        self.width_input.setFixedWidth(100)  # Adjust input box width
        width_layout.addWidget(self.width_input)

        display_layout.addLayout(width_layout)

        self.width_slider = QSlider(Qt.Horizontal)
        self.width_slider.setRange(100, 2000)  # Adjust range as needed
        self.width_slider.setValue(current_width)
        self.width_slider.valueChanged.connect(
            lambda value: self.width_input.setText(str(value))
        )
        self.width_input.textChanged.connect(
            lambda text: self.update_slider_value(text, self.width_slider)
        )
        display_layout.addWidget(self.width_slider)

        # Window Height Layout
        height_layout = QHBoxLayout()
        height_label = QLabel("Window Height:")
        height_label.setFixedWidth(100)
        height_layout.addWidget(height_label)

        self.height_input = QLineEdit(str(current_height))
        self.height_input.setFixedWidth(100)
        height_layout.addWidget(self.height_input)

        display_layout.addLayout(height_layout)

        self.height_slider = QSlider(Qt.Horizontal)
        self.height_slider.setRange(100, 2000)
        self.height_slider.setValue(current_height)
        self.height_slider.valueChanged.connect(
            lambda value: self.height_input.setText(str(value))
        )
        self.height_input.textChanged.connect(
            lambda text: self.update_slider_value(text, self.height_slider)
        )
        display_layout.addWidget(self.height_slider)

        self.display_tab.setLayout(display_layout)
        
        # --- NEW: Theme Selector ---
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Theme:")
        theme_layout.addWidget(theme_label)

        self.theme_combo = QComboBox()
        # Add "Green" as an option (you can add more if available)
        self.theme_combo.addItem("Green")
        self.theme_combo.addItem("Pink")
        # If you add more themes, add them here:
        # self.theme_combo.addItem("Dark")
        # self.theme_combo.addItem("Light")
        
        # Set the current selection based on settings (assuming it is stored as lowercase, e.g., "green")
        current_theme = self.settings_control.get_setting("theme")
        if current_theme:
            index = self.theme_combo.findText(current_theme.capitalize())
            if index >= 0:
                self.theme_combo.setCurrentIndex(index)
        theme_layout.addWidget(self.theme_combo)
        display_layout.addLayout(theme_layout)

        # -----------------------------------
        # Populate the Other Tab (placeholder)
        # -----------------------------------
        other_layout = QVBoxLayout()
        other_layout.addWidget(QLabel("Other settings go here"))
        self.other_tab.setLayout(other_layout)

        # Add the QTabWidget to the main layout
        main_layout.addWidget(self.tab_widget)

        # Create a separate layout for the Save and Close buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save Settings")
        self.save_button.clicked.connect(self.save_settings)
        button_layout.addWidget(self.save_button)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.close_button)

        # Add the button layout below the tabs so they're always visible
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def update_slider_value(self, text, slider):
        """Helper to update a slider's value if the text represents an integer."""
        if text.isdigit():
            slider.setValue(int(text))
            
    def center_window(self):
        """Center the window relative to its parent or the screen."""
        if self._is_centered:
            return  # Skip if already centered

        # Get the top-level window (the main application window)
        top_window = self.window()
        if top_window:
            parent_geo = top_window.frameGeometry()
            center_point = parent_geo.center()
        else:
            center_point = QApplication.primaryScreen().availableGeometry().center()
        frame_geo = self.frameGeometry()
        frame_geo.moveCenter(center_point)
        self.move(frame_geo.topLeft())
        self._is_centered = True  # Mark the window as centered

    def showEvent(self, event):
        """Center the settings window properly after it is shown."""
        super().showEvent(event)
        # Use a QTimer to delay the centering logic slightly
        QTimer.singleShot(100, self.center_window)

    def moveEvent(self, event):
        """Prevent the window from being moved after it is centered."""
        if self._is_centered:
            # If the window has already been centered, block further moves
            self.center_window()
        super().moveEvent(event)

    def save_settings(self):
        try:
            self.settings_control.update_setting("window_title", self.title_input.text())
            self.settings_control.update_setting("window_width", int(self.width_input.text()))
            self.settings_control.update_setting("window_height", int(self.height_input.text()))
            # Save the theme setting (converted to lowercase for consistency)
            self.settings_control.update_setting("theme", self.theme_combo.currentText().lower())
            self.settings_control.save_settings()
            
            # Optionally, if you need to trigger the update explicitly, call:
            if hasattr(self.settings_control, 'callback') and self.settings_control.callback:
                self.settings_control.callback()
            
            QMessageBox.information(self, "Success", "Settings saved successfully!")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input for width or height!")