# src/ui/logo_widget.py

import os
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from src.config import SETTINGS  # To read the current theme

class LogoWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Allow the logo widget to be transparent (except for the image)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Allow mouse events to pass through (so it doesn’t block interaction underneath)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        
        # Load the logo image based on the current theme
        self.updateLogo()

    def updateLogo(self):
        """Load the appropriate logo image based on the current theme."""
        # Get the current theme from SETTINGS (default to 'green')
        theme = SETTINGS.get("theme", "green").lower()
        # Determine the logo file based on the theme
        if theme == "pink":
            logo_file = "logo-pink.svg"
        else:
            logo_file = "logo-green.svg"
        
        # Build the absolute path to the logo file
        logo_path = os.path.join("assets", "images", "logo", logo_file)
        
        # Load and apply the pixmap
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            # Scale the pixmap to the desired height (for example, 65 pixels)
            scaled_pixmap = pixmap.scaledToHeight(65, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
            # Resize the widget to match the pixmap size
            self.resize(scaled_pixmap.size())
        else:
            self.setText("Logo")
