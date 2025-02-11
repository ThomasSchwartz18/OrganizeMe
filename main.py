import sys
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.styles.application_styles import get_global_style  # Import the function

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(get_global_style())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
