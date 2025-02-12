# src/styles/title_bar_style.py
from src.styles.themes import AVAILABLE_THEMES
from src.config import SETTINGS

def get_title_bar_style():
    current_theme = SETTINGS.get("theme", "green").lower()
    theme = AVAILABLE_THEMES.get(current_theme, AVAILABLE_THEMES["green"])
    
    style = f"""
    /* Title bar background */
    QWidget {{
        background-color: {theme['title_bar_bg']};
    }}

    /* Title label styling */
    QLabel {{
        color: {theme['title_bar_text']};
        font-size: 14px;
    }}

    /* QPushButton styling in the title bar */
    QPushButton {{
        background-color: {theme['background']};
        color: {theme['title_bar_bg']};
        border: 1px solid {theme['button_pressed']};
        border-radius: 3px;
        font-size: 12px;
        min-width: 10px;
        min-height: 10px;
    }}

    /* Button hover effect */
    QPushButton:hover {{
        background-color: {theme['button_pressed']};
        color: {theme['background']};
    }}
    """
    return style
