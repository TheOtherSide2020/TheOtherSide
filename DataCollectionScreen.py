import json
import os
# class for pollingScreen UI
import sys
import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = os.path.dirname(sys.argv[0])
    except Exception:
        base_path = os.path.dirname(sys.argv[0])
    return os.path.join(base_path, relative_path)


def plot(self, fileName):
    if DataCollectionScreen.count > 0:
        with open(os.path.join(resource_path('ResultData/' + DataCollectionScreen.template), fileName),
                  'r') as json_file:
            data = json.load(json_file)
            voteCountA = data['voteCounts'][0]
            voteCountB = data['voteCounts'][1]
            voteCountC = data['voteCounts'][2]
            voteCountD = data['voteCounts'][3]

        self.axes.bar(voteCountA['option'], voteCountA['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
        self.axes.bar(voteCountB['option'], voteCountB['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
        self.axes.bar(voteCountC['option'], voteCountC['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
        self.axes.bar(voteCountD['option'], voteCountD['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
        self.draw()
    else:
        for filename in os.listdir(resource_path('ResultData/' + DataCollectionScreen.template)):
            with open(os.path.join(resource_path('ResultData/' + DataCollectionScreen.template), filename),
                      'r') as json_file:
                data = json.load(json_file)
                voteCountA = data['voteCounts'][0]
                voteCountB = data['voteCounts'][1]
                voteCountC = data['voteCounts'][2]
                voteCountD = data['voteCounts'][3]

            self.axes.bar(voteCountA['option'], voteCountA['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
            self.axes.bar(voteCountB['option'], voteCountB['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
            self.axes.bar(voteCountC['option'], voteCountC['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
            self.axes.bar(voteCountD['option'], voteCountD['voteCount'], color=(0.2, 0.4, 0.6, 0.6))
            self.draw()


def plotUpdate(self, fileName):
    self.axes.clear()
    plot(self, fileName)


class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        plt.style.use('fivethirtyeight')
        self.fig, self.axes = plt.subplots(figsize=(8, 7), dpi=90)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        plot(self, "")


class DataCollectionScreen(QtWidgets.QMainWindow):
    count = 0
    currentEntry = ""

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.canvas = Canvas(self)
        self.canvas.move(280, 100)
        self.canvas.resize(900 , 600)
        self.setupUi(self)

    def is_file_empty(self, file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    # shows the first record
    def readFromJsonFile(self):
        if DataCollectionScreen.count == 0:
            self.listWidget.clear()
            plotUpdate(self.canvas, "")

        for filename in os.listdir(resource_path('ResultData/' + DataCollectionScreen.template)):
            with open(os.path.join(resource_path('ResultData/' + DataCollectionScreen.template), filename),
                      'r') as json_file:
                data = json.load(json_file)
                self.listWidget.addItem(data['name'])
                self.counter.setText(str(data['totalVote']))
                self.Time.setText(data['lastUpdated'])

    # Double clicking functionality for the data collection screen.
    def updateGraphOnClick(self):
        plotUpdate(self.canvas, self.listWidget.currentItem().text() + ".json")
        for filename in os.listdir(resource_path('ResultData/' + DataCollectionScreen.template)):
            with open(os.path.join(resource_path('ResultData/' + DataCollectionScreen.template), filename),
                      'r') as json_file:
                data = json.load(json_file)
                DataCollectionScreen.currentEntry = self.listWidget.currentItem().text()
                DataCollectionScreen.count += 1
                if data['name'] == self.listWidget.currentItem().text():
                    self.counter.setText(str(data['totalVote']))
                    self.Time.setText(data['lastUpdated'])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1218, 851)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 120, 301, 751))
        self.listWidget.setObjectName("listWidget_2")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignVCenter)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 301, 761))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 10, 51, 41))
        self.commandLinkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('Images/directional-chevron-back-512.ico')), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(900, 780, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(880, 740, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(970, 775, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Time.setFont(font)
        self.Time.setText("")
        self.Time.setObjectName("Time")
        self.counter = QtWidgets.QLabel(self.centralwidget)
        self.counter.setGeometry(QtCore.QRect(1020, 740, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.counter.setFont(font)
        self.counter.setText("")
        self.counter.setObjectName("counter")
        self.update()
        self.label.raise_()
        self.commandLinkButton.raise_()
        self.label_2.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.readFromJsonFile()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.label_2.setText(_translate("MainWindow", "History Data"))
        self.label.setText(_translate("MainWindow", "Data Collection"))
        self.label_3.setText(_translate("MainWindow", "Time:"))
        self.label_4.setText(_translate("MainWindow", "Total Count:"))
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.updateGraphOnClick)
