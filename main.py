from PyQt6.QtWidgets import QApplication
import sys
from layouts.start_page import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())