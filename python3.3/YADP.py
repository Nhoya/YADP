import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QMessageBox, QFileDialog)
from PyQt5.QtCore import QCoreApplication

class YADP_GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        patch_button = QPushButton("Patch")

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(QCoreApplication.instance().quit)

        license_button = QPushButton("License")
        license_button.clicked.connect(self.showLicense)

        rom_path = QLineEdit(self)
        rom_path.resize(200, 30)
        rom_path.move(70, 10)

        xdelta_path = QLineEdit(self)
        xdelta_path.resize(200, 30)
        xdelta_path.move(70, 50)

        select_rom = QPushButton("Select", self)
        select_rom.move(290, 10)
        select_rom.setToolTip('Select <b>ROM</b> file')
        select_rom.clicked.connect(self.openRom)

        select_xdelta= QPushButton("Select",self)
        select_xdelta.move (290, 50)
        select_xdelta.setToolTip('Select <b>xdelta</b> file')
        select_xdelta.clicked.connect(self.openXdelta)

        lab1 = QLabel("ROM:", self)
        lab1.move(30,10)

        lab2 = QLabel("xdelta:",self)
        lab2.move(20,50)


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

    def openRom(self):
        rom = QFileDialog.getOpenFileName(self, "Select Rom")
        if rom:
            print (rom)

    def openXdelta(self):
        path = "/home/nhoya"
        xfile = QFileDialog.getOpenFileName(self, "Select xDelta patch file")
        if xfile:
            print (xfile)
            self.showXdelta(xfile) #showXdelta() takes 1 positional argument but 2 were given

    def showXdelta(self):
        self.xdelta_path.Text("xfile")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YADP_GUI()
    sys.exit(app.exec_())
