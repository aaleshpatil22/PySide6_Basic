from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QLineEdit,QVBoxLayout,QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        lable = QLabel("FullName : ")
        self.line_edit = QLineEdit()
        #self.line_edit.textChanged.connect(self.text_changed)
        #self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        #self.line_edit.editingFinished.connect(self.editing_finished)
        #self.line_edit.returnPressed.connect(self.return_pressed)
        #self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab Data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_lable = QLabel("I am here")

        h_layout = QHBoxLayout()
        h_layout.addWidget(lable)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_lable)
        self.setLayout(v_layout)

    def button_clicked(self):
        #print("FullName : ",self.line_edit.text())
        self.text_holder_lable.setText(self.line_edit.text())

    def text_changed(self):
        self.text_holder_lable.setText(self.line_edit.text())

    def cursor_position_changed(self,old,new):
        print("Old: ",old,"New: ",new)

    def editing_finished(self):
        print("Editing Finished")

    def return_pressed(self):
        print("Return Pressed")

    def selection_changed(self):
        print("selection_changed",self.line_edit.selectedText())

    def text_edited(self,text):
        print("text_edited",text)







