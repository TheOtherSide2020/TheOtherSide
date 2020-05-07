import datetime
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl
# class for pollingScreen UI
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QHBoxLayout, QSlider, QPushButton, QStyle

from Editor.UploadScreen import UploadScreen


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = os.path.dirname(sys.argv[0])
    except Exception:
        return relative_path
    return os.path.join(base_path, relative_path)


def changeWindow(w1, w2):
    w1.hide()
    w2.show()


class ShowCaseScreen(QtWidgets.QMainWindow):
    fileName = " "
    doubleClicked = 0
    ImageFileName = ""
    VideoFileName = ""

    def is_file_empty(self, file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1550, 994)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Images/The Other Side_logo.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(443, 130, 1091, 841))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(resource_path("Images/Showcase_cricle.png")))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setGeometry(QtCore.QRect(450, 590, 161, 121))
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(12)
        self.Option1.setFont(font)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("textBrowser_2")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(790, 570, 151, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Option2.sizePolicy().hasHeightForWidth())
        self.Option2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(12)
        self.Option2.setFont(font)
        self.Option2.setSizeIncrement(QtCore.QSize(8, 8))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("textBrowser_3")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(865, 830, 291, 91))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(12)
        self.Option3.setFont(font)
        self.Option3.setTabChangesFocus(True)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("textBrowser_4")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(1360, 710, 141, 71))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(12)
        self.Option4.setFont(font)
        self.Option4.setTabChangesFocus(True)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("textBrowser_5")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(1390, 0, 91, 51))
        self.Save.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("Images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Save.setIcon(icon1)
        self.Save.setIconSize(QtCore.QSize(150, 35))
        self.Save.setFlat(True)
        self.Save.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 120, 421, 871))
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 120, 421, 871))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(False)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(0)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setGridSize(QtCore.QSize(300, 50))
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignVCenter)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily("Futura")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(290, 900, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        self.Delete.setFont(font)
        self.Delete.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("Images/Delete_active.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.Delete.setIcon(icon2)
        self.Delete.setIconSize(QtCore.QSize(100, 100))
        self.Delete.setFlat(True)
        self.Delete.setObjectName("pushButton_2")
        self.CreateNewContent = QtWidgets.QPushButton(self.centralwidget)
        self.CreateNewContent.setGeometry(QtCore.QRect(40, 900, 231, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateNewContent.sizePolicy().hasHeightForWidth())
        self.CreateNewContent.setSizePolicy(sizePolicy)
        self.CreateNewContent.setStyleSheet("border: 2px solid none\n"
                                            "; border-radius:15px;")
        self.CreateNewContent.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("Images/Create.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreateNewContent.setIcon(icon3)
        self.CreateNewContent.setIconSize(QtCore.QSize(220, 120))
        self.CreateNewContent.setAutoRepeatDelay(299)
        self.CreateNewContent.setFlat(True)
        self.CreateNewContent.setObjectName("pushButton_3")
        self.EntryName = QtWidgets.QTextEdit(self.centralwidget)
        self.EntryName.setGeometry(QtCore.QRect(700, 10, 491, 35))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.EntryName.setFont(font)
        self.EntryName.setAlignment(QtCore.Qt.AlignVCenter)
        self.EntryName.setAutoFillBackground(False)
        self.EntryName.setStyleSheet("background-color:white\n"
                                     "")
        self.EntryName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EntryName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EntryName.setLineWidth(2)
        self.EntryName.setMidLineWidth(3)
        self.EntryName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EntryName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EntryName.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.EntryName.setTabChangesFocus(True)
        self.EntryName.setReadOnly(False)
        self.EntryName.setOverwriteMode(True)
        self.EntryName.setObjectName("textEdit")
        self.Upload = QtWidgets.QPushButton(self.centralwidget)
        self.Upload.setGeometry(QtCore.QRect(1240, 360, 121, 51))
        self.Upload.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("Images/Upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Upload.setIcon(icon4)
        self.Upload.setIconSize(QtCore.QSize(120, 170))
        self.Upload.setAutoDefault(False)
        self.Upload.setFlat(True)
        self.Upload.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1170, 420, 271, 61))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.Question = QtWidgets.QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(1100, 250, 341, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Question.sizePolicy().hasHeightForWidth())
        self.Question.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily('Futura')
        font.setPointSize(12)
        self.Question.setFont(font)
        self.Question.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextSelectableByMouse)
        self.Question.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 281, 891))
        self.label_5.setAutoFillBackground(True)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1010, 110, 501, 441))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("border: 0px solid blue; \n"
                                   "                                    border-radius: 215px;")
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 70, 351, 51))
        self.label_7.setStyleSheet("background-color:white;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1550, 991))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(resource_path("Images/General background.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(23, 8, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path(resource_path("Images/directional-chevron-back-512.ico"))),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.label_4.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.Option1.raise_()
        self.Option2.raise_()
        self.Option3.raise_()
        self.Option4.raise_()
        self.Save.raise_()
        self.listWidget.raise_()
        self.Delete.raise_()
        self.CreateNewContent.raise_()
        self.EntryName.raise_()
        self.Upload.raise_()
        self.label_3.raise_()
        self.commandLinkButton.raise_()
        self.Question.raise_()
        self.label_7.raise_()
        self.label_2.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def readFromJsonFile(self):
        for filename in os.listdir(resource_path('TemplateJsonInstance/ShowcaseInstance/')):
            with open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'), filename),
                      'r') as json_file:
                data = json.load(json_file)
                self.listWidget.addItem(data['name'])

        # checks if this media file exists or not

    def checkIfMediaFilesExist(self, data):

        try:
            f = open(data['picturePath'])
            # Do something with the file
        except IOError:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(
                "Path for the image file is invalid, Please upload an image file for using the Showcase template")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap(resource_path("Images/Upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Upload.setIcon(icon4)
            return False

        if data['videoPath'] != '':
            try:
                f = open(data['videoPath'])
                # Do something with the file
            except IOError:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(
                    "The path given for video file is invalid. Please check is present in the current location.")
                msgBox.setWindowTitle("Error")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                x = msgBox.exec_()
        return True

        # append the field to the json file
        # append this entry to content list

    def save(self):
        self.Delete.setEnabled(False)
        # check if string is empty
        if self.label_3.text() != "" and self.Question.toPlainText() != "" and self.Option1.toPlainText() != "" and self.Option2.toPlainText() != "" and self.Option3.toPlainText() != "" and self.Option4.toPlainText() != "" and self.EntryName.toPlainText() != "":

            if self.listWidget.count() == 0:
                ShowCaseSystemRecord = {

                    "name": self.EntryName.toPlainText(),
                    "type": "showCase",
                    "createdOn": datetime.datetime.now().timestamp(),
                    "lastUpdated": datetime.datetime.now().timestamp(),
                    "question": self.Question.toPlainText(),
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
                ShowCaseScreen.ImageFileName = UploadScreen.ImageFileName
                ShowCaseScreen.VideoFileName = UploadScreen.VideoFileName

                if UploadScreen.ImageFileName == "":
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("ShowCase Template needs an Image File")
                    msgBox.setWindowTitle("Error")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    x = msgBox.exec_()
                else:
                    file = open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'),
                                             self.EntryName.toPlainText() + ".json"),
                                'w')
                    with file as json_file:
                        json.dump(ShowCaseSystemRecord, json_file)
                        self.listWidget.addItem(self.EntryName.toPlainText())
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setText(self.EntryName.toPlainText() + "saved!")
                        msgBox.setWindowTitle("Error")
                        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        x = msgBox.exec_()

            # check if this list item has already been added:  remove duplicates
            else:
                items = self.listWidget.findItems(self.EntryName.toPlainText(), Qt.MatchFixedString)

                if items.__len__() != 0:

                    # add functionality to allow for the same content to be modified.
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText(
                        "Do you want to edit the entry " + self.EntryName.toPlainText() + " previously saved")
                    msgBox.setWindowTitle("Info")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    x = msgBox.exec_()
                    if x == QMessageBox.Ok:
                        if items.__len__() != 0:
                            self.SavetoJson()
                else:
                    self.SavetoJson()
                    self.listWidget.addItem(self.EntryName.toPlainText())
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Fields cannot be left blank")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def checkDuplicateEntry(self):
        print('yes')
        if self.Question.textChanged():
            return True
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("This content entry already exists, please change one or more fields to be "
                           "able to save a duplicate entry under the same entry name")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()
            return False

    def SavetoJson(self):
        ShowCaseSystemRecord = {

            "name": self.EntryName.toPlainText(),
            "type": "showCase",
            "question": self.Question.toPlainText(),
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
        ShowCaseScreen.ImageFileName = UploadScreen.ImageFileName
        ShowCaseScreen.VideoFileName = UploadScreen.VideoFileName
        if UploadScreen.ImageFileName == "":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("ShowCase Template needs an Image File")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()
        else:
            if self.checkDuplicateEntry:
                file = open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'),
                                         self.EntryName.toPlainText() + ".json"), 'w')
                with file as json_file:
                    json.dump(ShowCaseSystemRecord, json_file)
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText(self.EntryName.toPlainText() + " saved!")
                msgBox.setWindowTitle("Success")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                x = msgBox.exec_()

    def undoDoubleClick(self):
        ShowCaseScreen.doubleClicked = 0
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("Images/Upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Upload.setIcon(icon4)
        # new content added
        self.listWidget.clearSelection
        self.Delete.setEnabled(False)
        UploadScreen.ImageFileName = ''
        UploadScreen.VideoFileName = ''
        ShowCaseScreen.VideoFileName = ''
        ShowCaseScreen.ImageFileName = ''

    def play(self):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(UploadScreen.VideoFileName)))
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

    def deleteItem(self):
        self.Question.clear()
        self.label_3.clear()
        self.Option1.clear()
        self.Option2.clear()
        self.Option3.clear()
        self.Option4.clear()
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
            msgBox.setText(self.EntryName.toPlainText() + " Deleted")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def populateTextForEdit(self):
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("Images/View.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Upload.setIcon(icon4)
        text = self.listWidget.currentItem().text()
        self.Question.setPlainText(text)
        self.Delete.setEnabled(True)
        # find the file corresponding to the entry name
        for fileName in os.listdir(resource_path('TemplateJsonInstance/ShowcaseInstance/')):
            # get the record from json for edit
            if fileName == text + ".json":
                with open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'), fileName),
                          'r') as json_file:
                    data = json.load(json_file)
                    self.label_3.setText(data['displayText'])
                    self.EntryName.setPlainText(data['name'])
                    self.Question.setPlainText(data['question'])
                    self.Option1.setPlainText(data['options'][0])
                    self.Option2.setPlainText(data['options'][1])
                    self.Option3.setPlainText(data['options'][2])
                    self.Option4.setPlainText(data['options'][3])
                    if self.checkIfMediaFilesExist(data):
                        # add video and image path here
                        ShowCaseScreen.VideoFileName = data['videoPath']
                        ShowCaseScreen.ImageFileName = data['picturePath']
                        ShowCaseScreen.doubleClicked = 1
                        uploadScreen = UploadScreen()
                        uploadScreen.loadImage(ShowCaseScreen.ImageFileName)
                        if ShowCaseScreen.VideoFileName != '':
                            uploadScreen.loadVideo(ShowCaseScreen.VideoFileName)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.Option1.setPlaceholderText(_translate("MainWindow", "Option1"))
        self.Option2.setPlaceholderText(_translate("MainWindow", "Option2"))
        self.Option3.setPlaceholderText(_translate("MainWindow", "Option3"))
        self.Option4.setPlaceholderText(_translate("MainWindow", "Option4"))
        self.Question.setPlaceholderText(_translate("MainWindow", "Question"))
        self.EntryName.setPlaceholderText(_translate("MainWindow", "Entry Name"))
        self.listWidget.setSortingEnabled(True)
        self.label_2.setText(_translate("MainWindow", "Content List"))
        self.Delete.setEnabled(False)

        self.Option1.anchorClicked['QUrl'].connect(self.listWidget.clearSelection)
        self.CreateNewContent.clicked.connect(self.Question.clear)
        self.CreateNewContent.clicked.connect(self.label_3.clear)
        self.CreateNewContent.clicked.connect(self.Option1.clear)
        self.CreateNewContent.clicked.connect(self.Option2.clear)
        self.CreateNewContent.clicked.connect(self.Option3.clear)
        self.CreateNewContent.clicked.connect(self.Option4.clear)
        self.CreateNewContent.clicked.connect(self.undoDoubleClick)

        self.readFromJsonFile()
        self.Save.clicked.connect(self.save)
        self.CreateNewContent.clicked.connect(self.EntryName.clear)
        self.Delete.clicked.connect(self.deleteItem)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(self.populateTextForEdit)


def showWindow(w1):
    w1.show()
