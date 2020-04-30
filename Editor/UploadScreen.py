import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, QUrl, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QStyle, QFileDialog, QMessageBox, QLabel, QVBoxLayout, QPushButton, QSlider, QHBoxLayout


# class for pollingScreen UI


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = os.path.dirname(sys.argv[0])
    except Exception:
        base_path = os.path.dirname(sys.argv[0])
    return os.path.join(base_path, relative_path)


class UploadScreen(QtWidgets.QMainWindow):
    VideoFileName = ""
    ImageFileName = ""
    Video = ""
    Image = ""

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

        self.loadVideo(UploadScreen.VideoFileName)

    def loadVideo(self, video):
        if video == '':
            self.videoWidget.hide()
            self.playButton.hide()
            self.positionSlider.hide()
            self.pushButton_5.hide()
            self.pushButton_2.show()
        else:
            url = QUrl.fromLocalFile(video)
            # set the file name as this in the previous screen
            if video.lower().endswith(('.mp3', '.avi', '.mp4', '.mov')):
                if video != '':
                    self.mediaPlayer.setMedia(
                        QMediaContent(QUrl.fromLocalFile(video)))
                    self.playButton.setEnabled(True)
                    self.videoWidget.show()
                    self.playButton.show()
                    self.positionSlider.show()
                    self.pushButton_2.hide()
                    self.pushButton_5.show()
                    UploadScreen.VideoFileName = video
                    UploadScreen.Video = url.fileName().upper()

            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Please upload a .mp3 or .avi or .mp4 or .mov file")
                msgBox.setWindowTitle("Error")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                x = msgBox.exec_()

    def openImageFile(self):

        UploadScreen.ImageFileName, _ = QFileDialog.getOpenFileName(self, "Open Image",
                                                                    QDir.homePath())

        self.loadImage(UploadScreen.ImageFileName)

    def loadImage(self, image):
        if image == '':
            self.imageWidget.hide()
            self.pushButton_4.hide()
            UploadScreen.ImageFileName = ' '
            UploadScreen.Image = ' '

        else:
            url = QUrl.fromLocalFile(image)

            if image.lower().endswith(('.png', '.jpg', '.jpeg')):

                if image != '':
                    self.pixmap = QPixmap(image)
                    self.imageWidget.setPixmap(self.pixmap)
                    self.imageWidget.show()
                    self.pushButton_4.show()
                    UploadScreen.ImageFileName = image
                    UploadScreen.Image = url.fileName().upper()

            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Please upload an .png, .jpeg or .jpg Image file")
                msgBox.setWindowTitle("Error")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                x = msgBox.exec_()

    def clearImage(self):
        self.imageWidget.hide()
        self.pushButton_4.hide()
        UploadScreen.Image = ""
        UploadScreen.ImageFileName = ""
        self.imageWidget.update()

    def clearVideo(self):
        self.videoWidget.hide()
        self.pushButton_2.show()
        self.positionSlider.hide()
        self.playButton.hide()
        self.pushButton_5.hide()
        UploadScreen.Video = ""
        UploadScreen.VideoFileName = ""
        self.videoWidget.update()

    def closeUploadScreen(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1085, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(59, 140, 451, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(184, 200, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Images/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 30))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(560, 139, 461, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setAutoFillBackground(True)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 200, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 40))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 100, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 100, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 610, 871, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 120, 51, 51))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("Images/Delete_upload window.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1015, 120, 41, 41))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-20, 0, 1101, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color:white;\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 1091, 701))
        self.label_5.setPixmap(QtGui.QPixmap(resource_path("Images/upload_window_bg.png")))
        self.label_5.setStyleSheet("background-color:white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 10, 48, 48))
        self.commandLinkButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("Images/back.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 130, 471, 451))
        self.label_6.setStyleSheet(" margin:5px; border:2px solid  rgb(193, 193, 193); border-style:dashed;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 130, 481, 451))
        self.label_7.setStyleSheet(" margin:5px; border:2px solid  rgb(193, 193, 193); border-style:dashed;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 680, 141, 41))
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("Images/Upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 120))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.imageWidget = QLabel(self)
        self.imageWidget.setScaledContents(True)
        self.imageWidget.hide()
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        layout = QVBoxLayout()
        layout.addWidget(self.imageWidget)

        self.widget.setLayout(layout)

        self.videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setStyleSheet("border:none")
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setStyleSheet("border:none")
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)

        self.widget_2.setLayout(layout)

        self.pushButton_4.setStyleSheet("border: 2px solid none; border-radius:5px;")
        self.pushButton_5.setStyleSheet("border: 2px solid none; border-radius:5px;")

        self.label_5.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.widget.raise_()
        self.pushButton_4.raise_()
        self.widget_2.raise_()
        self.pushButton_5.raise_()
        self.label_3.raise_()
        self.label.raise_()

        self.commandLinkButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Other Side"))
        self.pushButton.clicked.connect(self.openImageFile)
        self.pushButton_2.clicked.connect(self.openFile)

        self.label.setText(_translate("MainWindow", "Upload an image"))

        self.label_2.setText(_translate("MainWindow", "Upload a video (optional)"))

        self.label_3.setText(_translate("MainWindow",
                                        "You can upload either video or image, or both of them image will be the "
                                        "cover for idle status."))



        self.pushButton_4.hide()
        self.commandLinkButton.clicked.connect(self.closeUploadScreen)
        self.pushButton_5.hide()
        self.pushButton_5.clicked.connect(self.clearVideo)
        self.pushButton_4.clicked.connect(self.clearImage)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
