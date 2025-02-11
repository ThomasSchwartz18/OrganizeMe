# src/styles.py

from PyQt5.QtGui import QFontDatabase

# Define your custom colors
GREEN     = "#979E73"
DARKGREEN = "#585C42"
WHITE     = "#EAF3E6"
DARKWHITE = "#D3DCCF"
BLACK     = "#040404"
TAN       = "#CAC6B6"
GREY      = "#AAA9A8"
DARKGREY  = "#5F5F5E"

# Define the path to your custom font
FONT_PATH = "../assets/fonts/Comme/static/Comme-ExtraBold.ttf"

def get_global_style():
    """
    Loads the custom font (after QApplication is created) and returns the global style sheet string.
    """
    # Load the custom font now that QApplication exists.
    font_id = QFontDatabase.addApplicationFont(FONT_PATH)
    if font_id != -1:
        FONT_FAMILY = QFontDatabase.applicationFontFamilies(font_id)[0]
    else:
        FONT_FAMILY = "Sans Serif"

    # Global style sheet string.
    global_style = f"""
    /* Global widget styling */
    QWidget {{
        background-color: {WHITE};
        font-family: "{FONT_FAMILY}";
        color: {DARKGREY};
    }}

    /* QPushButton styling */
    QPushButton {{
        background-color: {GREEN};
        color: {WHITE};
        font-family: "{FONT_FAMILY}";
        border: none;
        padding: 5px;
        border-radius: 3px;
    }}
    QPushButton:pressed {{
        background-color: {DARKGREEN};
    }}

    /* QLabel styling */
    QLabel {{
        color: {DARKGREY};
        font-family: "{FONT_FAMILY}";
    }}
    """
    return global_style
