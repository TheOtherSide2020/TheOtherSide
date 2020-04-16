import datetime
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QFileDialog, QHBoxLayout, QLabel,
                             QSlider, QStyle, QVBoxLayout)
from PyQt5.QtWidgets import QMainWindow, QPushButton
# class for pollingScreen UI
from PyQt5.QtWidgets import QMessageBox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def changeWindow(w1, w2):
    w1.hide()
    w2.show()


class ShowCaseScreen(QtWidgets.QMainWindow):
    fileName = " "
    ImageFileName = ""
    VideoFileName = ""

    def is_file_empty(self, file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    def readFromJsonFile(self):
        for filename in os.listdir(resource_path('TemplateJsonInstance/ShowcaseInstance/')):
            with open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'), filename),
                      'r') as json_file:
                data = json.load(json_file)
                self.listWidget.addItem(data['name'])

    # append the field to the json file
    # append this entry to content list

    def save(self):
        # check if string is empty
        if self.label_3.text() != "" and self.textBrowser.toPlainText() != "" and self.Option1.toPlainText() != "" and self.Option2.toPlainText() != "" and self.Option3.toPlainText() != "" and self.Option4.toPlainText() != "" and self.EntryName.toPlainText() != "":

            if self.listWidget.count() == 0:
                ShowCaseSystemRecord = {
                    "ShowCaseRecord": [{
                        "name": self.EntryName.toPlainText(),
                        "type": "showCase",
                        "createdOn": datetime.datetime.now().timestamp(),
                        "lastUpdated": datetime.datetime.now().timestamp(),
                        "question": self.textBrowser.toPlainText(),
                        "videoPath": UploadScreen.VideofileName,
                        "picturePath": UploadScreen.ImagefileName,
                        "displayText": self.label_3.toPlainText(),
                        "options": [
                            self.Option1.toPlainText(),
                            self.Option2.toPlainText(),
                            self.Option3.toPlainText(),
                            self.Option4.toPlainText()
                        ]

                    }]

                }
                if UploadScreen.ImagefileName == "":
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("ShowCase Template needs an Image File")
                    msgBox.setWindowTitle("Error")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    x = msgBox.exec_()

                file = open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'),
                                         self.EntryName.toPlainText() + ".json"),
                            'w')
                with file as json_file:
                    json.dump(ShowCaseSystemRecord, json_file)
                    self.listWidget.addItem(self.EntryName.toPlainText())

            # check if this list item has already been added:  remove duplicates
            else:
                items = self.listWidget.findItems(self.EntryName.toPlainText(), Qt.MatchFixedString)

                if items.__len__() == 0:
                    ShowCaseSystemRecord = {

                        "name": self.EntryName.toPlainText(),
                        "type": "showCase",
                        "question": self.textBrowser.toPlainText(),
                        "createdOn": datetime.datetime.now().timestamp(),
                        "lastUpdated": datetime.datetime.now().timestamp(),
                        "videoPath": UploadScreen.VideoFileName,
                        "picturePath": UploadScreen.ImageFileName,
                        "displayText": self.label_3.text(),
                        "options": [
                            self.Option1.toPlainText(),
                            self.Option2.toPlainText(),
                            self.Option3.toPlainText(),
                            self.Option4.toPlainText()
                        ]

                    }
                    # append this entry to json file
                    file = open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'),
                                             self.EntryName.toPlainText() + ".json"),
                                'w')
                    with file as json_file:
                        json.dump(ShowCaseSystemRecord, json_file)
                        self.listWidget.addItem(self.EntryName.toPlainText())

                else:
                    # add functionality to allow for the same content to be modified.
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("The Entry Name " + self.EntryName.toPlainText() + " already exists!")
                    msgBox.setWindowTitle("Error")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    x = msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Fields cannot be left blank")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1576, 957)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('Images/The Other Side_logo.png')), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 70, 1301, 891))
        self.label.setPixmap(QtGui.QPixmap(resource_path("Images/MacBook Pro - 1.png")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(21)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setGeometry(QtCore.QRect(700, 550, 180, 58))
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option1.setFont(font)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("textBrowser_2")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(790, 810, 321, 51))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option2.setFont(font)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("textBrowser_3")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(1340, 690, 181, 45))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option3.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option3.setFont(font)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("textBrowser_4")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(310, 610, 181, 71))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option4.setTabChangesFocus(True)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("textBrowser_5")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option4.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1430, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 110, 281, 851))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignVCenter)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 860, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1290, 10, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 1581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(42, 10, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path('Images/directional-chevron-back-512.ico')), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(35, 35))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.EntryName = QtWidgets.QTextEdit(self.centralwidget)
        self.EntryName.setGeometry(QtCore.QRect(290, 20, 961, 41))
        self.EntryName.setAutoFillBackground(True)
        self.EntryName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EntryName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EntryName.setLineWidth(2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EntryName.setFont(font)
        self.EntryName.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.EntryName.setReadOnly(False)
        self.EntryName.setOverwriteMode(True)
        self.EntryName.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1170, 420, 191, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1060, 360, 411, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1060, 270, 411, 81))
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.label.raise_()
        self.commandLinkButton.raise_()
        self.Option1.raise_()
        self.Option2.raise_()
        self.Option3.raise_()
        self.Option4.raise_()
        self.pushButton.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.line.raise_()
        self.EntryName.raise_()
        self.pushButton_4.raise_()
        self.textBrowser.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Option1.anchorClicked['QUrl'].connect(self.listWidget.clearSelection)
        self.pushButton_3.clicked.connect(self.textBrowser.clear)
        self.pushButton_3.clicked.connect(self.label_3.clear)
        self.pushButton_3.clicked.connect(self.Option1.clear)
        self.pushButton_3.clicked.connect(self.Option2.clear)
        self.pushButton_3.clicked.connect(self.Option3.clear)
        self.pushButton_3.clicked.connect(self.Option4.clear)
        self.commandLinkButton.clicked.connect(self.commandLinkButton.showMenu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.readFromJsonFile()
        self.pushButton.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.label_3.clear)
        self.pushButton_3.clicked.connect(self.Option1.clear)
        self.pushButton_3.clicked.connect(self.Option2.clear)
        self.pushButton_3.clicked.connect(self.Option3.clear)
        self.pushButton_3.clicked.connect(self.Option4.clear)
        self.pushButton_2.clicked.connect(self.deleteItem)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.populateTextForEdit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def deleteItem(self):
        items = self.listWidget.selectedItems()
        for item in items:
            # delete the file
            for fileName in os.listdir(resource_path('TemplateJsonInstance/ShowcaseInstance/')):
                if fileName == self.listWidget.currentItem().text() + ".json":
                    os.remove(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'), fileName))

            self.listWidget.takeItem(self.listWidget.row(item))

            # delete confirmation
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Field Deleted")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def populateTextForEdit(self):
        text = self.listWidget.currentItem().text()
        self.textBrowser.setPlainText(text)
        # find the file corresponding to the entry name
        for fileName in os.listdir(resource_path('TemplateJsonInstance/ShowcaseInstance/')):
            # get the record from json for edit
            if fileName == text + ".json":
                with open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'), fileName),
                          'r') as json_file:
                    data = json.load(json_file)
                    self.label_3.setText(data['displayText'])
                    self.EntryName.setPlainText(data['name'])
                    self.textBrowser.setPlainText(data['question'])
                    self.Option1.setPlainText(data['options'][0])
                    self.Option2.setPlainText(data['options'][1])
                    self.Option3.setPlainText(data['options'][2])
                    self.Option4.setPlainText(data['options'][3])
                    ShowCaseScreen.VideoFileName = data['videoPath']
                    ShowCaseScreen.ImageFileName = data['picturePath']


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.Option1.setPlaceholderText(_translate("MainWindow", "Option1"))
        self.Option2.setPlaceholderText(_translate("MainWindow", "Option2"))
        self.Option3.setPlaceholderText(_translate("MainWindow", "Option3"))
        self.Option4.setPlaceholderText(_translate("MainWindow", "Option4"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Question"))
        self.EntryName.setPlaceholderText(_translate("MainWindow", "Entry Name"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.listWidget.setSortingEnabled(True)
        self.label_2.setText(_translate("MainWindow", "Content List"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "Upload"))


class UploadScreen(QtWidgets.QMainWindow):
    VideoFileName = ""
    ImageFileName = ""

    def play(self):
        self.pushButton_2.hide()
        self.pushButton_5.show()
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def openFile(self):

        UploadScreen.VideoFileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                                    QDir.homePath())
        url = QUrl.fromLocalFile(UploadScreen.VideoFileName)

        self.Video = url.fileName()

        # set the file name as this in the previous screen

        if UploadScreen.VideoFileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(UploadScreen.VideoFileName)))
            self.playButton.setEnabled(True)

    def openImageFile(self):

        UploadScreen.ImagefileName, _ = QFileDialog.getOpenFileName(self, "Open Image",
                                                                    QDir.homePath())

        url = QUrl.fromLocalFile(UploadScreen.ImagefileName)

        self.Image = url.fileName()

        if UploadScreen.ImagefileName != '':
            self.pixmap = QPixmap(UploadScreen.ImagefileName)
            self.imageWidget.setPixmap(self.pixmap)
            self.imageWidget.show()
            self.pushButton_4.show()

    def loadImage(self):
        self.Image = ShowCaseScreen.ImageFileName
        print(ShowCaseScreen.ImageFileName)

        if ShowCaseScreen.ImageFileName != '':
            self.pixmap = QPixmap(ShowCaseScreen.ImageFileName)
            self.imageWidget.setPixmap(self.pixmap)
            self.imageWidget.show()
            self.pushButton_4.show()

    def loadVideo(self):
        url = QUrl.fromLocalFile(ShowCaseScreen.VideoFileName)

        self.Video = url.fileName()

        # set the file name as this in the previous screen

        if ShowCaseScreen.VideoFileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(ShowCaseScreen.VideoFileName)))
            self.playButton.setEnabled(True)

    def clearImage(self):
        self.imageWidget.close()
        self.pushButton_4.hide()

    def clearVideo(self):
        self.videoWidget.close()
        self.pushButton_2.show()
        self.positionSlider.hide()
        self.playButton.hide()
        self.pushButton_5.hide()

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.Video = ""
        self.Image = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 900)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowTitleHint , False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('Images/The Other Side_logo.png')), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(59, 140, 451, 431))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(184, 200, 101, 51))
        self.pushButton.setObjectName("pushButton")

        self.imageWidget = QLabel(self)
        self.imageWidget.setScaledContents(True)
        self.imageWidget.hide()

        layout = QVBoxLayout()
        layout.addWidget(self.imageWidget)

        self.widget.setLayout(layout)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(560, 139, 461, 431))
        self.widget_2.setAutoFillBackground(True)
        self.widget_2.setObjectName("widget_2")
        self.videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 10, 51, 41))
        self.commandLinkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('Images/directional-chevron-back-512.ico')), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(35, 35))
        self.commandLinkButton.setObjectName("commandLinkButton")

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)

        self.widget_2.setLayout(layout)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 200, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(990, 10, 81, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 590, 101, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 590, 101, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 80, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 630, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.pushButton.setText(_translate("MainWindow", "Upload"))
        self.pushButton_2.setText(_translate("MainWindow", "Upload"))
        self.pushButton.clicked.connect(self.openImageFile)
        self.pushButton_2.clicked.connect(self.openFile)
        self.label.setText(_translate("MainWindow", "Upload an image"))
        self.label_2.setText(_translate("MainWindow", "Upload a video (optional)"))
        self.label_3.setText(_translate("MainWindow",
                                        "You can upload either video or image, or both of them image will be the "
                                        "cover for idle status."))
        self.pushButton_4.setText(_translate("MainWindow", "Clear Image"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Clear Video"))
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.pushButton_5.clicked.connect(self.clearVideo)
        self.pushButton_4.clicked.connect(self.clearImage)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)


def showWindow(w1):
    w1.show()
