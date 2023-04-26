'''Ahmad Project_plot GUI
version 1.0.1'''

#Importing libs
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget
from PyQt5.QtWidgets import QFileDialog
import logging
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plot 1D Signal")
        self.setGeometry(50,50,1000,600)
        self.UI()



    def UI(self):
        # defining font size for axis
        font_axis = QtGui.QFont()
        font_axis = QtGui.QFont("Times New Roman")
        font_axis.setPixelSize(18)
        labelStyle = {'font-size': '12pt'}

        self.GroupBox1 = QtWidgets.QGroupBox('Plot')
        font_g1 = QtGui.QFont()
        font_g1.setPointSize(14)
        font_g1.setBold(True)
        font_g1.setWeight(50)
        self.GroupBox1.setFont(font_g1)
        self.Previews = QtWidgets.QGridLayout()

        # self.frog_preview = GraphicsLayoutWidget()
        self.plot_preview = pg.PlotWidget()
        self.plot_preview.setBackground('black')
        self.plot_preview.setObjectName("plot_preview")
        self.plot_preview.getAxis('left').setLabel('Intensity[arb]', color='#ffffff', **labelStyle)
        self.plot_preview.getAxis('bottom').setLabel('Wavelength[nm]', color='#ffffff', **labelStyle)
        self.plot_preview.getAxis("bottom").tickFont = font_axis
        self.plot_preview.getAxis("bottom").setStyle(tickFont=font_axis)
        self.plot_preview.getAxis("left").tickFocolont = font_axis
        self.plot_preview.getAxis("left").setStyle(tickFont=font_axis)
        self.plot_preview.getAxis('bottom').setTextPen("w")
        self.plot_preview.getAxis('bottom').setPen('w')
        self.plot_preview.getAxis('left').setTextPen("w")
        self.plot_preview.getAxis('left').setPen('w')
        self.Previews.addWidget(self.plot_preview)
        self.GroupBox1.setLayout(self.Previews)



        self.GroupBox2 = QtWidgets.QGroupBox('Importing')
        font_g2 = QtGui.QFont()
        font_g2.setPointSize(14)
        font_g2.setBold(True)
        font_g2.setWeight(50)
        self.GroupBox2.setFont(font_g2)
        self.importing = QtWidgets.QVBoxLayout()
        self.file_selector = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.file_selector.setFont(font)
        self.file_selector.setStyleSheet("background-color:red")
        self.file_selector.setObjectName(("file_selector"))
        spacerItemi = QtWidgets.QSpacerItem(4, 4)
        self.file_selector.setMinimumHeight(70)
        self.file_selector.setMaximumHeight(70)

        self.wl_max_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.wl_max_label.setFont(font)
        self.wl_max_label.setScaledContents(False)
        self.wl_max_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wl_max_label.setIndent(0)
        self.wl_max_label.setObjectName(("wl_max_label"))

        self.wl_max = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.wl_max.setFont(font)
        self.wl_max.setAlignment(QtCore.Qt.AlignCenter)
        self.wl_max.setObjectName(("wl_max"))

        self.peak_wl = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.peak_wl.setFont(font)
        self.peak_wl.setScaledContents(False)
        self.peak_wl.setAlignment(QtCore.Qt.AlignCenter)
        self.peak_wl.setIndent(0)
        self.peak_wl.setObjectName(("peak_wl"))

        self.peak_wl_val = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        self.peak_wl_val.setFont(font)
        self.peak_wl_val.setAlignment(QtCore.Qt.AlignCenter)
        self.peak_wl_val.setObjectName(("peak_wl_val"))

        self.wl_min_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        self.wl_min_label.setFont(font)
        self.wl_min_label.setScaledContents(False)
        self.wl_min_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wl_min_label.setIndent(0)
        self.wl_min_label.setObjectName(("wl_min_label"))

        self.wl_min = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        self.wl_min.setFont(font)
        self.wl_min.setAlignment(QtCore.Qt.AlignCenter)
        self.wl_min.setObjectName(("wl_min"))

        self.peak = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        self.peak.setFont(font)
        self.peak.setScaledContents(False)
        self.peak.setAlignment(QtCore.Qt.AlignCenter)
        self.peak.setIndent(0)
        self.peak.setObjectName(("peak"))

        self.peak_entry = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        self.peak_entry.setFont(font)
        self.peak_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.peak_entry.setObjectName(("peak_entry"))

        self.importing.addWidget(self.file_selector)
        self.importing.addWidget(self.wl_max_label)
        self.importing.addWidget(self.wl_max)
        self.importing.addWidget(self.wl_min_label)
        self.importing.addWidget(self.wl_min)
        self.importing.addWidget(self.peak_wl)
        self.importing.addWidget(self.peak_wl_val)
        self.importing.addWidget(self.peak)
        self.importing.addWidget(self.peak_entry)
        spacerItemstartfreq = QtWidgets.QSpacerItem(4, 20)
        self.importing.addItem(spacerItemstartfreq)

        self.file_selector.setText("Select File")
        self.wl_max_label.setText(( "Wavelength Max[nm]"))
        self.wl_min_label.setText(("Wavelength Min[nm]"))
        self.peak_wl.setText(("Peak Wavelength[nm]"))
        self.peak.setText(("Peak Value"))
        self.GroupBox2.setLayout(self.importing)

        self.Grid_main = QtWidgets.QGridLayout()
        self.Grid_main.addWidget(self.GroupBox1, 0, 0,5,5)
        self.Grid_main.addWidget(self.GroupBox2,0,5,5,3)
        self.setLayout(self.Grid_main)
        self.file_selector.clicked.connect(self.selectfileclicked)

    def load_data_from_file(self, filename):

        try:
            with open(filename, 'r') as data_file:
                wavelengths = []
                spectra = []
                for line in data_file:
                    p = line.split()
                    wavelengths.append(float(p[0]))
                    spectra.append(float(p[1]))

            return np.array(wavelengths), np.array(spectra)
        except:
            pass
 
    def selectfileclicked(self):

        selected_text = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.wavelength, self.intensity = self.load_data_from_file(selected_text)
        self.wl_min.setText(str(np.amin(self.wavelength)))
        self.wl_max.setText(str(np.amax(self.wavelength)))
        self.peak_wl_val.setText(str(self.wavelength[np.argmax(self.intensity)]))
        self.peak_entry.setText(str(np.max(self.intensity)))
        self.plot_preview.plot(self.wavelength, self.intensity)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())



