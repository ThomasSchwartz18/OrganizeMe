# src/styles/settings_style.py

from PyQt5.QtGui import QFontDatabase
from src.styles.application_styles import GREEN, DARKGREEN, WHITE, BLACK, TAN, GREY, DARKGREY, FONT_PATH, DARKWHITE

def get_settings_style():
    """
    Returns a style sheet string for the settings window.
      - All non-input text is WHITE,
      - QLineEdit widgets have a white background with DARKGREY text,
      - QSlider's groove is DARKGREEN,
      - QSlider's handle is DARKGREY,
      - Selected tabs in QTabWidget are DARKGREEN.
    """
    # Load the custom font now that a QApplication exists.
    font_id = QFontDatabase.addApplicationFont(FONT_PATH)
    if font_id != -1:
        FONT_FAMILY = QFontDatabase.applicationFontFamilies(font_id)[0]
    else:
        FONT_FAMILY = "Sans Serif"

    style = f"""
    /* Style QLineEdit widgets (input boxes):
       - White background,
       - DARKGREY text color,
       - A light border with slight padding */
    
    QWidget {{
        background-color: {GREEN};
        font-family: "{FONT_FAMILY}";
        color: {WHITE};
        border-radius: 4px;
    }}
    
    QLineEdit {{
        background-color: {WHITE};
        color: {GREEN};
        border: 1px solid {DARKGREEN};
        border-radius: 3px;
        padding: 3px;
    }}

    /* style the placeholder text inside QLineEdits */
    QLineEdit::placeholder {{
        color: {GREEN};
    }}

    /* ensures the text is white */
    QLabel {{
        color: white;
        font-family: "{FONT_FAMILY}";
    }}

    /* For buttons - can keep the existing button styles or add additional styling */
    QPushButton {{
        background-color: {WHITE};
        color: {GREEN};
        font-family: "{FONT_FAMILY}";
        border: none;
        padding: 5px;
        border-radius: 3px;
    }}
    QPushButton:pressed {{
        background-color: {DARKWHITE};
    }}

    /* Style for QSlider (horizontal) */
    QSlider::groove:horizontal {{
        height: 8px;
        background: {DARKGREEN};
        margin: 2px 0;
        border-radius: 4px;
    }}

    QSlider::handle:horizontal {{
        background: {DARKGREY};
        border: 1px solid {DARKGREY};
        width: 18px;
        height: 18px;
        margin: -5px 0;  /* Adjusts the vertical alignment */
        border-radius: 9px;  /* Makes the handle circular */
    }}
    
    /* Style for QTabWidget and QTabBar */
    QTabWidget::pane {{
        border: 1px solid {DARKGREEN};
        background-color: {GREEN};
    }}

    QTabBar::tab {{
        background-color: {GREEN};
        color: {WHITE};
        font-family: "{FONT_FAMILY}";
        padding: 10px;
        border: 1px solid {DARKGREEN};
        border-bottom-color: {GREEN}; /* Remove bottom border */
    }}

    QTabBar::tab:selected {{
        background-color: {DARKGREEN};
        color: {WHITE};
        border: 1px solid {DARKGREEN};
        border-bottom-color: {DARKGREEN}; /* Match the background */
    }}

    QTabBar::tab:hover {{
        background-color: {DARKGREEN};
        color: {WHITE};
    }}

    #settingsWidget {{
        background-color: {GREEN};
        color: white;
        font-family: "{FONT_FAMILY}";
    }}
    """
    return style