#aalesh
from PySide6.QtWidgets import QWidget,QApplication,QLineEdit
import sys
from PySide6.QtUiTools import QUiLoader
from pymongo import MongoClient
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

client = MongoClient("mongodb://localhost:27017")

def info_load():
    data = {"fullName":window.full_name_line_edit.text(),
            "age":window.age_line_edit.text(),
            "mobile":window.mobile_no_line_edit.text(),
            "email":window.email_line_edit.text(),
            "city":window.city_line_edit.text()}
    client.myDatabase.myCollection.insert_one(data)
    print(window.full_name_line_edit.text(), window.age_line_edit.text())


if __name__=="__main__":

    loader = QUiLoader()
    app = QApplication(sys.argv)
    window = loader.load("form_ui.ui", None)
    validator = QRegularExpressionValidator(QRegularExpression("[1-9]|[1-9][0-9]|1[0-4][0-9]|150"))
    window.age_line_edit.setValidator(validator)
    validator1 = QRegularExpressionValidator(QRegularExpression(r"\d{10}"))
    window.mobile_no_line_edit.setValidator(validator1)
    validator2 = QRegularExpressionValidator(QRegularExpression(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"))
    window.email_line_edit.setValidator(validator2)
    validator3 = QRegularExpressionValidator(QRegularExpression(r"[A-Za-z]+"))
    window.city_line_edit.setValidator(validator3)
    window.submit_button.clicked.connect(info_load)
    window.mobile_no_line_edit.setEchoMode(QLineEdit.Password)
    window.show()
    app.exec()