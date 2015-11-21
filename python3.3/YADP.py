import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QInputDialog, QMessageBox)
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
        hblayout = QHBoxLayout()
        hblayout.addStretch(1)
        hblayout.addWidget(license_button)
        hblayout.addWidget(patch_button)
        hblayout.addWidget(exit_button)
        vblayout = QVBoxLayout()
        vblayout.addStretch(1)
        vblayout.addLayout(hblayout)
        self.setLayout(vblayout)
        self.setGeometry(400, 400, 400, 150)
        self.setWindowTitle('YADP')
        self.show()

    def showLicense(self):
        QMessageBox.about(self, "YADP - License", "This program is free software: you can redistribute it and/or modify "
                                                  "it under the terms of the GNU General Public License as published by "
                                                  "the Free Software Foundation, either version 3 of the License, or"
                                                  "(at your option) any later version.\n\n"
                                                  "This program is distributed in the hope that it will be useful, "
                                                  "but without any warranty; without even the implied warranty of "
                                                  "merchantability or fitness for a particular purpose. See the "
                                                  "GNU General Public License for more details.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YADP_GUI()
    sys.exit(app.exec_())
