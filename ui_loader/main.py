import sys
from PySide6.QtWidgets import QWidget,QApplication
from ui_widget import Ui_Widget
from pymongo import MongoClient

class window(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MyApp")
        self.submit_button.clicked.connect(self.do_something)
        self.client = MongoClient("mongodb://localhost:27017")

    def do_something(self):
        data = {"fullName":self.full_name_line_edit.text(),"occupation":self.occupation_line_edit.text()}
        self.client.myDatabase.myCollection.insert_one(data)
        print("FullName is",self.full_name_line_edit.text(), "Occupation is", self.occupation_line_edit.text())


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = window()
    window.show()
    app.exec()
