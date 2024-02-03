from PySide6.QtWidgets import QWidget,QListWidget,QAbstractItemView,QVBoxLayout,QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItem("One")
        self.list_widget.addItems(["Two","Three"])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        Button_add_item = QPushButton("Add Item")
        Button_add_item.clicked.connect(self.add_item)

        Button_delete_item = QPushButton("Delete Item")
        Button_delete_item.clicked.connect(self.delete_item)

        Button_item_count = QPushButton("Item Count")
        Button_item_count.clicked.connect(self.item_count)

        Button_selected_item = QPushButton("Selected Item")
        Button_selected_item.clicked.connect(self.selected_item)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(Button_add_item)
        v_layout.addWidget(Button_delete_item)
        v_layout.addWidget(Button_item_count)
        v_layout.addWidget(Button_selected_item)

        self.setLayout(v_layout)

    def current_item_changed(self,item):
        print(item.text())

    def current_text_changed(self,text):
        print(text)

    def add_item(self):
        self.list_widget.addItem("New Item")

    def delete_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def item_count(self):
        print(self.list_widget.count())

    def selected_item(self):
        lst = self.list_widget.selectedItems()
        print([i.text() for i in lst])

