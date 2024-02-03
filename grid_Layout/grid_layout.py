from PySide6.QtWidgets import QWidget,QPushButton,QGridLayout,QSizePolicy

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        button3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button4 = QPushButton("Button4")
        button5 = QPushButton("Button5")
        button6 = QPushButton("Button6")
        button7 = QPushButton("Button7")

        layout = QGridLayout()
        layout.addWidget(button1,0,0)
        layout.addWidget(button2,0,1,1,2)
        layout.addWidget(button3,1,0,2,1)
        layout.addWidget(button4,1,1)
        layout.addWidget(button5,1,2)
        layout.addWidget(button6,2,1)
        layout.addWidget(button7,2,2)

        self.setLayout(layout)

