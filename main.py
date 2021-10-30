import string
import sys
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMainWindow, QLCDNumber,QFileDialog

import pic2txt
import convert

class Example(QMainWindow, pic2txt.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.openfile_basic)
        self.pushButton_3.clicked.connect(self.textBrowser.clear)
        self.setFixedSize(self.width(),self.height())
        self.pushButton_4.clicked.connect(self.openfile_handwrite)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def openfile_basic(self):
        fileName = QFileDialog.getOpenFileName()
        # print(fileName[0])
        ocrText = convert.ocr_basic(fileName[0])
        self.textBrowser.clear()
        self.textBrowser.append(ocrText)

    def openfile_handwrite(self):
        fileName = QFileDialog.getOpenFileName()
        # print(fileName[0])
        ocrText = convert.ocr_handwrite(fileName[0])
        self.textBrowser.clear()
        self.textBrowser.append(ocrText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
