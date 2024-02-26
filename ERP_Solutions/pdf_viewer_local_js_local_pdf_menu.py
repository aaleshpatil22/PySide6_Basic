import sys
import math
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QLabel,QComboBox,QDateEdit,QGridLayout,QPushButton,QSizePolicy,QLineEdit,QFrame
from PySide6.QtCore import QUrl
from PySide6.QtGui import QAction
from PySide6.QtWebEngineWidgets import QWebEngineView
from matplotlib.backends.backend_pdf import PdfPages
from PySide6.QtCore import Qt, QDate
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import duckdb

class PdfViewerWidget(QWidget):

    def __init__(self, pdfjs_path):
        super().__init__()
        self.lst = []
        
        layout = QVBoxLayout(self)
        hlayout = QGridLayout(self)
        glayout = QGridLayout(self)
        
        self.date_label = QLabel("Date:")
        self.date_input = QDateEdit(self)
        self.date_input.setDate(QDate.currentDate())

        self.product_label = QLabel("Product:")
        self.product_combobox = QComboBox(self)
        self.product_combobox.addItems(['milk', 'butter', 'ghee', 'cheese', 'paneer'])
        
        
        self.weight_label = QLabel("Weight(gm/ml):")
        self.weight_input = QLineEdit(self)

        self.quantity_label = QLabel("Quantity:")
        self.quantity_input = QLineEdit(self)

        self.add_item_button = QPushButton("Add Item", self)
        self.add_item_button.clicked.connect(self.add_item)

        self.calculate_button = QPushButton("Calculate Total", self)
        self.calculate_button.clicked.connect(self.calculate_total)
        
        glayout.addWidget(self.date_label,0,0,1,1)
        glayout.addWidget(self.date_input,0,1,1,1)
        glayout.addWidget(self.product_label,0,2,1,1)
        glayout.addWidget(self.product_combobox,0,3,1,1)
        glayout.addWidget(self.weight_label,0,4,1,1)
        glayout.addWidget(self.weight_input,0,5,1,1)
        glayout.addWidget(self.quantity_label,0,6,1,1)
        glayout.addWidget(self.quantity_input,0,7,1,1)
        glayout.addWidget(self.add_item_button,0,8,1,1)
        glayout.addWidget(self.calculate_button,0,9,1,1)
        
        
        self.sales_group_label = QLabel("Sales Group")
        self.sales_group_box = QComboBox(self)
        self.sales_group_box.addItems(['Dairy-1', 'Dairy-2', 'Dairy-3', 'Dairy-4', 'Dairy-5'])
        
        self.from_date_label = QLabel("From:")
        self.from_date_input = QDateEdit(self)
        self.from_date_input.setDate(QDate.currentDate())
        
        self.to_date_label = QLabel("To:")
        self.to_date_input = QDateEdit(self)
        self.to_date_input.setDate(QDate.currentDate())
        
        self.item_group_label = QLabel("Item Group")
        self.item_group_box = QComboBox(self)
        self.item_group_box.addItems(['milk', 'butter', 'ghee', 'cheese', 'paneer','all'])
        
        self.show_button = QPushButton("Show")
        self.show_button.clicked.connect(self.show)
        self.show_button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        
        hlayout.addWidget(self.sales_group_label,0,0,1,1)
        hlayout.addWidget(self.sales_group_box,0,1,1,3)
        
        hlayout.addWidget(self.from_date_label,0,4,1,1)
        hlayout.addWidget(self.from_date_input,0,5,1,4)
        hlayout.addWidget(self.to_date_label,0,9,1,1)
        hlayout.addWidget(self.to_date_input,0,10,1,4)
        
        hlayout.addWidget(self.item_group_label,1,0,1,1)
        hlayout.addWidget(self.item_group_box,1,1,1,13)
        hlayout.addWidget(self.show_button,0,14,2,2)
        
        self.webview = QWebEngineView()
        local_url = QUrl.fromLocalFile(pdfjs_path).toString()
        self.webview.load(QUrl(local_url))
        
        layout.addLayout(glayout)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setLineWidth(2)
        line.setFixedHeight(20)
        layout.addWidget(line)
        layout.addLayout(hlayout)
        layout.addWidget(self.webview)

        def on_load_finished(ok):
            if ok and self.pdf_file:
                file_url = QUrl.fromLocalFile(self.pdf_file).toString()
                self.webview.page().runJavaScript(
                    f"PDFViewerApplication.open({{'url': '{file_url}'}});"
                )

        self.webview.loadFinished.connect(on_load_finished)

        self.pdf_file = None
    
    def add_item(self):
        try:
            self.product_dic ={'milk':80, 'butter':400, 'ghee':600, 'cheese':500, 'paneer':350}
            selected_date = self.date_input.date().toString(Qt.ISODate)
            date_format = '%Y-%m-%d'
            selected_date = datetime.strptime(selected_date, date_format).date()
            product = self.product_combobox.currentText()
            weight_str = self.weight_input.text()
            quantity_str = self.quantity_input.text()
            cost_str = math.ceil(self.product_dic[product]*(int(weight_str)/1000))
            
            data={"Date":selected_date,"Product":product,"Weight(gm/ml)":int(weight_str),"Quantity":int(quantity_str),"Cost/qty":int(cost_str),"Net Total":int(int(quantity_str)*int(cost_str)),"GST(18%)":int(int(quantity_str)*int(cost_str)*0.18),"Gross Total":int(int(quantity_str)*int(cost_str)*1.18)}
            self.lst.append(data)
            
            self.date_input.setDate(QDate.currentDate())
            self.product_combobox.setCurrentIndex(0)
            self.weight_input.clear()
            self.quantity_input.clear()
        except Exception as inst:
            print("error is ",inst)

    def calculate_total(self):
        try:
            df = pd.DataFrame(self.lst)
            self.lst=[]
            db_file_path = str(Path.home() / 'pdfjs' / 'duckdb' / 'example_database.db')
            # Establish a connection to DuckDB and create a disk-based database
            connection = duckdb.connect(database=db_file_path, read_only=False)
            df.to_sql(name='dairy',con=connection,index=False,if_exists='append')
            
            connection.close()
            total = ["Total","","",int(sum(df["Quantity"])),"",int(sum(df["Net Total"])),int(sum(df["GST(18%)"])),int(sum(df["Gross Total"]))]
                        
            df.loc[len(df)] = total
            
            fig, ax = plt.subplots(figsize=(8.27, 11.69), dpi=100)            
            fig.figure.tight_layout()
            
            ax.text(0.5, 0.95, 'ERP SOLUTIONS Pvt. Ltd.', fontsize=18, ha='center', va='center')
            ax.text(0.1, 0.9, f"Print Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", fontsize=8, ha='center', va='center')
            
            height =0.015*(len(df))+0.015
            ax.table(cellText=df.values,
                     colLabels=df.columns,
                     loc='center',
                     colWidths=[1 / df.columns.size] * df.columns.size,
                     bbox=[0, 1-height-0.15, 1,height] # [left, bottom, width, height]
                     )
            
            ax.axis('off')
            # Replace 'output_file.pdf' with your desired output file name
            path = Path.home() / 'pdfjs' / 'doc' / 'tax_invoice' / f"tax_invoice_{datetime.now().strftime('%d%m%Y%H%M%S')}.pdf"
            plt.savefig(path, format='pdf')
            self.pdf_file = path
            self.webview.reload()
                        
        except Exception as inst:
            print("error is ",inst)
        
    def make_pdf(self,path,df_result):
        with PdfPages(path) as pdf:
            if len(df_result)==1:
                    fig, ax = plt.subplots(figsize=(8.27, 11.69), dpi=100)  # Adjust as needed
                    
                    fig.tight_layout()
                    
                    ax.text(0.5, 0.98, 'ERP SOLUTIONS Pvt. Ltd.', fontsize=18, ha='center', va='center')
            
                    ax.text(0.5, 0.95, f"From Date {self.from_date_input.date().toString(Qt.ISODate)} To {self.to_date_input.date().toString(Qt.ISODate)}", fontsize=8, ha='center', va='center')
                        
                    ax.text(0.5, 0.93, f"Stock Statement Report of {self.sales_group_box.currentText()} For Item {self.item_group_box.currentText()}", fontsize=8, ha='center', va='center')
                        
                    ax.text(0.1, 0.90, f"Print Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", fontsize=8, ha='center', va='center')
                    
                    ax.table(cellText=[["", "", "", "", "", "", "", ""]],
                             colLabels=df_result.columns,
                             cellLoc='center',
                             loc='center',
                             bbox=[0, 0.80,1, 0.03]  # [left, bottom, width, height]
                             )
                  # Adjust font size as needed
                    ax.axis('off')
                    pdf.savefig(fig)
                    plt.close(fig)
                                    
            start_row = 0
            nrows=56
            while start_row < len(df_result):
                end_row = start_row + nrows
                page_df = df_result.iloc[start_row:end_row]

                try:
                    
                    fig, ax = plt.subplots(figsize=(8.27, 11.69), dpi=100)  # Adjust as needed
                    
                    fig.tight_layout()
                    
                    if start_row==0:
                    
                        ax.text(0.5, 0.98, 'ERP SOLUTIONS Pvt. Ltd.', fontsize=18, ha='center', va='center')
                
                        ax.text(0.5, 0.95, f"From Date {self.from_date_input.date().toString(Qt.ISODate)} To {self.to_date_input.date().toString(Qt.ISODate)}", fontsize=8, ha='center', va='center')
                            
                        ax.text(0.5, 0.93, f"Stock Statement Report of {self.sales_group_box.currentText()} For Item {self.item_group_box.currentText()}", fontsize=8, ha='center', va='center')
                            
                        ax.text(0.1, 0.90, f"Print Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", fontsize=8, ha='center', va='center')
                        
                        nrows=62                        
                    # Apply styling if provided
                    if len(page_df) ==62 or len(page_df)==56:
                        height =0.015*(len(page_df))+0.015
                        ax.table(
                                cellText=page_df.values,
                                colLabels=page_df.columns,
                                loc='center',
                                colWidths=[1 / df_result.columns.size] * df_result.columns.size,
                                bbox=[0,0.015, 1,height] # [left, bottom, width, height]
                            )
                    else:
                        if start_row==0:
                            height =0.015*(len(page_df))+0.015
                            ax.table(
                                    cellText=page_df.values,
                                    colLabels=page_df.columns,
                                    loc='center',
                                    colWidths=[1 / df_result.columns.size] * df_result.columns.size,
                                    bbox=[0, 1-height-0.15, 1,height] # [left, bottom, width, height]
                                )
                        else:
                            height =0.015*(len(page_df))+0.015
                            ax.table(
                                    cellText=page_df.values,
                                    colLabels=page_df.columns,
                                    loc='center',
                                    colWidths=[1 / df_result.columns.size] * df_result.columns.size,
                                    bbox=[0, 1-height-0.03, 1,height] # [left, bottom, width, height]
                                )                        
                    
                    ax.axis('off')
                    pdf.savefig(fig)
                    plt.close(fig)

                except Exception as e:
                    print(e)

                start_row = end_row
            
        self.pdf_file = path
        self.webview.reload()
                
    def show(self):
        
        self.from_date = self.from_date_input.date().toString(Qt.ISODate)
        self.to_date = self.to_date_input.date().toString(Qt.ISODate)
            
        db_file_path = str(Path.home() / 'pdfjs' / 'duckdb' / 'example_database.db')
        # Establish a connection to DuckDB and create a disk-based database
        connection = duckdb.connect(database=db_file_path, read_only=False)

        # Execute a query to fetch data from the table (just for verification)   
        item_str = ''
        if self.item_group_box.currentText() in ['milk', 'butter', 'ghee', 'cheese', 'paneer']:
            item_str = f"('{self.item_group_box.currentText()}')"
        else:
            item_str =  "('milk', 'butter', 'ghee', 'cheese', 'paneer')"      
        
        query_result = connection.execute(f"select * from dairy where date between '{self.from_date}' and '{self.to_date}' and Product in {item_str} order by Date Desc")
        rows = query_result.fetchall()
        # Get the column names from the query result description
        columns = [column[0] for column in query_result.description]
        # Create a DataFrame using the fetched rows and column names
        df_result = pd.DataFrame(rows, columns=columns)
        
        total = ["Total","","",int(sum(df_result["Quantity"])),"",int(sum(df_result["Net Total"])),int(sum(df_result["GST(18%)"])),int(sum(df_result["Gross Total"]))]
        
        df_result.loc[len(df_result)] = total
           
        path = Path.home() / 'pdfjs' / 'doc' /'record'/ f'{datetime.now().strftime("%d%m%Y%H%M%S")}.pdf'
        self.make_pdf(path,df_result)
                
    def open_pdf(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open PDF File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        path1 = str(Path.home() / 'pdfjs'/ 'doc')
        file_dialog.setDirectory(path1)
                
        if file_dialog.exec_() == QFileDialog.Accepted:
            self.pdf_file = file_dialog.selectedFiles()[0]
            self.webview.reload()

class PdfViewerApp(QMainWindow):

    def __init__(self, pdfjs_path):
        super().__init__()

        self.viewer = PdfViewerWidget(pdfjs_path)
        self.setCentralWidget(self.viewer)

        self.create_menu_bar()

        # Set the title and icon
        self.setWindowTitle("ERP Invoice & Transaction Detail")

    def create_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QAction("Open PDF...", self)
        open_action.triggered.connect(self.viewer.open_pdf)
        file_menu.addAction(open_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Make sure you replace this path with the path to your local PDF.js 'viewer.html' file
    pdfjs_path = Path.home() / 'pdfjs' / 'web' / 'viewer.html'
    main_win = PdfViewerApp(pdfjs_path)
    main_win.show()
    sys.exit(app.exec())