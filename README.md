## MandelbrotQtViewer
Simple Python script to visualize the infamous [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) without any interaction.

# Usage
Clone the project, run `pip install pyqt5`, then run the script with three arguments:
1. The number of iterations needed to check if the complex number becomes unbounded. 20 should do the trick, but 100 is also a possibility
2. The width of the window
3. The height of the window

Example: `python main.py 20 1000 1000`

The higher these numbers, the slower you will see results onscreen.

# Output
![alt text](https://i.gyazo.com/09fa1e9245bce22765446f9694d7ccb6.png "Mandelbrot visualized")
