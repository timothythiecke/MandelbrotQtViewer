# Qt window code based on https://pythonprogramminglanguage.com/pyqt5-hello-world/

import sys
import PyQt5.QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QImage, QColor
from PyQt5.QtCore import QSize   



def mandleInit(x, y, width, height, maxIterations):
    # Need to scale input to -2.5 -> 1 for x
    # and for y -1 -> 1
    
    xScaled = -2.5 + (4*(x/width))
    yScaled = -(-2 + (4*(y/height))) # TODO: numbers need to be global or shared
    return mandleRec(complex(xScaled, yScaled), complex(0, 0), 0, maxIterations)



def mandleRec(c, z, it, maxIterations):
    if it < maxIterations:
        tempZ = z*z
        tempZ += c

        # Do square magnitude calculation to speed up
        real = tempZ.real * tempZ.real 
        im = tempZ.imag * tempZ.imag

        if real + im > 4: # If the complex number is no longer bounded, we disregard it
            return it
        
        return mandleRec(c, tempZ, it + 1, maxIterations)

    return it



class MandelbrotWindow(QMainWindow): # Python inheritance
    def __init__(self):
        QMainWindow.__init__(self)

        width = int(sys.argv[2])
        height = int(sys.argv[3])
        self.setMinimumSize(QSize(width, height))    
        self.setWindowTitle("MandelbrotQtViewer") 
        
        pixmap = QPixmap(width, height).toImage()
        pixmap.fill(PyQt5.QtGui.QColor.fromRgb(255, 255, 255))
        
        maxSteps = int(sys.argv[1])
        print (maxSteps)
        for row in range(height):
            for col in range(width):
                steps = mandleInit(col, row, width, height, maxSteps)
                colorValue = 255*(1-(steps/maxSteps))
                inverted = 255 - colorValue

                red = 0
                green = 0
                blue = 0

                if steps != maxSteps:
                    red = inverted
                    green = inverted
                    blue = colorValue

                pixmap.setPixelColor(col, row, PyQt5.QtGui.QColor.fromRgb(red, green, blue))
    
        palette = QPalette()
        palette.setBrush(PyQt5.QtGui.QPalette.Background, PyQt5.QtGui.QBrush(pixmap))
        self.setPalette(palette)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MandelbrotWindow()
    mainWin.show()
    sys.exit( app.exec_() )


# ScanLine(0) return first pixel data
#ptr = pixmap.scanLine(0) # Scanline
#ptr2 = pixmap.bits()
# bits() == scanLine(0)
#print(ptr, ptr2)
# setPixelColor is less efficient, but easier to work with
