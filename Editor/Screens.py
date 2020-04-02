# class for second Screens :
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# class for pollingScreen UI
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Polling Screen Functionality
class PollingScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def is_file_empty(self, file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    def readFromJsonFile(self):
        is_empty = self.is_file_empty(resource_path('PollingSystemRecords.txt'))
        if not is_empty:
            with open(resource_path('PollingSystemRecords.txt'), 'r') as json_file:
                data = json.load(json_file)
                for p in data['PollingSystemRecord']:
                    self.listWidget.addItem(p['EntryName'])

    def appendToJsonFile(self, PollingSystemRecord):
        try:
            with open(resource_path('PollingSystemRecords.txt')) as json_file:
                data = json.load(json_file)
                data['PollingSystemRecord'].append(PollingSystemRecord)

            with open(resource_path('PollingSystemRecords.txt'), 'w') as json_file:
                json.dump(data, json_file)
        except FileNotFoundError as exc:
            pass

    # append the field to the json file
    # append this entry to content list

    def save(self):
        # check if string is empty
        if self.Question.toPlainText() != "" and self.Option1.toPlainText() != "" and self.Option2.toPlainText() != "" and self.Option3.toPlainText() != "" and self.Option4.toPlainText() != "" and self.EntryName.toPlainText() != "":

            if self.listWidget.count() == 0:
                PollingSystemRecord = {
                    "PollingSystemRecord": [{
                        "EntryName": self.EntryName.toPlainText(),
                        "Question": self.Question.toPlainText(),
                        "Option1": self.Option1.toPlainText(),
                        "Option2": self.Option2.toPlainText(),
                        "Option3": self.Option3.toPlainText(),
                        "Option4": self.Option4.toPlainText()
                    }]
                }

                with open(resource_path('PollingSystemRecords.txt'), 'w') as json_file:
                    json.dump(PollingSystemRecord, json_file)

                self.listWidget.addItem(self.EntryName.toPlainText())

            # check if this list item has already been added:  remove duplicates
            else:
                items = self.listWidget.findItems(self.EntryName.toPlainText(), Qt.MatchFixedString)

                if items.__len__() == 0:
                    PollingSystemRecord = {
                        "EntryName": self.EntryName.toPlainText(),
                        "Question": self.Question.toPlainText(),
                        "Option1": self.Option1.toPlainText(),
                        "Option2": self.Option2.toPlainText(),
                        "Option3": self.Option3.toPlainText(),
                        "Option4": self.Option4.toPlainText()

                    }
                    # append this entry to json file
                    self.appendToJsonFile(PollingSystemRecord)
                    self.listWidget.addItem(self.EntryName.toPlainText())

                else:
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1576, 964)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('The Other Side_logo.png')), QtGui.QIcon.Normal,
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
        self.label.setPixmap(QtGui.QPixmap(resource_path('PollingScreen.png')))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(21)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Question = QtWidgets.QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(1070, 260, 371, 95))
        self.Question.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Question.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Question.setFont(font)
        self.Question.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Question.setObjectName("Question")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setGeometry(QtCore.QRect(700, 540, 151, 55))
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option1.setFont(font)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("Option1")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(840, 780, 201, 65))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option2.setFont(font)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("Option2")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(1340, 680, 151, 65))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option3.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option3.setFont(font)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("Option3")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(310, 600, 201, 71))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option4.setTabChangesFocus(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Option4.setFont(font)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("Option4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1430, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 110, 281, 851))
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
        self.listWidget.setObjectName("listWidget")
        # this function reads the previous records in the json file
        self.readFromJsonFile()

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 860, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1290, 10, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")

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
        icon1.addPixmap(QtGui.QPixmap(resource_path('directional-chevron-back-512.ico')), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
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
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.line.raise_()
        self.EntryName.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.Question.clear)
        self.pushButton_3.clicked.connect(self.Option1.clear)
        self.pushButton_3.clicked.connect(self.Option2.clear)
        self.pushButton_3.clicked.connect(self.Option3.clear)
        self.pushButton_3.clicked.connect(self.Option4.clear)
        self.pushButton_2.clicked.connect(self.deleteItem)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.populateTextForEdit)
        # self.commandLinkButton.clicked.connect()  #back functionality
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def deleteItem(self):
        items = self.listWidget.selectedItems()
        for item in items:
            self.listWidget.takeItem(self.listWidget.row(item))
        # remove the entry from the json file


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
        # get the record from json for edit
        with open(resource_path('PollingSystemRecords.txt'), 'r') as json_file:
            data = json.load(json_file)
            for p in data['PollingSystemRecord']:
                if text == p['EntryName']:
                    self.Question.setPlainText(p['Question'])
                    self.Option1.setPlainText(p['Option1'])
                    self.Option2.setPlainText(p['Option2'])
                    self.Option3.setPlainText(p['Option3'])
                    self.Option4.setPlainText(p['Option4'])

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
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Content List"))


# class for Second Screen, This Screen presents the option to choose between templates, Polling, conversational,
# Showcase
class Screen2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 849)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('The Other Side_logo.png')), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 270, 311, 311))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 270, 311, 311))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 270, 311, 311))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 120, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.commandLinkButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path('directional-chevron-back-512.ico')), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.pushButton.setText(_translate("MainWindow", "ShowCase"))
        self.pushButton_2.setText(_translate("MainWindow", "Polling System"))
        self.pushButton_3.setText(_translate("MainWindow", "Conversation"))
        self.label.setText(_translate("MainWindow", "Select Your Template"))


# class for first Screen, This Screen presents the option to choose the content editor or the data collection editor
class Screen1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 851)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path('The Other Side_logo.png')), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(10.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 421, 371))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 230, 401, 371))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.pushButton.setText(_translate("MainWindow", "Content Editor"))
        self.pushButton_2.setText(_translate("MainWindow", "Data Collection"))


# class for the Data collection Screen UI
class DataCollectionScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 851)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/The Other Side_logo.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 281, 871))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 130, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.label.setText(_translate("MainWindow", "How Do You Learn A New Language?"))
        self.label_2.setText(_translate("MainWindow", "History Data"))


def changeWindow(w1, w2):
    w1.hide()
    w2.show()


def main():
    app = QtWidgets.QApplication(sys.argv)

    screen1 = Screen1()
    screen1.show()

    screen2 = Screen2()
    pollingScreen = PollingScreen()
    dataCollectionScreen = DataCollectionScreen()

    screen1.pushButton.clicked.connect(lambda: changeWindow(screen1, screen2))
    screen1.pushButton_2.clicked.connect(lambda: changeWindow(screen1, dataCollectionScreen))
    screen2.pushButton_2.clicked.connect(lambda: changeWindow(screen2, pollingScreen))
    screen2.commandLinkButton.clicked.connect(lambda: changeWindow(screen2, screen1))
    pollingScreen.commandLinkButton.clicked.connect(lambda: changeWindow(pollingScreen, screen2))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
