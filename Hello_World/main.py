from PySide6.QtWidgets import QApplication
import sys
from hello_world import Widget


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    app.exec()