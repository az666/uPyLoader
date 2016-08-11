# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/qt\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout_3.addWidget(self.statusLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.portComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.portComboBox.setObjectName("portComboBox")
        self.horizontalLayout_3.addWidget(self.portComboBox)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/refresh-64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_3.addWidget(self.refreshButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.baudComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.baudComboBox.setObjectName("baudComboBox")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.baudComboBox)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_3.addWidget(self.connectButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.localPathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.localPathEdit.setObjectName("localPathEdit")
        self.horizontalLayout.addWidget(self.localPathEdit)
        self.saveLocalButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveLocalButton.setObjectName("saveLocalButton")
        self.horizontalLayout.addWidget(self.saveLocalButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filenameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout_2.addWidget(self.filenameEdit)
        self.saveMcuButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveMcuButton.setObjectName("saveMcuButton")
        self.horizontalLayout_2.addWidget(self.saveMcuButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeView = QtWidgets.QTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(250, 0))
        self.treeView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView.setBaseSize(QtCore.QSize(0, 0))
        self.treeView.setObjectName("treeView")
        self.codeEdit = QtWidgets.QTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.codeEdit.sizePolicy().hasHeightForWidth())
        self.codeEdit.setSizePolicy(sizePolicy)
        self.codeEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.codeEdit.setObjectName("codeEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMinimumSize(QtCore.QSize(150, 0))
        self.listView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.listButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listButton.sizePolicy().hasHeightForWidth())
        self.listButton.setSizePolicy(sizePolicy)
        self.listButton.setObjectName("listButton")
        self.verticalLayout.addWidget(self.listButton)
        self.executeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.executeButton.setObjectName("executeButton")
        self.verticalLayout.addWidget(self.executeButton)
        self.removeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNavigate = QtWidgets.QAction(MainWindow)
        self.actionNavigate.setObjectName("actionNavigate")
        self.actionTerminal = QtWidgets.QAction(MainWindow)
        self.actionTerminal.setObjectName("actionTerminal")
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.menuFile.addAction(self.actionNavigate)
        self.menuFile.addAction(self.actionUpload)
        self.menuView.addAction(self.actionTerminal)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.baudComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "uPyLoader"))
        self.label_3.setText(_translate("MainWindow", "Status:"))
        self.statusLabel.setText(_translate("MainWindow", "Disconnected"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label.setText(_translate("MainWindow", "Baud rate:"))
        self.baudComboBox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudComboBox.setItemText(1, _translate("MainWindow", "115200"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.label_4.setText(_translate("MainWindow", "Filename:"))
        self.saveLocalButton.setText(_translate("MainWindow", "Save Local"))
        self.saveMcuButton.setText(_translate("MainWindow", "Save to MCU"))
        self.listButton.setText(_translate("MainWindow", "List files"))
        self.executeButton.setText(_translate("MainWindow", "Execute"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionNavigate.setText(_translate("MainWindow", "Navigate"))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal"))
        self.actionUpload.setText(_translate("MainWindow", "Init transfer files"))
