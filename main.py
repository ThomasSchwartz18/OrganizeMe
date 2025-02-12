import sys
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.styles.application_styles import get_global_style  # Import the function
from PyQt5.QtGui import QFont

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set the entire application's default font to Segoe UI with a specific point size.
    app.setFont(QFont("Segoe UI", 12))
    
    app.setStyleSheet(get_global_style())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
