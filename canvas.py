import matplotlib
from matplotlib.widgets import Cursor

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as patches
from PyQt5.QtWidgets import QMessageBox


class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.Figure()
        FigureCanvas.__init__(self, self.fig)
        self.parent = parent
        self.subfig = self.fig.add_subplot(111)
        self.cursor = Cursor(self.subfig, useblit=False, color='gray', linewidth=1)
        self.cursor.visible = False
        self.img = None

    def updateCanvas(self, path):
        self.subfig.cla()
        self.img = Image.open(path)
        self.subfig.imshow(self.img)
        self.cursor = Cursor(self.subfig, useblit=False, color='gray', linewidth=1)
        self.cursor.visible = False
        self.draw()
