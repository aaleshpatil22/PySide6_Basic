from PySide6.QtWidgets import QWidget,QCheckBox,QGroupBox,QVBoxLayout,QHBoxLayout,QRadioButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        os = QGroupBox("OS")
        window = QCheckBox("Window")
        window.toggled.connect(self.window_clicked)
        linux = QCheckBox("Linux")
        mac = QCheckBox("Mac")
        linux.setChecked(True)
        v_layout = QVBoxLayout()
        v_layout.addWidget(window)
        v_layout.addWidget(linux)
        v_layout.addWidget(mac)
        os.setLayout(v_layout)


        drink = QGroupBox("Drinks")
        water = QRadioButton("Water")
        tea = QRadioButton("Tea")
        coffee = QRadioButton("Coffee")
        water.setChecked(True)
        lout = QVBoxLayout()
        lout.addWidget(water)
        lout.addWidget(tea)
        lout.addWidget(coffee)
        drink.setLayout(lout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drink)
        self.setLayout(h_layout)

    def window_clicked(self):
        print("Window Clicked")


