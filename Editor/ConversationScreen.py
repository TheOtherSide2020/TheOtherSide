import datetime
import json
import os
import sys
import time

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
        return relative_path

    return os.path.join(base_path, relative_path)


# class for conversation screen,
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
        self.pushButton_2.setEnabled(False)
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
        ts = time.time()
        PollingSystemRecord = {
            "name": self.EntryName.toPlainText(),
            "type": "text",
            "question": self.Question.toPlainText(),
            "createdOn": datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
            "lastUpdated": datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
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
        msgBox.setText(self.EntryName.toPlainText() + " saved!")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        x = msgBox.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1550, 961)
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
        self.label.setGeometry(QtCore.QRect(440, 100, 1091, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(resource_path("Images/Conversation_circle.png")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(21)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Question = QtWidgets.QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(1160, 260, 328, 111))
        self.Question.setFrameShape(QtWidgets.QFrame.StyledPanel)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Futura")
        self.Question.setFont(font)
        self.Question.setFont(font)
        self.Question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Question.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Question.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Question.setTabChangesFocus(True)
        self.Question.setLineWrapColumnOrWidth(3)
        self.Question.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Question.setObjectName("textBrowser")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(785, 530, 168, 74))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Futura")
        self.Option2.setFont(font)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("textBrowser_2")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(850, 770, 321, 101))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option3.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Futura")
        self.Option3.setFont(font)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("textBrowser_3")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(1350, 670, 166, 71))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("futura")
        self.Option4.setFont(font)
        self.Option4.setTabChangesFocus(True)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("textBrowser_4")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setFont(font)
        self.Option1.setGeometry(QtCore.QRect(450, 590, 181, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Option4.sizePolicy().hasHeightForWidth())
        self.Option1.setSizePolicy(sizePolicy)
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("textBrowser_5")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 130, 421, 871))
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
        self.listWidget.setStyleSheet("QListWidget::item {"
                                      "color: black;"
                                      "filter: alpha(opacity=20);"
                                      "}"
                                      "QListWidget::item:selected {"
                                      "background-color: rgba(173, 162, 231, 0.5);"
                                      "}")
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignVCenter)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(23, 8, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path(resource_path("Images/back.png"))),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1561, 991))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(resource_path("Images/General background.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 870, 231, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("border: 2px solid none\n"
                                        "; border-radius:15px;")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("Images/Create.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(220, 120))
        self.pushButton_3.setAutoRepeatDelay(299)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 870, 101, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("Images/Delete_active.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1460, 0, 91, 51))
        self.pushButton_6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("Images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(150, 35))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.EntryName = QtWidgets.QTextEdit(self.centralwidget)
        self.EntryName.setGeometry(QtCore.QRect(700, 5, 491, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily('Futura')
        font.setBold(False)
        font.setWeight(50)
        self.EntryName.setFont(font)
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
        self.label_4.raise_()
        self.commandLinkButton.raise_()
        self.label.raise_()
        self.Question.raise_()
        self.Option1.raise_()
        self.Option2.raise_()
        self.Option3.raise_()
        self.Option4.raise_()
        self.listWidget.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_6.raise_()
        self.EntryName.raise_()
        self.commandLinkButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def disableDeleteButton(self):
        self.pushButton_2.setEnabled(False)

    def deleteItem(self):
        self.Question.clear()
        self.Option1.clear()
        self.Option2.clear()
        self.Option3.clear()
        self.Option4.clear()
        items = self.listWidget.selectedItems()
        for item in items:
            # delete the file
            for fileName in os.listdir(resource_path('TemplateJsonInstance/TextInstance/')):
                if fileName == self.listWidget.currentItem().text() + ".json":
                    os.remove(os.path.join(resource_path('TemplateJsonInstance/TextInstance/'), fileName))

            self.listWidget.takeItem(self.listWidget.row(item))

            # delete confirmation
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(self.EntryName.toPlainText() + " Deleted")
            msgBox.setWindowTitle("Success")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msgBox.exec_()

    def populateTextForEdit(self):
        self.pushButton_2.setEnabled(True)
        text = self.listWidget.currentItem().text()
        self.EntryName.setPlainText(text)
        # find the file corresponding to the entry name
        for fileName in os.listdir(resource_path('TemplateJsonInstance/TextInstance/')):
            # get the record from json for edit
            if fileName == text + ".json":
                with open(os.path.join(resource_path('TemplateJsonInstance/TextInstance/'), fileName),
                          'r') as json_file:
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
        self.pushButton_2.setEnabled(False)
        self.label_2.setText(_translate("MainWindow", "Content List"))
        self.pushButton_6.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.Question.clear)
        self.pushButton_3.clicked.connect(self.Option1.clear)
        self.pushButton_3.clicked.connect(self.Option2.clear)
        self.pushButton_3.clicked.connect(self.Option3.clear)
        self.pushButton_3.clicked.connect(self.Option4.clear)
        self.pushButton_3.clicked.connect(self.EntryName.clear)
        self.pushButton_3.clicked.connect(self.disableDeleteButton)
        self.pushButton_2.clicked.connect(self.deleteItem)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(self.populateTextForEdit)
        self.readFromJsonFile()
