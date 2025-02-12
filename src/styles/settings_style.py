# src/styles/settings_style.py
from src.styles.themes import AVAILABLE_THEMES
from src.config import SETTINGS

def get_settings_style():
    current_theme = SETTINGS.get("theme", "green").lower()
    theme = AVAILABLE_THEMES.get(current_theme, AVAILABLE_THEMES["green"])

    style = f"""
    /* General widget styling for settings */
    QWidget {{
        background-color: {theme['background']};
        color: {theme['text']};
        border-radius: 4px;
    }}
    
    /* QLineEdit styling */
    QLineEdit {{
        background-color: {theme['background']};
        color: {theme['text']};
        border: 1px solid {theme['button_pressed']};
        border-radius: 3px;
        padding: 3px;
    }}

    /* Placeholder text styling */
    QLineEdit::placeholder {{
        color: {theme['button']};
    }}

    /* QLabel styling */
    QLabel {{
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
    
    QPushButton:hover {{
        background-color: {theme['button_pressed']};
    }}

    /* QSlider styling */
    QSlider::groove:horizontal {{
        height: 8px;
        background: {theme['button']};
        margin: 2px 0;
        border-radius: 4px;
    }}

    QSlider::handle:horizontal {{
        background: {theme['slider_groove']};
        border: 1px solid {theme['slider_handle']};
        width: 18px;
        height: 18px;
        margin: -5px 0;
        border-radius: 9px;
    }}
    
    /* QTabWidget and QTabBar styling */
    QTabWidget::pane {{
        border: 1px solid {theme['button_pressed']};
        background-color: {theme['button']};
    }}

    QTabBar::tab {{
        background-color: {theme['button']};
        color: {theme['background']};
        padding: 10px;
        border: 1px solid {theme['button_pressed']};
        border-bottom-color: {theme['background']};
    }}

    QTabBar::tab:selected {{
        background-color: {theme['button_pressed']};
        color: {theme['background']};
        border: 1px solid {theme['button_pressed']};
        border-bottom-color: {theme['button_pressed']};
    }}

    QTabBar::tab:hover {{
        background-color: {theme['button_pressed']};
        color: {theme['background']};
    }}

    /* QComboBox (drop-down menu) styling */
    QComboBox {{
        background-color: {theme['background']};
        color: {theme['text']};
        border: 1px solid {theme['button_pressed']};
        border-radius: 3px;
        padding: 5px;
    }}

    QComboBox:hover {{
        background-color: {theme['button']};
    }}

    QComboBox::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 20px;
        border-left: 1px solid {theme['button_pressed']};
    }}

    /* Style for the popup list (the drop-down items) */
    QComboBox QAbstractItemView {{
        background-color: {theme['background']};
        border: 1px solid {theme['button_pressed']};
        /* This color applies when an item is selected */
        selection-background-color: {theme['button_pressed']};
        selection-color: {theme['button_text']};
    }}

    QComboBox QAbstractItemView::item {{
        padding: 4px;
    }}

    QComboBox QAbstractItemView::item:hover {{
        background-color: {theme['button_pressed']};
        color: {theme['button_text']};
    }}

    QListView::item:hover {{
    background-color: {theme['button_pressed']};
    color: {theme['button_text']};
    }}


    /* Settings widget styling */
    #settingsWidget {{
        background-color: {theme['background']};
        color: {theme['text']};
    }}
    """
    return style
