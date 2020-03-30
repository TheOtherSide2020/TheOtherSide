# class for second Screens :
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# class for pollingScreen UI
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


# Polling Screen Functionality
class PollingScreen(object):

    def is_file_empty(self, file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    def readFromJsonFile(self):
        is_empty = self.is_file_empty('../Json/PollingSystemRecords.txt')
        if not is_empty:
            with open('../Json/PollingSystemRecords.txt', 'r') as json_file:
                data = json.load(json_file)
                for p in data['PollingSystemRecord']:
                    self.listWidget.addItem(p['Question'])

    def appendToJsonFile(self, PollingSystemRecord):
        try:
            with open('../Json/PollingSystemRecords.txt') as json_file:
                data = json.load(json_file)
                data['PollingSystemRecord'].append(PollingSystemRecord)

            with open('../Json/PollingSystemRecords.txt', 'w') as json_file:
                json.dump(data, json_file)
        except FileNotFoundError as exc:
            pass

    # append the field to the json file
    # append this entry to content list

    def save(self):
        # check if string is empty
        if self.Question.toPlainText() != " " and self.Option1.toPlainText() != " " and self.Option2.toPlainText() != "" and self.Option3.toPlainText() != " " and self.Option4.toPlainText() != " ":

            if self.listWidget.count() == 0:
                PollingSystemRecord = {
                    "PollingSystemRecord": [{
                        "Question": self.Question.toPlainText(),
                        "Option1": self.Option1.toPlainText(),
                        "Option2": self.Option2.toPlainText(),
                        "Option3": self.Option3.toPlainText(),
                        "Option4": self.Option4.toPlainText()
                    }]
                }

                with open('../Json/PollingSystemRecords.txt', 'w') as json_file:
                    json.dump(PollingSystemRecord, json_file)

                self.listWidget.addItem(self.Question.toPlainText())

            # check if this list item has already been added:  remove duplicates
            else:
                items = self.listWidget.findItems(self.Question.toPlainText(), Qt.MatchFixedString)

                if items.__len__() == 0:
                    PollingSystemRecord = {

                        "Question": self.Question.toPlainText(),
                        "Option1": self.Option1.toPlainText(),
                        "Option2": self.Option2.toPlainText(),
                        "Option3": self.Option3.toPlainText(),
                        "Option4": self.Option4.toPlainText()

                    }
                    # append this entry to json file
                    self.appendToJsonFile(PollingSystemRecord)
                    self.listWidget.addItem(self.Question.toPlainText())

                else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("The Question   " + self.Question.toPlainText() + "already exists")
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
        MainWindow.resize(1403, 855)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 0, 1131, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Images/PollingScreen.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setIndent(21)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.Question = QtWidgets.QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(970, 200, 331, 41))
        self.Question.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Question.setTabChangesFocus(True)
        self.Question.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Question.setObjectName("Question")
        self.Option1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option1.setGeometry(QtCore.QRect(650, 460, 131, 31))
        self.Option1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option1.setTabChangesFocus(True)
        self.Option1.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option1.setObjectName("Option1")
        self.Option2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option2.setGeometry(QtCore.QRect(770, 700, 171, 31))
        self.Option2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option2.setTabChangesFocus(True)
        self.Option2.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option2.setObjectName("Option2")
        self.Option3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option3.setGeometry(QtCore.QRect(1210, 600, 131, 31))
        self.Option3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option3.setTabChangesFocus(True)
        self.Option3.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option3.setObjectName("Option3")
        self.Option4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Option4.setGeometry(QtCore.QRect(310, 520, 171, 31))
        self.Option4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Option4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Option4.setTabChangesFocus(True)
        self.Option4.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.Option4.setObjectName("Option4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1234, 32, 101, 31))
        self.pushButton.setObjectName("saveButton")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 40, 281, 851))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.isSortingEnabled()
        # this function reads the previous records in the json file
        self.readFromJsonFile()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.populateTextForEdit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def populateTextForEdit(self):
        text = self.listWidget.currentItem().text()
        self.Question.setPlainText(text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.Question.setPlaceholderText(_translate("MainWindow", "Question"))
        self.Option1.setPlaceholderText(_translate("MainWindow", "Option1"))
        self.Option2.setPlaceholderText(_translate("MainWindow", "Option2"))
        self.Option3.setPlaceholderText(_translate("MainWindow", "Option3"))
        self.Option4.setPlaceholderText(_translate("MainWindow", "Option4"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton.clicked.connect(self.save)
        self.label_2.setText(_translate("MainWindow", "Content List"))


# class for Second Screen, This Screen presents the option to choose between templates, Polling, conversational,
# Showcase
class Screen2(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = PollingScreen()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 849)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.pushButton.setText(_translate("MainWindow", "ShowCase"))
        self.pushButton_2.setText(_translate("MainWindow", "Polling System"))
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_3.setText(_translate("MainWindow", "Conversation"))
        self.label.setText(_translate("MainWindow", "Select Your Template"))


# class for first Screen, This Screen presents the option to choose the content editor or the data collection editor
class Screen1(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Screen2()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 851)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ScreenUI\\../Images/glassWall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2.setText(_translate("MainWindow", "Data Collection"))


# class for the Data collection Screen UI
class DataCollectionScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1223, 851)
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Screen1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
