from PySide6.QtWidgets import QWidget,QPushButton,QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Button")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def button_clicked(self):
        print("Clicked")

    def button_pressed(self):
        print("Pressed")

    def button_released(self):
        print("Released")
