import datetime
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
# class for pollingScreen UI
from PyQt5.QtWidgets import QMessageBox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = os.path.dirname(sys.argv[0])
    except Exception:
        base_path = os.path.dirname(sys.argv[0])

    return os.path.join(base_path, relative_path)


class ConversationScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def is_file_empty(self, file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    def readFromJsonFile(self):
        for filename in os.listdir(resource_path('TemplateJsonInstance/TextInstance/')):
            with open(os.path.join(resource_path('TemplateJsonInstance/TextInstance/'), filename), 'r') as json_file:
                data = json.load(json_file)
                self.listWidget.addItem(data['name'])

    def save(self):
        # check if string is empty
        if self.Question.toPlainText() != "" and self.Option1.toPlainText() != "" and self.Option2.toPlainText() != "" and self.Option3.toPlainText() != "" and self.Option4.toPlainText() != "" and self.EntryName.toPlainText() != "":

            if self.listWidget.count() == 0:
                self.saveJson()
                self.listWidget.addItem(self.EntryName.toPlainText())

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
                            self.saveJson()

                else:
                    self.saveJson()
                    self.listWidget.addItem(self.EntryName.toPlainText())



        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Fields cannot be left blank")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def saveJson(self):
        PollingSystemRecord = {
            "name": self.EntryName.toPlainText(),
            "type": "text",
            "question": self.Question.toPlainText(),
            "createdOn": datetime.datetime.now().timestamp(),
            "lastUpdated": datetime.datetime.now().timestamp(),
            "options": [
                self.Option1.toPlainText(),
                self.Option2.toPlainText(),
                self.Option3.toPlainText(),
                self.Option4.toPlainText()
            ]

        }
        file = open(os.path.join(resource_path('TemplateJsonInstance/TextInstance/'),
                                 self.EntryName.toPlainText() + ".json"),
                    'w')
        with file as json_file:
            json.dump(PollingSystemRecord, json_file)

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Entry Saved")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        x = msgBox.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1576, 957)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('Images/The Other Side_logo.png')), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 1291, 920))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(resource_path('Images/Conversation_circle.png')))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(21)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Question = QtWidgets.QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(1150, 240, 365, 91))
        self.Question.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Question.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Question.setFont(font)
        self.Question.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Question.setObjectName("Question")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(680, 540, 200, 80))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option2.setFont(font)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("Option1")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(770, 830, 350, 100))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option3.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option3.setFont(font)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("Option2")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(1350, 700, 200, 80))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option4.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option4.setFont(font)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("Option3")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setGeometry(QtCore.QRect(290, 630, 240, 71))
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option1.setFont(font)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("Option4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1300, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")

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
        # this function reads the previous records in the json file
        self.readFromJsonFile()

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

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path('Images/directional-chevron-back-512.ico')), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.EntryName = QtWidgets.QTextBrowser(self.centralwidget)
        self.EntryName.setGeometry(QtCore.QRect(240, 10, 961, 41))
        self.EntryName.setAutoFillBackground(True)
        self.EntryName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EntryName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EntryName.setLineWidth(2)
        self.EntryName.setObjectName("Entry Name")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.EntryName.setFont(font)

        self.EntryName.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.EntryName.setReadOnly(False)
        self.EntryName.setOverwriteMode(True)
        self.EntryName.setObjectName("textEdit")
        self.commandLinkButton.raise_()
        self.label.raise_()
        self.Question.raise_()
        self.Option1.raise_()
        self.Option2.raise_()
        self.Option3.raise_()
        self.Option4.raise_()
        self.pushButton.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.Delete.raise_()
        self.CreateNewContent.raise_()
        self.line.raise_()
        self.EntryName.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.save)
        self.CreateNewContent.clicked.connect(self.Question.clear)
        self.CreateNewContent.clicked.connect(self.Option1.clear)
        self.CreateNewContent.clicked.connect(self.Option2.clear)
        self.CreateNewContent.clicked.connect(self.Option3.clear)
        self.CreateNewContent.clicked.connect(self.Option4.clear)
        self.CreateNewContent.clicked.connect(self.EntryName.clear)
        self.Delete.clicked.connect(self.deleteItem)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.populateTextForEdit)
        # self.commandLinkButton.clicked.connect()  #back functionality
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def deleteItem(self):
        items = self.listWidget.selectedItems()
        for item in items:
            # delete the file
            for fileName in os.listdir(resource_path('TemplateJsonInstance/TextInstance/')):
                if fileName == self.listWidget.currentItem().text() + ".json":
                    os.remove( os.path.join(resource_path('TemplateJsonInstance/TextInstance/'), fileName))

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
        self.EntryName.setPlainText(text)
        # find the file corresponding to the entry name
        for fileName in os.listdir(resource_path('TemplateJsonInstance/TextInstance/')):
            # get the record from json for edit
            if fileName == text + ".json":
                with open(os.path.join(resource_path('TemplateJsonInstance/TextInstance/'), fileName), 'r') as json_file:
                    data = json.load(json_file)
                    self.Question.setPlainText(data['question'])
                    self.Option1.setPlainText(data['options'][0])
                    self.Option2.setPlainText(data['options'][1])
                    self.Option3.setPlainText(data['options'][2])
                    self.Option4.setPlainText(data['options'][3])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.Question.setPlaceholderText(_translate("MainWindow", "Question"))
        self.Option1.setPlaceholderText(_translate("MainWindow", "Option1"))
        self.Option2.setPlaceholderText(_translate("MainWindow", "Option2"))
        self.Option3.setPlaceholderText(_translate("MainWindow", "Option3"))
        self.Option4.setPlaceholderText(_translate("MainWindow", "Option4"))
        self.EntryName.setPlaceholderText(_translate("MainWindow", "Entry Name"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.CreateNewContent.setText(_translate("MainWindow", "Create New Content"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Content List"))


