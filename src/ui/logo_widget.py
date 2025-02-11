# src/ui/logo_widget.py

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class LogoWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Allow the logo widget to be transparent (except for the image)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # Allow mouse events to pass through (so it doesn’t block interaction underneath)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        
        # Load the logo image (adjust the path if necessary)
        pixmap = QPixmap("assets/images/logo.svg")
        if not pixmap.isNull():
            # Scale the pixmap to the desired height (for example, 50 pixels)
            scaled_pixmap = pixmap.scaledToHeight(65, Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
            # Resize the widget to match the pixmap size
            self.resize(scaled_pixmap.size())
        else:
            self.setText("Logo")
