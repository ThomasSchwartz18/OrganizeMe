# src/styles/title_bar_style.py

from src.styles.application_styles import GREEN, WHITE, DARKGREEN

def get_title_bar_style():
    """
    Returns the style sheet for the title bar and its buttons.
    """
    style = f"""
    /* Title bar styling */
    QWidget {{
        background-color: {GREEN};
    }}

    /* Title label styling */
    QLabel {{
        color: {WHITE};
        font-size: 14px;
    }}

    /* Button styling */
    QPushButton {{
        background-color: {WHITE};
        color: {GREEN};
        border: 1px solid {DARKGREEN};
        border-radius: 3px;
        font-size: 12px;
        min-width: 10px;
        min-height: 10px;
    }}

    /* Button hover effect */
    QPushButton:hover {{
        background-color: {DARKGREEN};
        color: {WHITE};
    }}
    """
    return style