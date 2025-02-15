from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from src.styles.title_bar_style import get_title_bar_style  # Import the style function

class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent  # Reference to the main window
        self.setFixedHeight(40)  # Increase the height to accommodate the larger logo

        # Apply the title bar style (green background)
        self.setStyleSheet(get_title_bar_style())

        # Create the layout for the title bar
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 0, 10, 0)

        # Create a label for the logo
        self.logo_label = QLabel()
        self.logo_label.setStyleSheet("background: transparent;")  # Ensure no background is painted behind the logo

        # Add a stretch so that the buttons appear at the right edge
        self.layout.addStretch()

        # Create a settings button with a gear icon
        self.settings_button = QPushButton("⚙")
        self.settings_button.setFixedSize(20, 20)
        self.settings_button.clicked.connect(self.parent.open_settings)
        self.layout.addWidget(self.settings_button)

        # Create a minimize button
        self.minimize_button = QPushButton("-")
        self.minimize_button.setFixedSize(20, 20)
        self.minimize_button.clicked.connect(self.parent.showMinimized)
        self.layout.addWidget(self.minimize_button)

        # Create a close button
        self.close_button = QPushButton("x")
        self.close_button.setFixedSize(20, 20)
        self.close_button.clicked.connect(self.parent.close)
        self.layout.addWidget(self.close_button)

        # Variables to help with dragging the window
        self._is_dragging = False
        self._drag_position = QPoint(0, 0)

    def mousePressEvent(self, event):
        """Start tracking for window drag on left-click."""
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            # Record the position where the mouse was pressed (global position relative to the window)
            self._drag_position = event.globalPos() - self.parent.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        """Move the window if dragging."""
        if self._is_dragging and event.buttons() & Qt.LeftButton:
            self.parent.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Stop dragging."""
        self._is_dragging = False
        event.accept()

    def setTitle(self, title):
        """Update the title text (if needed)."""
        pass  # Not used since the logo replaces the title text