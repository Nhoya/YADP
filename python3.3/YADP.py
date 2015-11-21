import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QMessageBox, QFileDialog,
                             QFormLayout, QSizePolicy, QSpacerItem)
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

        layout_upper = QVBoxLayout()
        layout_rom = QHBoxLayout()
        layout_xdelta = QHBoxLayout()
        self.rom_path = QLineEdit(self)
        self.rom_path.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.rom_label = QLabel("Rom path")
        self.rom_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        select_rom = QPushButton("Select", self)
        select_rom.setToolTip('Select <b>ROM</b> file')
        select_rom.clicked.connect(self.openRom)
        self.xdelta_path = QLineEdit(self)
        self.xdelta_label = QLabel("Xdelta path")
        select_xdelta = QPushButton("Select",self)
        select_xdelta.setToolTip('Select <b>xdelta</b> file')
        select_xdelta.clicked.connect(self.openXdelta)
        layout_xdelta.addWidget(self.xdelta_label)
        layout_xdelta.addWidget(self.xdelta_path)
        layout_xdelta.addWidget(select_xdelta)
        layout_rom.addWidget(self.rom_label)
        layout_rom.addWidget(self.rom_path)
        layout_rom.addWidget(select_rom)
        layout_upper.addLayout(layout_rom)
        layout_upper.addLayout(layout_xdelta)

        layout_bottom = QHBoxLayout()
        layout_bottom.addWidget(license_button)
        layout_bottom.addWidget(patch_button)
        layout_bottom.addWidget(exit_button)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_upper)
        layout_main.addLayout(layout_bottom)
        self.setLayout(layout_main)
        self.setMaximumHeight(150)
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
            print (rom[0])

    def openXdelta(self):
        xfile = QFileDialog.getOpenFileName(self, "Select xDelta patch file")
        if xfile:
            print (xfile[0])
            self.showXdelta(xfile[0]) #showXdelta() takes 1 positional argument but 2 were given

    def showXdelta(self, path):
        self.xdelta_path.setText(path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YADP_GUI()
    sys.exit(app.exec_())
