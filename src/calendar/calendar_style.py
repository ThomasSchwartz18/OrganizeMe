from src.styles.themes import AVAILABLE_THEMES
from src.config import SETTINGS

def get_calendar_style():
    """Generate the stylesheet for the calendar UI based on the selected theme."""
    
    current_theme = SETTINGS.get("theme", "green").lower()
    theme = AVAILABLE_THEMES.get(current_theme, AVAILABLE_THEMES["green"])

    style = f"""
    /* Calendar background */
    QCalendarWidget {{
        background-color: {theme['background']};
        color: {theme['text']};
        border: 1px solid {theme['button_pressed']};
        border-radius: 4px;
    }}

    /* General day number styling */
    QCalendarWidget QAbstractItemView {{
        selection-background-color: {theme['light_button_press']};
        selection-color: {theme['text']};
    }}

    /* Selected day */
    QCalendarWidget QTableView::item:selected {{
        background-color: {theme['button_pressed']};
        color: {theme['background']}; /* Text color */
        border-radius: 6px;
        font-weight: bold;
        border: 2px solid {theme['button_text']}; 
    }}
    
    QCalendarWidget QAbstractItemView::item:selected {{
        background-color: {theme['button_pressed']};
    }}

    /* Fix: Hover effect to show selection clearer */
    QCalendarWidget QAbstractItemView::item:hover {{
        background-color: {theme['button']}; 
        color: {theme['background']}; 
    }}

    /* Weekend day text color */
    QCalendarWidget QTableView::item:enabled:!selected:nth-child(7),  
    QCalendarWidget QTableView::item:enabled:!selected:nth-child(6) {{
        color: {theme['button']}; /* Weekend text color */
    }}

    /* Navigation bar (Month & Year selector) */
    QCalendarWidget QWidget#qt_calendar_navigationbar {{
        background-color: {theme['button']};
        color: {theme['button_text']};
    }}

    QPushButton#qt_calendar_prevmonth, QPushButton#qt_calendar_nextmonth {{
        background-color: {theme['button_pressed']};
        color: {theme['background']};
        border-radius: 3px;
    }}

    QPushButton#qt_calendar_prevmonth:hover, QPushButton#qt_calendar_nextmonth:hover {{
        background-color: {theme['button_text']};
        color: {theme['button_pressed']};
    }}

    /* Events inside the calendar */
    QListWidget {{
        background-color: {theme['background']};
        color: {theme['text']};
        border: 1px solid {theme['button_pressed']};
        border-radius: 4px;
    }}

    /* Event items */
    QListWidget::item {{
        background-color: {theme['background']};
        color: {theme['text']};
        padding: 5px;
        border-radius: 3px;
    }}

    QListWidget::item:selected {{
        background-color: {theme['button_pressed']};
        color: {theme['background']};
    }}
    
    /* Delete Event Button */
    QPushButton {{
        background-color: {theme['button']};
        color: {theme['button_text']};
        border: 1px solid {theme['button_pressed']};
        border-radius: 4px;
        padding: 5px;
    }}

    QPushButton:hover {{
        background-color: {theme['button_pressed']};
        color: {theme['background']};
    }}

    QPushButton:pressed {{
        background-color: {theme['button_text']};
        color: {theme['button_pressed']};
    }}
    """
    
    return style