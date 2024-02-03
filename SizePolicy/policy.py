from PySide6.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit,QHBoxLayout,QSizePolicy

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Some Text: ")
        line_edit = QLineEdit()

        line_edit.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)

        button1 = QPushButton("Button1")
        button2 = QPushButton("Button1")
        button3 = QPushButton("Button1")

        layout = QHBoxLayout()
        layout.addWidget(button1,2)
        layout.addWidget(button2,1)
        layout.addWidget(button3,1)

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(layout)

        self.setLayout(v_layout)

