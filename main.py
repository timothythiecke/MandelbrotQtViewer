# Based on code from https://pythonprogramminglanguage.com/pyqt5-hello-world/

import sys
import PyQt5.QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QImage, QColor
from PyQt5.QtCore import QSize   

class MandelbrotWindow(QMainWindow): # Python inheritance
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("MandelbrotQtViewer") 
        
        pixmap = QPixmap(640, 480).toImage()
        pixmap.fill(PyQt5.QtGui.QColor.fromRgb(255, 255, 255))
        
        for i in range(300):
            pixmap.setPixelColor(i, i, PyQt5.QtGui.QColor.fromRgb(255, 0, 0))
        #pixmap.setPixelColor(1, 1, PyQt5.QtGui.QColor.fromRgb(255, 255, 0))
        # ScanLine(0) return first pixel data
        #ptr = pixmap.scanLine(0) # Scanline
        #ptr2 = pixmap.bits()
        # bits() == scanLine(0)
        #print(ptr, ptr2)

        # setPixelColor is less efficient, but easier to work with

        palette = QPalette()
        palette.setBrush(PyQt5.QtGui.QPalette.Background, PyQt5.QtGui.QBrush(pixmap))
        self.setPalette(palette)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MandelbrotWindow()
    mainWin.show()
    sys.exit( app.exec_() )