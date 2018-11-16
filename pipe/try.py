import sys, time
import os
from PyQt4 import QtGui,QtCore
import subprocess
import trainform

# Compile this file as chmod -x run.py
# Run this file as ./run.py
# Compile other ui file as --> pyuic4 TrainWidget.ui -o TrainWidget.py

#_____________________________________________________________________________

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx||||||||||||||||||||||||||||||||||||
# # worker class
# class TrainWorkThread(QtCore.QThread):
# 	def __init__(self):
# 		QtCore.QThread.__init__(self)

# 	def run(self):
# 		print('TrainWorkThread run()')
# 		time.sleep(5)

# #
# 		train_cmd_str = './darknet detector train voc_gui.data gui.cfg'
# 		print("\n calling ",train_cmd_str,"\n")
# 		#subprocess.call(train_cmd_str,shell=True)
# #

# 		self.emit( QtCore.SIGNAL('update(QString)'), "from TrainWorkThread" )
# 		return
		
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|||||||||||||||||||||||||||||||||||||


class Ui_mainWindow(object):
#-------------------------------------------------------------------------------------------------
#   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
#   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V
#-------------------------------------------------------------------------------------------------
    count = 0 # no. of classes selected
    classSet = []	# list of selected class names
    filterSet = []

    def count_class(self,state):
        print("\n-------->count class function")
        if state == QtCore.Qt.Checked:
            self.count = self.count + 1
        else:
            self.count = self.count - 1
        self.lcdNumber.display(self.count)
        self.lcdNumber_filters.display( 5*( self.count + 5 ) )

    def cal_weight(self):
    	print('\n-------->cal_weight function')
    	# class update cmd
    	self.updateClasses()
    	wt_cal = 'python wt_cal.py '+str( self.count )
    	print("\n calling ",wt_cal,"\n")
    	subprocess.call(wt_cal,shell=True)
    	# print(" ----<<<<>>>------")
    	weights_result = open('gui_weights.txt','r').readlines()
    	self.lcdNumber_weight.display(float(weights_result[0]))

#>>>
    def stop_cmd(self):
    	pass
# now
    def updateFilters(self):# called after updateClasses function call
    	print('\n-------->updateFilters function')
    	string = ''
    	self.filterSet = []
    	self.filterSet.append(self.spinBoxConv1.value())
    	self.filterSet.append(self.spinBoxConv2.value())
    	self.filterSet.append(self.spinBoxConv3.value())
    	self.filterSet.append(self.spinBoxConv4.value())
    	self.filterSet.append(self.spinBoxConv5.value())
    	self.filterSet.append(self.spinBoxConv6.value())
    	self.filterSet.append(self.spinBoxConv7.value())
    	self.filterSet.append(self.spinBoxConv8.value())
    	self.filterSet.append( 5*(5+len(self.classSet)) )

    	for f in self.filterSet:
    		string+=str(f)+' '

    	filters_update_cmd = 'python updateFilters.py '+string
    	print("\n calling ",filters_update_cmd,"\n")
    	subprocess.call(filters_update_cmd,shell=True)
    	# print(" ----<<<<>>>------")
# .,.,.,.,.,.,.,.,.,

    def relaunch_cmd(self):
    	relaunch_cmd_str = './darknet detector train modified/voc_gui.data modified/gui.cfg gui.backup -gpus 0,1'
    	print("\n calling ",relaunch_cmd_str,"\n")
    	subprocess.call(relaunch_cmd_str,shell=True)
    	# print(" ----<<<<>>>------")
#>>>

    def updateClasses(self):
        print('\n-------->updateClasses function')
        self.class_sub()
        string = ''
        for c in self.classSet:
            string = string+str(c)+' '
        string = string[:-1]

        class_update_cmd = "python updateClasses.py "+str( len(self.classSet) )+' '+string
        print("\n calling ",class_update_cmd,"\n")
        subprocess.call(class_update_cmd,shell=True)
        # print(" ----<<<<>>>------")
        self.updateFilters()


    def train_cmd(self):
    	self.updateClasses()
    	train_cmd_str = './darknet detector train voc_gui.data gui.cfg'
    	print("\n calling ",train_cmd_str,"\n")
    	# subprocess.call(train_cmd_str,shell=True)

    def class_sub(self):
	##	-->> here classes are implemented by manually creating checkbox button
        self.classSet = []
        if self.aeroplane.isChecked(): 
            self.classSet.append( str(self.aeroplane.objectName()) )
        if self.bicycle.isChecked(): 
            self.classSet.append( str(self.bicycle.objectName()) )
        if self.bird.isChecked(): 
            self.classSet.append( str(self.bird.objectName()) )
        if self.boat.isChecked(): 
            self.classSet.append( str(self.boat.objectName()) )
        if self.bottle.isChecked(): 
            self.classSet.append( str(self.bottle.objectName()) )
        if self.bus.isChecked(): 
            self.classSet.append( str(self.bus.objectName()) )
        if self.cat.isChecked(): 
            self.classSet.append( str(self.cat.objectName()) )
        if self.car.isChecked(): 
            self.classSet.append( str(self.car.objectName()) )
        if self.chair.isChecked(): 
            self.classSet.append( str(self.chair.objectName()) )
        if self.cow.isChecked(): 
            self.classSet.append( str(self.cow.objectName()) )
        if self.dog.isChecked(): 
            self.classSet.append( str(self.dog.objectName()) )
        if self.diningtable.isChecked(): 
            self.classSet.append( str(self.diningtable.objectName()) )
        if self.horse.isChecked(): 
            self.classSet.append( str(self.horse.objectName()) )
        if self.motorbike.isChecked(): 
            self.classSet.append( str(self.motorbike.objectName()) )
        if self.person.isChecked(): 
            self.classSet.append( str(self.person.objectName()) )
        if self.pottedplant.isChecked(): 
            self.classSet.append( str(self.pottedplant.objectName()) )
        if self.sheep.isChecked(): 
            self.classSet.append( str(self.sheep.objectName()) )
        if self.sofa.isChecked(): 
            self.classSet.append( str(self.sofa.objectName()) )
        if self.train.isChecked(): 
            self.classSet.append( str(self.train.objectName()) )
        if self.tvmonitor.isChecked(): 
            self.classSet.append( str(self.tvmonitor.objectName()) )

#-------------------------------------------------------------------------------------------------
#   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A
#   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
#-------------------------------------------------------------------------------------------------

    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(500, 737)
        mainWindow.setMaximumSize(QtCore.QSize(500, 737))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem = QtGui.QSpacerItem(431, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 4, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.NumClassLabel = QtGui.QLabel(self.centralwidget)
        self.NumClassLabel.setObjectName(_fromUtf8("NumClassLabel"))
        self.gridLayout_2.addWidget(self.NumClassLabel, 0, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(50, 50))
        self.lcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.weightButton = QtGui.QPushButton(self.centralwidget)
        self.weightButton.setMinimumSize(QtCore.QSize(100, 25))
        self.weightButton.setMaximumSize(QtCore.QSize(100, 25))
        self.weightButton.setAutoRepeatDelay(-3)
        self.weightButton.setObjectName(_fromUtf8("weightButton"))
        self.gridLayout_2.addWidget(self.weightButton, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lcdNumber_weight = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_weight.setMinimumSize(QtCore.QSize(50, 50))
        self.lcdNumber_weight.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_weight.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_weight.setObjectName(_fromUtf8("lcdNumber_weight"))
        self.gridLayout_2.addWidget(self.lcdNumber_weight, 1, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(353, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.TrainWigLabel = QtGui.QLabel(self.centralwidget)
        self.TrainWigLabel.setObjectName(_fromUtf8("TrainWigLabel"))
        self.gridLayout_5.addWidget(self.TrainWigLabel, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.aeroplane = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aeroplane.setFont(font)
        self.aeroplane.setObjectName(_fromUtf8("aeroplane"))
        self.gridLayout.addWidget(self.aeroplane, 0, 0, 1, 1)
        self.bicycle = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bicycle.setFont(font)
        self.bicycle.setObjectName(_fromUtf8("bicycle"))
        self.gridLayout.addWidget(self.bicycle, 0, 1, 1, 1)
        self.bird = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bird.setFont(font)
        self.bird.setObjectName(_fromUtf8("bird"))
        self.gridLayout.addWidget(self.bird, 0, 2, 1, 1)
        self.boat = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boat.setFont(font)
        self.boat.setObjectName(_fromUtf8("boat"))
        self.gridLayout.addWidget(self.boat, 0, 3, 1, 1)
        self.chair = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chair.setFont(font)
        self.chair.setObjectName(_fromUtf8("chair"))
        self.gridLayout.addWidget(self.chair, 0, 4, 1, 1)
        self.sheep = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sheep.setFont(font)
        self.sheep.setObjectName(_fromUtf8("sheep"))
        self.gridLayout.addWidget(self.sheep, 0, 5, 1, 1)
        self.diningtable = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diningtable.setFont(font)
        self.diningtable.setObjectName(_fromUtf8("diningtable"))
        self.gridLayout.addWidget(self.diningtable, 0, 6, 1, 1)
        self.motorbike = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.motorbike.setFont(font)
        self.motorbike.setObjectName(_fromUtf8("motorbike"))
        self.gridLayout.addWidget(self.motorbike, 1, 0, 1, 1)
        self.cat = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cat.setFont(font)
        self.cat.setObjectName(_fromUtf8("cat"))
        self.gridLayout.addWidget(self.cat, 1, 1, 1, 1)
        self.bottle = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bottle.setFont(font)
        self.bottle.setObjectName(_fromUtf8("bottle"))
        self.gridLayout.addWidget(self.bottle, 1, 2, 1, 1)
        self.bus = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bus.setFont(font)
        self.bus.setObjectName(_fromUtf8("bus"))
        self.gridLayout.addWidget(self.bus, 1, 3, 1, 1)
        self.car = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.car.setFont(font)
        self.car.setObjectName(_fromUtf8("car"))
        self.gridLayout.addWidget(self.car, 1, 4, 1, 1)
        self.cow = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cow.setFont(font)
        self.cow.setObjectName(_fromUtf8("cow"))
        self.gridLayout.addWidget(self.cow, 1, 5, 1, 1)
        self.pottedplant = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pottedplant.setFont(font)
        self.pottedplant.setObjectName(_fromUtf8("pottedplant"))
        self.gridLayout.addWidget(self.pottedplant, 1, 6, 1, 1)
        self.tvmonitor = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tvmonitor.setFont(font)
        self.tvmonitor.setObjectName(_fromUtf8("tvmonitor"))
        self.gridLayout.addWidget(self.tvmonitor, 2, 0, 1, 1)
        self.sofa = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sofa.setFont(font)
        self.sofa.setObjectName(_fromUtf8("sofa"))
        self.gridLayout.addWidget(self.sofa, 2, 1, 1, 1)
        self.train = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.train.setFont(font)
        self.train.setObjectName(_fromUtf8("train"))
        self.gridLayout.addWidget(self.train, 2, 2, 1, 1)
        self.person = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person.setFont(font)
        self.person.setObjectName(_fromUtf8("person"))
        self.gridLayout.addWidget(self.person, 2, 3, 1, 1)
        self.dog = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dog.setFont(font)
        self.dog.setObjectName(_fromUtf8("dog"))
        self.gridLayout.addWidget(self.dog, 2, 4, 1, 1)
        self.horse = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horse.setFont(font)
        self.horse.setObjectName(_fromUtf8("horse"))
        self.gridLayout.addWidget(self.horse, 2, 5, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 722, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 0, 2, 5, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.trainButton = QtGui.QPushButton(self.centralwidget)
        self.trainButton.setMinimumSize(QtCore.QSize(100, 25))
        self.trainButton.setMaximumSize(QtCore.QSize(127, 30))
        self.trainButton.setObjectName(_fromUtf8("trainButton"))
        self.gridLayout_6.addWidget(self.trainButton, 0, 0, 1, 1)
        self.cancelButton_stop = QtGui.QPushButton(self.centralwidget)
        self.cancelButton_stop.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelButton_stop.setMaximumSize(QtCore.QSize(127, 30))
        self.cancelButton_stop.setObjectName(_fromUtf8("cancelButton_stop"))
        self.gridLayout_6.addWidget(self.cancelButton_stop, 0, 1, 1, 1)
        self.trainButton_relaunch = QtGui.QPushButton(self.centralwidget)
        self.trainButton_relaunch.setMinimumSize(QtCore.QSize(100, 25))
        self.trainButton_relaunch.setMaximumSize(QtCore.QSize(127, 30))
        self.trainButton_relaunch.setObjectName(_fromUtf8("trainButton_relaunch"))
        self.gridLayout_6.addWidget(self.trainButton_relaunch, 0, 2, 1, 1)
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelButton.setMaximumSize(QtCore.QSize(127, 30))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout_6.addWidget(self.cancelButton, 0, 3, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 3, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 722, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 0, 0, 5, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.TrainWigLabel_31 = QtGui.QLabel(self.centralwidget)
        self.TrainWigLabel_31.setObjectName(_fromUtf8("TrainWigLabel_31"))
        self.gridLayout_4.addWidget(self.TrainWigLabel_31, 2, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName(_fromUtf8("tabWidgetPage1"))
        self.TrainWigLabel_2 = QtGui.QLabel(self.tabWidgetPage1)
        self.TrainWigLabel_2.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_2.setObjectName(_fromUtf8("TrainWigLabel_2"))
        self.TrainWigLabel_11 = QtGui.QLabel(self.tabWidgetPage1)
        self.TrainWigLabel_11.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_11.setObjectName(_fromUtf8("TrainWigLabel_11"))
        self.spinBoxConv1 = QtGui.QSpinBox(self.tabWidgetPage1)
        self.spinBoxConv1.setGeometry(QtCore.QRect(100, 60, 51, 22))
        self.spinBoxConv1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv1.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv1.setMinimum(1)
        self.spinBoxConv1.setMaximum(4096)
        self.spinBoxConv1.setSingleStep(16)
        self.spinBoxConv1.setProperty("value", 16)
        self.spinBoxConv1.setObjectName(_fromUtf8("spinBoxConv1"))
        self.TrainWigLabel_11.raise_()
        self.TrainWigLabel_2.raise_()
        self.spinBoxConv1.raise_()
        self.tabWidget.addTab(self.tabWidgetPage1, _fromUtf8(""))
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName(_fromUtf8("tabWidgetPage2"))
        self.TrainWigLabel_32 = QtGui.QLabel(self.tabWidgetPage2)
        self.TrainWigLabel_32.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_32.setObjectName(_fromUtf8("TrainWigLabel_32"))
        self.TrainWigLabel_33 = QtGui.QLabel(self.tabWidgetPage2)
        self.TrainWigLabel_33.setGeometry(QtCore.QRect(10, 40, 151, 41))
        self.TrainWigLabel_33.setObjectName(_fromUtf8("TrainWigLabel_33"))
        self.tabWidget.addTab(self.tabWidgetPage2, _fromUtf8(""))
        self.tabWidgetPage3 = QtGui.QWidget()
        self.tabWidgetPage3.setObjectName(_fromUtf8("tabWidgetPage3"))
        self.TrainWigLabel_4 = QtGui.QLabel(self.tabWidgetPage3)
        self.TrainWigLabel_4.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_4.setObjectName(_fromUtf8("TrainWigLabel_4"))
        self.TrainWigLabel_21 = QtGui.QLabel(self.tabWidgetPage3)
        self.TrainWigLabel_21.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_21.setObjectName(_fromUtf8("TrainWigLabel_21"))
        self.spinBoxConv2 = QtGui.QSpinBox(self.tabWidgetPage3)
        self.spinBoxConv2.setGeometry(QtCore.QRect(110, 60, 51, 22))
        self.spinBoxConv2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv2.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv2.setMinimum(1)
        self.spinBoxConv2.setMaximum(4096)
        self.spinBoxConv2.setSingleStep(16)
        self.spinBoxConv2.setProperty("value", 32)
        self.spinBoxConv2.setObjectName(_fromUtf8("spinBoxConv2"))
        self.tabWidget.addTab(self.tabWidgetPage3, _fromUtf8(""))
        self.tabWidgetPage4 = QtGui.QWidget()
        self.tabWidgetPage4.setObjectName(_fromUtf8("tabWidgetPage4"))
        self.TrainWigLabel_34 = QtGui.QLabel(self.tabWidgetPage4)
        self.TrainWigLabel_34.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_34.setObjectName(_fromUtf8("TrainWigLabel_34"))
        self.TrainWigLabel_35 = QtGui.QLabel(self.tabWidgetPage4)
        self.TrainWigLabel_35.setGeometry(QtCore.QRect(10, 40, 151, 41))
        self.TrainWigLabel_35.setObjectName(_fromUtf8("TrainWigLabel_35"))
        self.tabWidget.addTab(self.tabWidgetPage4, _fromUtf8(""))
        self.tabWidgetPage5 = QtGui.QWidget()
        self.tabWidgetPage5.setObjectName(_fromUtf8("tabWidgetPage5"))
        self.TrainWigLabel_5 = QtGui.QLabel(self.tabWidgetPage5)
        self.TrainWigLabel_5.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_5.setObjectName(_fromUtf8("TrainWigLabel_5"))
        self.TrainWigLabel_22 = QtGui.QLabel(self.tabWidgetPage5)
        self.TrainWigLabel_22.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_22.setObjectName(_fromUtf8("TrainWigLabel_22"))
        self.spinBoxConv3 = QtGui.QSpinBox(self.tabWidgetPage5)
        self.spinBoxConv3.setGeometry(QtCore.QRect(110, 60, 51, 22))
        self.spinBoxConv3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv3.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv3.setMinimum(1)
        self.spinBoxConv3.setMaximum(4096)
        self.spinBoxConv3.setSingleStep(16)
        self.spinBoxConv3.setProperty("value", 64)
        self.spinBoxConv3.setObjectName(_fromUtf8("spinBoxConv3"))
        self.tabWidget.addTab(self.tabWidgetPage5, _fromUtf8(""))
        self.tabWidgetPage6 = QtGui.QWidget()
        self.tabWidgetPage6.setObjectName(_fromUtf8("tabWidgetPage6"))
        self.TrainWigLabel_36 = QtGui.QLabel(self.tabWidgetPage6)
        self.TrainWigLabel_36.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_36.setObjectName(_fromUtf8("TrainWigLabel_36"))
        self.TrainWigLabel_37 = QtGui.QLabel(self.tabWidgetPage6)
        self.TrainWigLabel_37.setGeometry(QtCore.QRect(10, 40, 151, 41))
        self.TrainWigLabel_37.setObjectName(_fromUtf8("TrainWigLabel_37"))
        self.tabWidget.addTab(self.tabWidgetPage6, _fromUtf8(""))
        self.tabWidgetPage7 = QtGui.QWidget()
        self.tabWidgetPage7.setObjectName(_fromUtf8("tabWidgetPage7"))
        self.TrainWigLabel_6 = QtGui.QLabel(self.tabWidgetPage7)
        self.TrainWigLabel_6.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_6.setObjectName(_fromUtf8("TrainWigLabel_6"))
        self.TrainWigLabel_23 = QtGui.QLabel(self.tabWidgetPage7)
        self.TrainWigLabel_23.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_23.setObjectName(_fromUtf8("TrainWigLabel_23"))
        self.spinBoxConv4 = QtGui.QSpinBox(self.tabWidgetPage7)
        self.spinBoxConv4.setGeometry(QtCore.QRect(110, 60, 51, 22))
        self.spinBoxConv4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv4.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv4.setMinimum(1)
        self.spinBoxConv4.setMaximum(4096)
        self.spinBoxConv4.setSingleStep(16)
        self.spinBoxConv4.setProperty("value", 128)
        self.spinBoxConv4.setObjectName(_fromUtf8("spinBoxConv4"))
        self.tabWidget.addTab(self.tabWidgetPage7, _fromUtf8(""))
        self.tabWidgetPage8 = QtGui.QWidget()
        self.tabWidgetPage8.setObjectName(_fromUtf8("tabWidgetPage8"))
        self.TrainWigLabel_38 = QtGui.QLabel(self.tabWidgetPage8)
        self.TrainWigLabel_38.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_38.setObjectName(_fromUtf8("TrainWigLabel_38"))
        self.TrainWigLabel_39 = QtGui.QLabel(self.tabWidgetPage8)
        self.TrainWigLabel_39.setGeometry(QtCore.QRect(10, 40, 151, 41))
        self.TrainWigLabel_39.setObjectName(_fromUtf8("TrainWigLabel_39"))
        self.tabWidget.addTab(self.tabWidgetPage8, _fromUtf8(""))
        self.tabWidgetPage9 = QtGui.QWidget()
        self.tabWidgetPage9.setObjectName(_fromUtf8("tabWidgetPage9"))
        self.TrainWigLabel_7 = QtGui.QLabel(self.tabWidgetPage9)
        self.TrainWigLabel_7.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_7.setObjectName(_fromUtf8("TrainWigLabel_7"))
        self.TrainWigLabel_24 = QtGui.QLabel(self.tabWidgetPage9)
        self.TrainWigLabel_24.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_24.setObjectName(_fromUtf8("TrainWigLabel_24"))
        self.spinBoxConv5 = QtGui.QSpinBox(self.tabWidgetPage9)
        self.spinBoxConv5.setGeometry(QtCore.QRect(110, 60, 51, 22))
        self.spinBoxConv5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv5.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv5.setMinimum(1)
        self.spinBoxConv5.setMaximum(4096)
        self.spinBoxConv5.setSingleStep(16)
        self.spinBoxConv5.setProperty("value", 256)
        self.spinBoxConv5.setObjectName(_fromUtf8("spinBoxConv5"))
        self.tabWidget.addTab(self.tabWidgetPage9, _fromUtf8(""))
        self.tabWidgetPage10 = QtGui.QWidget()
        self.tabWidgetPage10.setObjectName(_fromUtf8("tabWidgetPage10"))
        self.TrainWigLabel_40 = QtGui.QLabel(self.tabWidgetPage10)
        self.TrainWigLabel_40.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_40.setObjectName(_fromUtf8("TrainWigLabel_40"))
        self.TrainWigLabel_41 = QtGui.QLabel(self.tabWidgetPage10)
        self.TrainWigLabel_41.setGeometry(QtCore.QRect(10, 50, 151, 41))
        self.TrainWigLabel_41.setObjectName(_fromUtf8("TrainWigLabel_41"))
        self.tabWidget.addTab(self.tabWidgetPage10, _fromUtf8(""))
        self.tabWidgetPage11 = QtGui.QWidget()
        self.tabWidgetPage11.setObjectName(_fromUtf8("tabWidgetPage11"))
        self.TrainWigLabel_8 = QtGui.QLabel(self.tabWidgetPage11)
        self.TrainWigLabel_8.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_8.setObjectName(_fromUtf8("TrainWigLabel_8"))
        self.TrainWigLabel_25 = QtGui.QLabel(self.tabWidgetPage11)
        self.TrainWigLabel_25.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_25.setObjectName(_fromUtf8("TrainWigLabel_25"))
        self.spinBoxConv6 = QtGui.QSpinBox(self.tabWidgetPage11)
        self.spinBoxConv6.setGeometry(QtCore.QRect(110, 60, 51, 22))
        self.spinBoxConv6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv6.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv6.setMinimum(1)
        self.spinBoxConv6.setMaximum(4096)
        self.spinBoxConv6.setSingleStep(16)
        self.spinBoxConv6.setProperty("value", 512)
        self.spinBoxConv6.setObjectName(_fromUtf8("spinBoxConv6"))
        self.tabWidget.addTab(self.tabWidgetPage11, _fromUtf8(""))
        self.tabWidgetPage12 = QtGui.QWidget()
        self.tabWidgetPage12.setObjectName(_fromUtf8("tabWidgetPage12"))
        self.TrainWigLabel_42 = QtGui.QLabel(self.tabWidgetPage12)
        self.TrainWigLabel_42.setGeometry(QtCore.QRect(10, 20, 141, 21))
        self.TrainWigLabel_42.setObjectName(_fromUtf8("TrainWigLabel_42"))
        self.TrainWigLabel_43 = QtGui.QLabel(self.tabWidgetPage12)
        self.TrainWigLabel_43.setGeometry(QtCore.QRect(10, 50, 151, 41))
        self.TrainWigLabel_43.setObjectName(_fromUtf8("TrainWigLabel_43"))
        self.tabWidget.addTab(self.tabWidgetPage12, _fromUtf8(""))
        self.tabWidgetPage13 = QtGui.QWidget()
        self.tabWidgetPage13.setObjectName(_fromUtf8("tabWidgetPage13"))
        self.TrainWigLabel_9 = QtGui.QLabel(self.tabWidgetPage13)
        self.TrainWigLabel_9.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_9.setObjectName(_fromUtf8("TrainWigLabel_9"))
        self.TrainWigLabel_26 = QtGui.QLabel(self.tabWidgetPage13)
        self.TrainWigLabel_26.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_26.setObjectName(_fromUtf8("TrainWigLabel_26"))
        self.spinBoxConv7 = QtGui.QSpinBox(self.tabWidgetPage13)
        self.spinBoxConv7.setGeometry(QtCore.QRect(100, 60, 51, 22))
        self.spinBoxConv7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv7.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv7.setMinimum(1)
        self.spinBoxConv7.setMaximum(4096)
        self.spinBoxConv7.setSingleStep(16)
        self.spinBoxConv7.setProperty("value", 1024)
        self.spinBoxConv7.setObjectName(_fromUtf8("spinBoxConv7"))
        self.tabWidget.addTab(self.tabWidgetPage13, _fromUtf8(""))
        self.tabWidgetPage14 = QtGui.QWidget()
        self.tabWidgetPage14.setObjectName(_fromUtf8("tabWidgetPage14"))
        self.TrainWigLabel_10 = QtGui.QLabel(self.tabWidgetPage14)
        self.TrainWigLabel_10.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_10.setObjectName(_fromUtf8("TrainWigLabel_10"))
        self.TrainWigLabel_27 = QtGui.QLabel(self.tabWidgetPage14)
        self.TrainWigLabel_27.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_27.setObjectName(_fromUtf8("TrainWigLabel_27"))
        self.spinBoxConv8 = QtGui.QSpinBox(self.tabWidgetPage14)
        self.spinBoxConv8.setGeometry(QtCore.QRect(100, 60, 51, 22))
        self.spinBoxConv8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxConv8.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBoxConv8.setMinimum(1)
        self.spinBoxConv8.setMaximum(4096)
        self.spinBoxConv8.setSingleStep(16)
        self.spinBoxConv8.setProperty("value", 1024)
        self.spinBoxConv8.setObjectName(_fromUtf8("spinBoxConv8"))
        self.tabWidget.addTab(self.tabWidgetPage14, _fromUtf8(""))
        self.tabWidgetPage15 = QtGui.QWidget()
        self.tabWidgetPage15.setObjectName(_fromUtf8("tabWidgetPage15"))
        self.TrainWigLabel_28 = QtGui.QLabel(self.tabWidgetPage15)
        self.TrainWigLabel_28.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.TrainWigLabel_28.setObjectName(_fromUtf8("TrainWigLabel_28"))
        self.TrainWigLabel_29 = QtGui.QLabel(self.tabWidgetPage15)
        self.TrainWigLabel_29.setGeometry(QtCore.QRect(10, 40, 151, 131))
        self.TrainWigLabel_29.setObjectName(_fromUtf8("TrainWigLabel_29"))
        self.lcdNumber_filters = QtGui.QLCDNumber(self.tabWidgetPage15)
        self.lcdNumber_filters.setGeometry(QtCore.QRect(130, 40, 71, 60))
        self.lcdNumber_filters.setMinimumSize(QtCore.QSize(50, 50))
        self.lcdNumber_filters.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_filters.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_filters.setDigitCount(3)
        self.lcdNumber_filters.setProperty("value", 25.0)
        self.lcdNumber_filters.setObjectName(_fromUtf8("lcdNumber_filters"))
        self.TrainWigLabel_29.raise_()
        self.TrainWigLabel_28.raise_()
        self.lcdNumber_filters.raise_()
        self.tabWidget.addTab(self.tabWidgetPage15, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget, 2, 1, 1, 1)
        self.TrainWigLabel_30 = QtGui.QLabel(self.centralwidget)
        self.TrainWigLabel_30.setObjectName(_fromUtf8("TrainWigLabel_30"))
        self.gridLayout_4.addWidget(self.TrainWigLabel_30, 1, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.actionTest = QtGui.QAction(mainWindow)
        self.actionTest.setObjectName(_fromUtf8("actionTest"))
#-------------------------------------------------------------------------------------------------
#   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
#   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V   V
#-------------------------------------------------------------------------------------------------

        self.aeroplane.stateChanged.connect(self.count_class)
        self.bicycle.stateChanged.connect(self.count_class)
        self.bird.stateChanged.connect(self.count_class)
        self.boat.stateChanged.connect(self.count_class)
        self.bottle.stateChanged.connect(self.count_class)
        self.bus.stateChanged.connect(self.count_class)
        self.car.stateChanged.connect(self.count_class)
        self.cat.stateChanged.connect(self.count_class)
        self.chair.stateChanged.connect(self.count_class)
        self.cow.stateChanged.connect(self.count_class)
        self.diningtable.stateChanged.connect(self.count_class)
        self.dog.stateChanged.connect(self.count_class)
        self.horse.stateChanged.connect(self.count_class)
        self.motorbike.stateChanged.connect(self.count_class)
        self.person.stateChanged.connect(self.count_class)
        self.pottedplant.stateChanged.connect(self.count_class)
        self.sheep.stateChanged.connect(self.count_class)
        self.sofa.stateChanged.connect(self.count_class)
        self.train.stateChanged.connect(self.count_class)
        self.tvmonitor.stateChanged.connect(self.count_class)
        #QtCore.QObject.connect(self.trainButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.train_cmd)
        self.weightButton.clicked.connect(self.cal_weight)
        self.trainButton.clicked.connect(self.train_cmd)
        self.cancelButton_stop.clicked.connect(self.stop_cmd)
        self.trainButton_relaunch.clicked.connect(self.relaunch_cmd)
        self.cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

#-------------------------------------------------------------------------------------------------
#   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A   A
#   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
#-------------------------------------------------------------------------------------------------

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(14)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "YOLO GUI", None))
        self.NumClassLabel.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#005500;\">Number of classes selected</span></p></body></html>", None))
        self.weightButton.setText(_translate("mainWindow", "Calculate Weight", None))
        self.TrainWigLabel.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#161616;\">Choose classes to Train Model</span></p></body></html>", None))
        self.aeroplane.setText(_translate("mainWindow", "aeroplane", None))
        self.bicycle.setText(_translate("mainWindow", "bicycle", None))
        self.bird.setText(_translate("mainWindow", "bird", None))
        self.boat.setText(_translate("mainWindow", "boat", None))
        self.chair.setText(_translate("mainWindow", "chair", None))
        self.sheep.setText(_translate("mainWindow", "sheep", None))
        self.diningtable.setText(_translate("mainWindow", "dining table", None))
        self.motorbike.setText(_translate("mainWindow", "motorbike", None))
        self.cat.setText(_translate("mainWindow", "cat", None))
        self.bottle.setText(_translate("mainWindow", "bottle", None))
        self.bus.setText(_translate("mainWindow", "bus", None))
        self.car.setText(_translate("mainWindow", "car", None))
        self.cow.setText(_translate("mainWindow", "cow", None))
        self.pottedplant.setText(_translate("mainWindow", "potted plant", None))
        self.tvmonitor.setText(_translate("mainWindow", "tv monitor", None))
        self.sofa.setText(_translate("mainWindow", "sofa", None))
        self.train.setText(_translate("mainWindow", "train", None))
        self.person.setText(_translate("mainWindow", "person", None))
        self.dog.setText(_translate("mainWindow", "dog", None))
        self.horse.setText(_translate("mainWindow", "horse", None))
        self.trainButton.setText(_translate("mainWindow", "Train", None))
        self.cancelButton_stop.setText(_translate("mainWindow", "stop", None))
        self.trainButton_relaunch.setText(_translate("mainWindow", "Relaunch", None))
        self.cancelButton.setText(_translate("mainWindow", "Exit", None))
        self.TrainWigLabel_31.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">LAYERS</span></p><p><span style=\" font-weight:600;\">0 conv 16</span></p><p><span style=\" font-weight:600;\">1 max</span></p><p><span style=\" font-weight:600;\">2 conv 32</span></p><p><span style=\" font-weight:600;\">3 max</span></p><p><span style=\" font-weight:600;\">4 conv 64</span></p><p><span style=\" font-weight:600;\">5 max</span></p><p><span style=\" font-weight:600;\">6 conv 128</span></p><p><span style=\" font-weight:600;\">7 max</span></p><p><span style=\" font-weight:600;\">8 conv 256</span></p><p><span style=\" font-weight:600;\">9 max</span></p><p><span style=\" font-weight:600;\">10 conv 512</span></p><p><span style=\" font-weight:600;\">11 max</span></p><p><span style=\" font-weight:600;\">12 conv 1024</span></p><p><span style=\" font-weight:600;\">13 conv 1024</span></p><p><span style=\" font-weight:600;\">14 conv 125</span></p><p><span style=\" font-weight:600;\">15 detection</span></p></body></html>", None))
        self.TrainWigLabel_2.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">0 Conv Layer - 1</span></p></body></html>", None))
        self.TrainWigLabel_11.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_32.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">1 Maxpool Layer</span></p></body></html>", None))
        self.TrainWigLabel_33.setText(_translate("mainWindow", "<html><head/><body><p>size=2</p><p>stride=2</p></body></html>", None))
        self.TrainWigLabel_4.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">2 Conv Layer - 2</span></p></body></html>", None))
        self.TrainWigLabel_21.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_34.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">3 Maxpool Layer</span></p></body></html>", None))
        self.TrainWigLabel_35.setText(_translate("mainWindow", "<html><head/><body><p>size=2</p><p>stride=2</p></body></html>", None))
        self.TrainWigLabel_5.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">4 Conv Layer - 3</span></p></body></html>", None))
        self.TrainWigLabel_22.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_36.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">5 Maxpool Layer</span></p></body></html>", None))
        self.TrainWigLabel_37.setText(_translate("mainWindow", "<html><head/><body><p>size=2</p><p>stride=2</p></body></html>", None))
        self.TrainWigLabel_6.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">6 Conv Layer - 4</span></p></body></html>", None))
        self.TrainWigLabel_23.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_38.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">7 Maxpool Layer</span></p></body></html>", None))
        self.TrainWigLabel_39.setText(_translate("mainWindow", "<html><head/><body><p>size=2</p><p>stride=2</p></body></html>", None))
        self.TrainWigLabel_7.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">8 Conv Layer - 5</span></p></body></html>", None))
        self.TrainWigLabel_24.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_40.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">9 Maxpool Layer</span></p></body></html>", None))
        self.TrainWigLabel_41.setText(_translate("mainWindow", "<html><head/><body><p>size=2</p><p>stride=2</p></body></html>", None))
        self.TrainWigLabel_8.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">10 Conv Layer - 6</span></p></body></html>", None))
        self.TrainWigLabel_25.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_42.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">11 Maxpool Layer</span></p></body></html>", None))
        self.TrainWigLabel_43.setText(_translate("mainWindow", "<html><head/><body><p>size=2</p><p>stride=1</p></body></html>", None))
        self.TrainWigLabel_9.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">12 Conv Layer - 7</span></p></body></html>", None))
        self.TrainWigLabel_26.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_10.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">13 Conv Layer - 8</span></p></body></html>", None))
        self.TrainWigLabel_27.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p>filters</p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_28.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">14 Conv Layer - 9</span></p></body></html>", None))
        self.TrainWigLabel_29.setText(_translate("mainWindow", "<html><head/><body><p>batch_normalize=1</p><p><span style=\" font-weight:600;\">filters = (classes + 5)x5 = </span></p><p>size=3</p><p>stride=1</p><p>pad=1</p><p>activation=leaky</p></body></html>", None))
        self.TrainWigLabel_30.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#161616;\">YOLOv2-tiny-voc Layer Structure</span></p></body></html>", None))
        self.actionTest.setText(_translate("mainWindow", "Test", None))


class Athread(QtCore.QThread):
	"""docstring for Athread"""
	def __init__(self):
		QtCore.QThread.__init__(self)

	def run(self):
		print('Athread run()')
		time.sleep(5)

#
		train_cmd_str = './darknet detector train voc_gui.data gui.cfg'
		print("\n calling here ",train_cmd_str,"\n")
		#subprocess.call(train_cmd_str,shell=True)
#

		self.emit( QtCore.SIGNAL('clicked()'), "from TrainWorkThread" )
		return


app = QtGui.QApplication(sys.argv)

form = QtGui.QWidget()
mainWindow = QtGui.QMainWindow()

trainWidget = Ui_mainWindow()
form_ob = trainform.Ui_Form()

trainWidget.setupUi(mainWindow)
form_ob.setupUi(form)
# form.show()
mainWindow.show()
print('yoiyi')
time.sleep(5)
form.hide()
# thread = Athread()
# thread.finished.connect(app.exit)
# thread.start()
sys.exit(app.exec_())




#_____________________________________________________________________________
#if __name__ == "__main__":
    # app = QtGui.QApplication(sys.argv)
    # mainWindow = QtGui.QMainWindow()
    # trainWidget = Train_gui.Ui_mainWindow()
    # trainWidget.setupUi(mainWindow)
    # # mainWindow.show()
    # # sys.exit(app.exec_())
    # trainfx()

    # def train_cmd():
    #     self.WorkThread = TrainWorkThread()
    #     self.connect( self.WorkThread, QtCore.SIGNAL("update(QString)"),self.TrainWorkThread )
    #     self.WorkThread.start()



