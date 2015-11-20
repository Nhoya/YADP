import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtCore import QCoreApplication


class YADP_GUI(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        patch_button = QPushButton("Patch")
        exit_button = QPushButton("Exit")
        license_button = QPushButton("License")
        exit_button.clicked.connect(QCoreApplication.instance().quit);
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(license_button)
        hbox.addWidget(patch_button)
        hbox.addWidget(exit_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(400, 400, 400, 150)
        self.setWindowTitle('YADP')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = YADP_GUI()
    sys.exit(app.exec_())
