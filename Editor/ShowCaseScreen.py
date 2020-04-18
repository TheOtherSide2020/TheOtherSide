import datetime
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
# class for pollingScreen UI
from PyQt5.QtWidgets import QMessageBox

from Editor.UploadScreen import UploadScreen


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = os.path.dirname(sys.argv[0])
    except Exception:
        base_path = os.path.dirname(sys.argv[0])
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
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Entry Saved")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

            file = open(os.path.join(resource_path('TemplateJsonInstance/ShowcaseInstance/'),
                                     self.EntryName.toPlainText() + ".json"), 'w')
            with file as json_file:
                json.dump(ShowCaseSystemRecord, json_file)

    def undoDoubleClick(self):
        ShowCaseScreen.doubleClicked = 0
        # new content added
        self.listWidget.clearSelection
        ShowCaseScreen.VideoFileName = ''
        ShowCaseScreen.ImageFileName = ''

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1519, 957)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Images/The Other Side_logo.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(280, 70, 1301, 891))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(resource_path("Images/Showcase.png")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setIndent(10)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(685, 580, 181, 51))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option2.setFont(font)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("textBrowser_2")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(780, 830, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Option2.sizePolicy().hasHeightForWidth())
        self.Option3.setSizePolicy(sizePolicy)
        self.Option3.setSizeIncrement(QtCore.QSize(8, 8))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option3.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option3.setFont(font)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("textBrowser_3")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(1330, 710, 181, 41))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option4.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option4.setFont(font)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("textBrowser_4")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setGeometry(QtCore.QRect(310, 605, 181, 71))
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option1.setFont(font)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("textBrowser_5")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(1320, 10, 130, 41))
        self.Save.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 110, 281, 851))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignVCenter)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(30, 860, 211, 41))
        self.Delete.setObjectName("pushButton_2")
        self.CreateNewContent = QtWidgets.QPushButton(self.centralwidget)
        self.CreateNewContent.setGeometry(QtCore.QRect(30, 810, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateNewContent.sizePolicy().hasHeightForWidth())
        self.CreateNewContent.setSizePolicy(sizePolicy)
        self.CreateNewContent.setStyleSheet("border-width: 2px;")
        self.CreateNewContent.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 1581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 10, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("Images/directional-chevron-back-512.ico")),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.EntryName = QtWidgets.QTextEdit(self.centralwidget)
        self.EntryName.setGeometry(QtCore.QRect(600, 20, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(50)
        self.EntryName.setFont(font)
        self.EntryName.setAutoFillBackground(False)
        self.EntryName.setStyleSheet("background-color:rgb(225, 225, 225)")
        self.EntryName.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.EntryName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EntryName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EntryName.setLineWidth(2)
        self.EntryName.setMidLineWidth(3)
        self.EntryName.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.EntryName.setReadOnly(False)
        self.EntryName.setOverwriteMode(True)
        self.EntryName.setObjectName("textEdit")
        self.Upload = QtWidgets.QPushButton(self.centralwidget)
        self.Upload.setGeometry(QtCore.QRect(1170, 420, 191, 61))
        self.Upload.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1060, 360, 411, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Question = QtWidgets.QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(1050, 280, 411, 81))
        self.Question.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Question.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Question.setFont(font)
        self.Question.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Question.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("background-color:grey;\n"
                                   "")
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1571, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setText("")
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 281, 891))
        self.label_5.setAutoFillBackground(True)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.commandLinkButton.raise_()
        self.Option1.raise_()
        self.Option2.raise_()
        self.Option3.raise_()
        self.Option4.raise_()
        self.Save.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.Delete.raise_()
        self.CreateNewContent.raise_()
        self.line.raise_()
        self.EntryName.raise_()
        self.Upload.raise_()
        self.label_3.raise_()
        self.Question.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Option1.anchorClicked['QUrl'].connect(self.listWidget.clearSelection)
        self.CreateNewContent.clicked.connect(self.Question.clear)
        self.CreateNewContent.clicked.connect(self.label_3.clear)
        self.CreateNewContent.clicked.connect(self.Option1.clear)
        self.CreateNewContent.clicked.connect(self.Option2.clear)
        self.CreateNewContent.clicked.connect(self.Option3.clear)
        self.CreateNewContent.clicked.connect(self.Option4.clear)
        self.CreateNewContent.clicked.connect(self.undoDoubleClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.readFromJsonFile()
        self.Save.clicked.connect(self.save)
        self.CreateNewContent.clicked.connect(self.label_3.clear)
        self.CreateNewContent.clicked.connect(self.Option1.clear)
        self.CreateNewContent.clicked.connect(self.Option2.clear)
        self.CreateNewContent.clicked.connect(self.Option3.clear)
        self.CreateNewContent.clicked.connect(self.Option4.clear)
        self.CreateNewContent.clicked.connect(self.EntryName.clear)
        self.CreateNewContent.clicked.connect(self.changeLabel)
        self.Delete.clicked.connect(self.deleteItem)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.populateTextForEdit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeLabel(self):
        self.Upload.setText("Upload Media Files")

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
            msgBox.setText(self.EntryName.toPlainText()+ " Deleted")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def populateTextForEdit(self):
        text = self.listWidget.currentItem().text()
        self.Question.setPlainText(text)
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
                    # add video and image path here

                    ShowCaseScreen.VideoFileName = data['videoPath']
                    ShowCaseScreen.ImageFileName = data['picturePath']
                    ShowCaseScreen.doubleClicked = 1
                    uploadScreen = UploadScreen()
                    uploadScreen.loadImage(ShowCaseScreen.ImageFileName)
                    print(ShowCaseScreen.VideoFileName)
                    if ShowCaseScreen.VideoFileName != '':
                        uploadScreen.loadVideo(ShowCaseScreen.VideoFileName)
                    self.Upload.setText("View Media Files")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.Option1.setPlaceholderText(_translate("MainWindow", "Option1"))
        self.Option2.setPlaceholderText(_translate("MainWindow", "Option2"))
        self.Option3.setPlaceholderText(_translate("MainWindow", "Option3"))
        self.Option4.setPlaceholderText(_translate("MainWindow", "Option4"))
        self.Question.setPlaceholderText(_translate("MainWindow", "Question"))
        self.EntryName.setPlaceholderText(_translate("MainWindow", "Entry Name"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.listWidget.setSortingEnabled(True)
        self.label_2.setText(_translate("MainWindow", "Content List"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.CreateNewContent.setText(_translate("MainWindow", "Create New Content"))
        self.Upload.setText(_translate("MainWindow", "Upload"))


def showWindow(w1):
    w1.show()


