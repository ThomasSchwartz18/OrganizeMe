# src/styles/themes.py

GREEN_THEME = {
    "background": "#EAF3E6",         # Corresponds to WHITE in your constants
    "text": "#5F5F5E",               # Corresponds to DARKGREY
    "button": "#979E73",             # GREEN
    "button_pressed": "#585C42",     # DARKGREEN
    "button_text": "#EAF3E6",         # WHITE (for text on buttons)
    "slider_groove": "#585C42",       # DARKGREEN
    "slider_handle": "#5F5F5E",       # DARKGREY
    "title_bar_bg": "#979E73",        # GREEN
    "title_bar_text": "#EAF3E6",      # WHITE
    "light_button_press": "#CCCEBD",  # LIGHT GREEN
}

PINK_THEME = {
    "background": "#F8E5E8",         # Corresponds to WHITE in your constants
    "text": "#5F5F5E",               # Corresponds to DARKGREY
    "button": "#F794D6",             # PINK
    "button_pressed": "#E368BA",     # DARKPINK
    "button_text": "#F8E5E8",         # WHITE (for text on buttons)
    "slider_groove": "#E368BA",       # DARKPINK
    "slider_handle": "#5F5F5E",       # DARKGREY
    "title_bar_bg": "#F794D6",        # PINK
    "title_bar_text": "#F8E5E8",      # WHITE
    "light_button_press": "#E37DC1",  # LIGHT PINK
}

# If you plan on having more themes, you can add them here:
AVAILABLE_THEMES = {
    "green": GREEN_THEME,
    "pink": PINK_THEME,
    # "dark": DARK_THEME,
    # "light": LIGHT_THEME,
}
