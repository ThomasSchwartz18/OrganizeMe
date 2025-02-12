# src/core/settings_control.py
import json
import os
from src.config import SETTINGS_PATH
class SettingsControl:
    def __init__(self):
        """Initialize the settings controller."""
        self.settings_path = SETTINGS_PATH
        self.settings = self.load_settings()
        self.callback = None  # Callback to notify when settings are updated

    def load_settings(self):
        """Load settings from the settings.json file."""
        if not os.path.exists(self.settings_path):
            # Create default settings if the file doesn't exist
            default_settings = {
                "window_title": "My Application",
                "window_width": 800,
                "window_height": 600,
                "theme": "light"
            }
            os.makedirs("data", exist_ok=True)
            with open(self.settings_path, "w") as f:
                json.dump(default_settings, f, indent=4)
            return default_settings

        with open(self.settings_path, "r") as f:
            return json.load(f)

    def get_setting(self, key):
        """Get a specific setting by key."""
        return self.settings.get(key)

    def update_setting(self, key, value):
        """Update a specific setting."""
        self.settings[key] = value

    def save_settings(self):
        """Save the current settings to the settings.json file."""
        with open(self.settings_path, "w") as f:
            json.dump(self.settings, f, indent=4)
        
        # Notify the main window that settings have been updated
        if self.callback:
            self.callback()

    def set_callback(self, callback):
        """Set a callback to be called when settings are updated."""
        self.callback = callback