from PySide6.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QTextEdit,QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.text_edit = QTextEdit()

        current_text_button = QPushButton("Current Text")
        current_text_button.clicked.connect(self.current_text_button_clicked)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redu")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("Set HTML")
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def current_text_button_clicked(self):
        print(self.text_edit.toPlainText())

    def set_plain_text(self):
        self.text_edit.setPlainText("""In the heart of Serenity Springs stood a centuries-old oak tree, its branches reaching out like wise old arms, cradling the stories of generations past. Underneath its leafy canopy, the townsfolk gathered for community events, sharing laughter, tales, and the simple joys of life.""")

    def set_html(self):
        self.text_edit.setHtml("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            text-align: center;
        }
        h1 {
            color: #3366cc;
        }
        p {
            color: #333;
        }
    </style>
</head>
<body>

    <header>
        <h1>Welcome to My Sample HTML Page</h1>
    </header>

    <main>
        <section>
            <p>This is a simple example of an HTML page. You can use this as a starting point and build upon it for your projects.</p>
        </section>

        <section>
            <h2>Features</h2>
            <ul>
                <li>Structured with HTML5</li>
                <li>Styled with CSS</li>
                <li>Ready for content</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Your Website Name. All rights reserved.</p>
    </footer>

</body>
</html>
""")
