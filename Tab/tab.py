from PySide6.QtWidgets import QWidget,QLabel,QLineEdit,QTabWidget,QHBoxLayout,QVBoxLayout,QPushButton,QComboBox

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        tab_widget = QTabWidget(self)

        #form
        widget_form = QWidget()
        label_full_name = QLabel("FullName: ")
        line_edit_full_name = QLineEdit()
        h_layout = QHBoxLayout()
        h_layout.addWidget(label_full_name)
        h_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(h_layout)

        #buttons
        widget_button = QWidget()
        button1 = QPushButton("One")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        v_layout = QVBoxLayout()
        v_layout.addWidget(button1)
        v_layout.addWidget(button2)
        v_layout.addWidget(button3)
        widget_button.setLayout(v_layout)

        #combo
        widget_combo = QWidget()
        combo_box = QComboBox()
        combo_box.addItem("Earth")
        combo_box.addItem("Mars")
        combo_box.addItem("venus")
        box_layout = QVBoxLayout()
        box_layout.addWidget(combo_box)
        widget_combo.setLayout(box_layout)

        tab_widget.addTab(widget_form,"Form")
        tab_widget.addTab(widget_button,"Buttons")
        tab_widget.addTab(widget_combo,"Combo")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)


    def button1_clicked(self):
        print("button1_clicked")









