from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 636)
        font = QFont('Microsoft Yahei', 12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(320, 0, 284, 61))
        # self.label.setFont(font)
        # self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        # self.label.setMouseTracking(False)
        # self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        # self.label.setToolTipDuration(3)
        # self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.label.setLineWidth(100)
        # self.label.setMidLineWidth(100)
        # self.label.setScaledContents(False)
        # self.label.setWordWrap(False)
        # self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(23)
        self.hboxlayout.setObjectName("hboxlayout")
        self.nameList = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.nameList.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameList.sizePolicy().hasHeightForWidth())
        self.nameList.setSizePolicy(sizePolicy)
        self.nameList.setFont(font)
        self.nameList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nameList.setObjectName("nameList")
        self.hboxlayout.addWidget(self.nameList)
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.addButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addButton.setCheckable(True)
        self.addButton.setChecked(True)
        self.addButton.setAutoRepeat(True)
        self.addButton.setAutoExclusive(True)
        self.addButton.setObjectName("addButton")
        self.hboxlayout.addWidget(self.addButton)
        self.reduceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reduceButton.sizePolicy().hasHeightForWidth())
        self.reduceButton.setSizePolicy(sizePolicy)
        self.reduceButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.reduceButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.reduceButton.setCheckable(True)
        self.reduceButton.setChecked(True)
        self.reduceButton.setAutoRepeat(True)
        self.reduceButton.setAutoExclusive(True)
        self.reduceButton.setObjectName("reduceButton")
        self.hboxlayout.addWidget(self.reduceButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 120, 1420, 820))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-50, -50, 300, 350))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_2 = QWebEngineView(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(-100, 0, 300, 400))
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)
        self.table_label = QWebEngineView(self.centralwidget)
        self.table_label.setGeometry(QtCore.QRect(30, 120, 435, 820))
        self.table_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_label.setStyleSheet("overflow: auto;")
        self.table_label.setObjectName("table_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "职业体验日课堂分数排名"))
        # self.label.setText(_translate("MainWindow", "实时控分系统"))
        self.addButton.setText(_translate("MainWindow", "加分"))
        self.reduceButton.setText(_translate("MainWindow", "减分"))
        # self.bar_chart_label.setAcceptRichText(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
