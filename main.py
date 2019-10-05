# Based on code from https://pythonprogramminglanguage.com/pyqt5-hello-world/

import sys
import PyQt5.QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QImage, QColor
from PyQt5.QtCore import QSize   

def mandleInit(x, y, maxIterations):
    # Need to scale input to -2.5 -> 1 for x
    # and for y -1 -> 1
    
    xScaled = -2.5 + (3.5*(x/640))
    yScaled = -1 + (2*(y/480)) # TODO: numbers need to be global

    c = complex(xScaled, yScaled)

    mandleRec(c, complex(0, 0), 0, maxIterations)

def mandleRec(c, z, it, maxIterations):
    if it < maxIterations:
        tempZ = z*z
        tempZ += c

        print(z)
        mandleRec(c, tempZ, it + 1, maxIterations)



class MandelbrotWindow(QMainWindow): # Python inheritance
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("MandelbrotQtViewer") 
        
        pixmap = QPixmap(640, 480).toImage()
        pixmap.fill(PyQt5.QtGui.QColor.fromRgb(255, 255, 255))
        
        for i in range(300):
            pixmap.setPixelColor(0, i, PyQt5.QtGui.QColor.fromRgb(255, 0, 0)) # First element is x, second is y
        #pixmap.setPixelColor(1, 1, PyQt5.QtGui.QColor.fromRgb(255, 255, 0))
        # ScanLine(0) return first pixel data
        #ptr = pixmap.scanLine(0) # Scanline
        #ptr2 = pixmap.bits()
        # bits() == scanLine(0)
        #print(ptr, ptr2)

        mandleInit(0, 0, 5)


        # setPixelColor is less efficient, but easier to work with

        palette = QPalette()
        palette.setBrush(PyQt5.QtGui.QPalette.Background, PyQt5.QtGui.QBrush(pixmap))
        self.setPalette(palette)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MandelbrotWindow()
    mainWin.show()
    sys.exit( app.exec_() )