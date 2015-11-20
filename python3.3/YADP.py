import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QInputDialog)
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
        license_button.clicked.connect(self.showLicense)
        box1 = QHBoxLayout()
        box1.addStretch(1)
        box1.addWidget(license_button)
        box1.addWidget(patch_button)
        box1.addWidget(exit_button)
        box2 = QVBoxLayout()
        box2.addStretch(1)
        box2.addLayout(box1)
        self.setLayout(box2)
        self.setGeometry(400, 400, 400, 150)
        self.setWindowTitle('YADP')
        self.show()

    def showLicense(self):
     # stuff here
    # Open new form w/ License

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = YADP_GUI()
    sys.exit(app.exec_())
