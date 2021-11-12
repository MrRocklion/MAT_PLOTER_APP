# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import mplcyberpunk
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("cyberpunk")
x = np.linspace(0,5,11)
y = x**2
class App():
    def __init__(self):
        super(App, self).__init__()
        self.ui = QUiLoader().load(QFile("form.ui"))
        self.ui.pushButton.clicked.connect(self.graficar)
        self.grafica = Canvas_grafica()

    def graficar(self):
        self.ui.verticalLayout_4.addWidget(self.grafica)

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.figure()
        super().__init__(self.fig)
        self.ax = self.fig.add_axes([0.1, 0.1, 0.9, 0.9])
        self.ax.plot(x,y,label = 'cuadratic function', color= '#F1C40F',lw =2 , ls = '--')
        mplcyberpunk.add_glow_effects()
        self.fig.suptitle('Grafica de Barras',size=9)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = App()
    widget.ui.show()
    sys.exit(app.exec_())

