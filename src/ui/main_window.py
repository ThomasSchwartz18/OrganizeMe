# src/ui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
from src.ui.title_bar import TitleBar  # Your custom title bar
from src.ui.settings_ui import SettingsUI
from src.core.settings_control import SettingsControl
from src.config import SETTINGS, load_settings
from src.ui.logo_widget import LogoWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Remove the default window frame
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Apply initial settings (title, size, etc.)
        self.apply_settings()

        # Create a central widget and force it to use the style sheet background.
        central_widget = QWidget()
        central_widget.setAttribute(Qt.WA_TranslucentBackground)
        central_widget.setAttribute(Qt.WA_StyledBackground, True)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # Let title bar span full width

        # Add your custom title bar (with opaque green background)
        self.title_bar = TitleBar(self)
        self.main_layout.addWidget(self.title_bar)

        # Create a QStackedWidget for your views (which will inherit the translucent white background)
        self.stacked_widget = QStackedWidget()
        # Optionally, if needed, enable translucency for the stacked widget:
        self.stacked_widget.setAttribute(Qt.WA_TranslucentBackground)
        self.stacked_widget.setAttribute(Qt.WA_StyledBackground, True)
        self.main_layout.addWidget(self.stacked_widget)

        self.setCentralWidget(central_widget)

        # Build the main view
        self.main_view = QWidget()
        self.main_view_layout = QVBoxLayout()
        # self.settings_button = QPushButton("Open Settings")
        # self.settings_button.clicked.connect(self.open_settings)
        # self.main_view_layout.addWidget(self.settings_button)
        self.main_view.setLayout(self.main_view_layout)
        self.stacked_widget.addWidget(self.main_view)

        # Initialize settings control and UI
        self.settings_control = SettingsControl()
        self.settings_control.set_callback(self.on_settings_updated)
        
        # --- Create and position the logo widget ---
        self.logo_widget = LogoWidget(self)
        # Position the logo at the top left corner (with a small margin if desired)
        self.logo_widget.move(10, 10)
        self.logo_widget.raise_()

    def apply_settings(self):
        """Apply settings from config.py to the main window."""
        self.setWindowTitle(SETTINGS["window_title"])
        self.resize(SETTINGS["window_width"], SETTINGS["window_height"])
        if hasattr(self, 'title_bar'):
            self.title_bar.setTitle(SETTINGS["window_title"])

    def open_settings(self):
        """Open the settings UI."""
        self.settings_ui = SettingsUI(self.settings_control)
        self.settings_ui.close_button.clicked.connect(self.close_settings)
        self.stacked_widget.addWidget(self.settings_ui)
        self.stacked_widget.setCurrentWidget(self.settings_ui)

    def close_settings(self):
        """Close the settings UI and return to the main view."""
        self.stacked_widget.setCurrentWidget(self.main_view)
        self.stacked_widget.removeWidget(self.settings_ui)
        self.settings_ui.deleteLater()

    def on_settings_updated(self):
        """Called when settings are updated."""
        global SETTINGS
        SETTINGS = load_settings()
        self.apply_settings()
