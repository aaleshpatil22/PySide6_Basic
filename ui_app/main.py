from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from app_uii import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowIcon(r"C:/Users/Aalesh/PycharmProjects/pythonProject/ui_app/images/quitIcon.png")
        self.setWindowTitle("MyApp")
        self.actionQuit.triggered.connect(self.quit)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.aboutQt)

    def quit(self):
        self.app.quit()

    def copy(self):
        self.textEdit.copy()

    def cut(self):
        self.textEdit.cut()

    def paste(self):
        self.textEdit.paste()

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def about(self):
        QMessageBox.information(self, "App Info", "This Application Developed by Aalesh Patil\nApplication Version: 1.0.0")

    def aboutQt(self):
        QApplication.aboutQt()


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    app.exec()