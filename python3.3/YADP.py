import sys, base64
from PyQt5.QtWidgets import (QWidget, QLabel,QProgressBar, QPushButton, QHBoxLayout, QVBoxLayout,QApplication, QLineEdit, QMessageBox, QFileDialog,
                             QFormLayout, QSizePolicy, QSpacerItem)
from PyQt5.QtCore import QCoreApplication


class YADP_GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.patch_button = QPushButton("Patch")
    #    self.patch_button.setEnabled(False)
        self.patch_button.clicked.connect(self.patchClicked)

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
        self.progressBar = QProgressBar(self)
        self.progressBar.hide()
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
        layout_bottom.addWidget(self.patch_button)
        layout_bottom.addWidget(exit_button)
        layout_bottom.addWidget(self.progressBar)



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
        rom = QFileDialog.getOpenFileName(self, "Select Rom", "", "All files (*.*);;*.iso")
        if rom:
           #print (rom[0])
            self.showRom(rom[0])

    def openXdelta(self):
        xfile = QFileDialog.getOpenFileName(self, "Select xDelta patch file","", "All files (*.*);;*.xdelta")
        if xfile:
            #print (xfile[0])
            self.showXdelta(xfile[0])
            self.showXdeltaFileDesc(xfile[0])

    def showXdelta(self, path):
        self.xdelta_path.setText(path)

    def showRom(self, rom):
        self.rom_path.setText(rom)


    def patchClicked(self):
        self.progressBar.setRange(0,0)
        self.progressBar.show()
        self.patch_button.setEnabled(False)


        rom = self.rom_path.text()
        xdelta_file = self.xdelta_path.text()

        if rom and xdelta_file:
            self.progressBar.show()
            print (rom)
            print (xdelta_file)
        else:
            self.progressBar.hide()
            conf = QMessageBox.question(self, 'Error',
            "Please select ROM and xdelta file before patching", QMessageBox.Ok)

            if conf == QMessageBox.Ok:
                self.patch_button.setEnabled(True)

    def showXdeltaFileDesc(self, xfile):
        f = open(xfile, 'rb')
        with f:
            byte = bytearray()
            length = 0

            f.seek(5)
            while True:
                size = length << 7
                byte = f.read(1)
                length = size | (byte[0] & 0x7F)

                if (byte[0] & 0x80) == 0:
                    break;

            if length == 0:
                return

            tmp = f.read(length)
            f.close()

            if int(tmp[0]) == 94 and int(tmp[1]) == 42:         # 94 = '^', 42 = '*'
                desc = tmp[2:]
                desc = base64.b64decode(desc)
                desc = desc.decode('utf-8')
                QMessageBox.about(self, "Description", desc)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YADP_GUI()
    sys.exit(app.exec_())
