#python3 run.py
import sys
import os
from PyQt4 import QtGui,QtCore
import subprocess
import Train_gui

# Compile this file as chmod -x run.py
# Run this file as ./run.py
# Compile other ui file as --> pyuic4 TrainWidget.ui -o TrainWidget.py

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    trainWidget = Train_gui.Ui_mainWindow()
    trainWidget.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
