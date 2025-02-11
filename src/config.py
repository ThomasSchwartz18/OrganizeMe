import json
import os

# Path to the settings file
SETTINGS_PATH = os.path.join("data", "settings.json")

def load_settings():
    """Load settings from the settings.json file."""
    if not os.path.exists(SETTINGS_PATH):
        # Create default settings if the file doesn't exist
        default_settings = {
            "window_title": "My Application",
            "window_width": 800,
            "window_height": 600,
            "theme": "light"
        }
        os.makedirs("data", exist_ok=True)
        with open(SETTINGS_PATH, "w") as f:
            json.dump(default_settings, f, indent=4)
        return default_settings

    with open(SETTINGS_PATH, "r") as f:
        return json.load(f)

# Load settings when the module is imported
SETTINGS = load_settings()