# src/styles/application_styles.py
from src.styles.themes import AVAILABLE_THEMES
from src.config import SETTINGS  # SETTINGS holds the current settings, including theme

def get_global_style():
    # Determine which theme to use; default to "green" if not set.
    current_theme = SETTINGS.get("theme", "green").lower()
    theme = AVAILABLE_THEMES.get(current_theme, AVAILABLE_THEMES["green"])

    global_style = f"""
    /* Global widget styling */
    QWidget {{
        background-color: {theme['background']};
        color: {theme['text']};
    }}

    /* QPushButton styling */
    QPushButton {{
        background-color: {theme['button']};
        color: {theme['button_text']};
        border: none;
        padding: 5px;
        border-radius: 3px;
    }}
    QPushButton:pressed {{
        background-color: {theme['button_pressed']};
    }}

    /* QLabel styling */
    QLabel {{
        color: {theme['text']};
    }}
    """
    return global_style
