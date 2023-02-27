import sys
from mfc_designer_class import Example
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec())
    except Exception as e:
        print(e)
