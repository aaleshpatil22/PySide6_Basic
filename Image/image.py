from PySide6.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QHBoxLayout
from PySide6.QtGui import QPixmap
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("C:/Users/Aalesh/Downloads/download.jpeg"))

        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)

        self.setLayout(v_layout)
