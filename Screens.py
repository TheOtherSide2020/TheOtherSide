# Main Class for Backend Editor
# Has Instances of PollingScreen, Data Collection Screen, ShowCase Screen and Text Screen
# Ruchi_Hendre@2020
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Editor.DataCollectionScreen import DataCollectionScreen
from Editor.PollingScreen import PollingScreen
from Editor.Screen1 import Screen1
from Editor.Screen2 import Screen2
from Editor.ShowCaseScreen import ShowCaseScreen, UploadScreen


def changeWindow(w1, w2):
    w1.hide()
    w2.show()


def changeDataCollectionScreen(w1, w2, template):
    DataCollectionScreen.template = template
    DataCollectionScreen.count = 0
    w2.readFromJsonFile()
    w1.hide()
    w2.show()


def showWindow(w1):
    w1.loadImage()
    if ShowCaseScreen.VideoFileName != '':
     w1.loadVideo()
    w1.show()


def labelText(self, MainWindow, value):
    if MainWindow.Image == "":
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Image is needed")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        x = msgBox.exec_()

    else:
        self.label_3.setText(str(value))
        MainWindow.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("QTextBrowser { background-color: white; border-radius: "
                      "10px;}")
    screen1 = Screen1()
    screen1.show()

    screen2 = Screen2()
    screen2DataCollection = Screen2()
    pollingScreen = PollingScreen()
    DataCollectionScreen.template = "Polling"
    dataCollectionScreen = DataCollectionScreen()
    showCaseScreen = ShowCaseScreen()
    uploadScreen = UploadScreen()

    screen1.pushButton.clicked.connect(lambda: changeWindow(screen1, screen2))
    screen1.pushButton_2.clicked.connect(lambda: changeWindow(screen1, screen2DataCollection))
    screen2DataCollection.pushButton_2.clicked.connect(
        lambda: changeDataCollectionScreen(screen2DataCollection, dataCollectionScreen, "Polling"))
    screen2DataCollection.pushButton.clicked.connect(
        lambda: changeDataCollectionScreen(screen2DataCollection, dataCollectionScreen, "Showcase"))
    screen2.pushButton_2.clicked.connect(lambda: changeWindow(screen2, pollingScreen))
    screen2.pushButton.clicked.connect(lambda: changeWindow(screen2, showCaseScreen))
    screen2.commandLinkButton.clicked.connect(lambda: changeWindow(screen2, screen1))
    pollingScreen.commandLinkButton.clicked.connect(lambda: changeWindow(pollingScreen, screen2))
    showCaseScreen.pushButton_4.clicked.connect(lambda: showWindow(uploadScreen))

    uploadScreen.pushButton_3.clicked.connect(lambda: labelText(showCaseScreen, uploadScreen,
                                                                uploadScreen.Video + "  " + uploadScreen.Image + "uploaded"))

    dataCollectionScreen.commandLinkButton.clicked.connect(lambda: changeWindow(dataCollectionScreen, screen1))

    showCaseScreen.commandLinkButton.clicked.connect(lambda: changeWindow(showCaseScreen, screen2))
    uploadScreen.commandLinkButton.clicked.connect(lambda: changeWindow(uploadScreen, showCaseScreen))

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
