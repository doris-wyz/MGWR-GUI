# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-no-prediction-pc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 563)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(764, 618))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(289, 0, 191, 391))
        self.groupBox_2.setObjectName("groupBox_2")
        self.variableList = QtWidgets.QListWidget(self.groupBox_2)
        self.variableList.setGeometry(QtCore.QRect(10, 20, 171, 361))
        self.variableList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.variableList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variableList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.variableList.setDragEnabled(False)
        self.variableList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.variableList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.variableList.setResizeMode(QtWidgets.QListView.Fixed)
        self.variableList.setObjectName("variableList")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(490, 0, 261, 391))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_6)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 241, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addOffset = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.addOffset.setMinimumSize(QtCore.QSize(25, 20))
        self.addOffset.setObjectName("addOffset")
        self.gridLayout.addWidget(self.addOffset, 1, 1, 1, 1)
        self.removeOffset = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.removeOffset.setMinimumSize(QtCore.QSize(25, 20))
        self.removeOffset.setObjectName("removeOffset")
        self.gridLayout.addWidget(self.removeOffset, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.OffsetLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.OffsetLabel.setEnabled(False)
        self.OffsetLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.OffsetLabel.setObjectName("OffsetLabel")
        self.gridLayout.addWidget(self.OffsetLabel, 1, 3, 1, 1)
        self.responseLabel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.responseLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.responseLabel.setReadOnly(True)
        self.responseLabel.setObjectName("responseLabel")
        self.gridLayout.addWidget(self.responseLabel, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.addY = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.addY.setMinimumSize(QtCore.QSize(25, 20))
        self.addY.setObjectName("addY")
        self.gridLayout.addWidget(self.addY, 0, 1, 1, 1)
        self.removeY = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.removeY.setMinimumSize(QtCore.QSize(25, 20))
        self.removeY.setObjectName("removeY")
        self.gridLayout.addWidget(self.removeY, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setGeometry(QtCore.QRect(68, 85, 181, 296))
        self.groupBox_3.setObjectName("groupBox_3")
        self.localList = QtWidgets.QListWidget(self.groupBox_3)
        self.localList.setGeometry(QtCore.QRect(10, 20, 161, 266))
        self.localList.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.localList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.localList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.localList.setObjectName("localList")
        self.localList.raise_()
        self.gridLayoutWidget.raise_()
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_6)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(5, 225, 60, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.removeLocal = QtWidgets.QToolButton(self.horizontalLayoutWidget_5)
        self.removeLocal.setMinimumSize(QtCore.QSize(25, 20))
        self.removeLocal.setObjectName("removeLocal")
        self.horizontalLayout_5.addWidget(self.removeLocal)
        self.addLocal = QtWidgets.QToolButton(self.horizontalLayoutWidget_5)
        self.addLocal.setMinimumSize(QtCore.QSize(25, 20))
        self.addLocal.setObjectName("addLocal")
        self.horizontalLayout_5.addWidget(self.addLocal)
        self.groupBox_7 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 205, 271, 46))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 256, 19))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.isMGWRRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.isMGWRRBTN.setChecked(True)
        self.isMGWRRBTN.setObjectName("isMGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isMGWRRBTN)
        self.isGWRRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.isGWRRBTN.setEnabled(True)
        self.isGWRRBTN.setCheckable(True)
        self.isGWRRBTN.setChecked(False)
        self.isGWRRBTN.setObjectName("isGWRRBTN")
        self.horizontalLayout_2.addWidget(self.isGWRRBTN)
        self.kernelDropdownGrou = QtWidgets.QGroupBox(Dialog)
        self.kernelDropdownGrou.setGeometry(QtCore.QRect(10, 255, 271, 51))
        self.kernelDropdownGrou.setObjectName("kernelDropdownGrou")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.kernelDropdownGrou)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 15, 256, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fixedBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.fixedBox.setMinimumSize(QtCore.QSize(0, 22))
        self.fixedBox.setObjectName("fixedBox")
        self.fixedBox.addItem("")
        self.fixedBox.addItem("")
        self.horizontalLayout_3.addWidget(self.fixedBox)
        self.shapeBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.shapeBox.setMinimumSize(QtCore.QSize(0, 22))
        self.shapeBox.setObjectName("shapeBox")
        self.shapeBox.addItem("")
        self.shapeBox.addItem("")
        self.shapeBox.addItem("")
        self.horizontalLayout_3.addWidget(self.shapeBox)
        self.groupBox_9 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 310, 271, 161))
        self.groupBox_9.setObjectName("groupBox_9")
        self.bwDropdown = QtWidgets.QComboBox(self.groupBox_9)
        self.bwDropdown.setGeometry(QtCore.QRect(10, 15, 256, 22))
        self.bwDropdown.setMinimumSize(QtCore.QSize(0, 22))
        self.bwDropdown.setObjectName("bwDropdown")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.bwDropdown.addItem("")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_9)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 236, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.bwPreDefined = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwPreDefined.setEnabled(False)
        self.bwPreDefined.setObjectName("bwPreDefined")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bwPreDefined)
        self.bwMin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwMin.setEnabled(False)
        self.bwMin.setObjectName("bwMin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bwMin)
        self.bwMax = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwMax.setEnabled(False)
        self.bwMax.setObjectName("bwMax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bwMax)
        self.bwInterval = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bwInterval.setEnabled(False)
        self.bwInterval.setObjectName("bwInterval")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bwInterval)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 50, 271, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 125, 256, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.isPrjCoorRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.isPrjCoorRBTN.setChecked(True)
        self.isPrjCoorRBTN.setObjectName("isPrjCoorRBTN")
        self.horizontalLayout.addWidget(self.isPrjCoorRBTN)
        self.isSphCoorRBTN = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.isSphCoorRBTN.setObjectName("isSphCoorRBTN")
        self.horizontalLayout.addWidget(self.isSphCoorRBTN)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 256, 101))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.removeYCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeYCoor.setMinimumSize(QtCore.QSize(25, 20))
        self.removeYCoor.setObjectName("removeYCoor")
        self.gridLayout_4.addWidget(self.removeYCoor, 2, 3, 1, 1)
        self.addID = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addID.setMinimumSize(QtCore.QSize(25, 20))
        self.addID.setObjectName("addID")
        self.gridLayout_4.addWidget(self.addID, 0, 2, 1, 1)
        self.label_Y = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_Y.setObjectName("label_Y")
        self.gridLayout_4.addWidget(self.label_Y, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.idLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.idLabel.setText("")
        self.idLabel.setDragEnabled(True)
        self.idLabel.setReadOnly(True)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout_4.addWidget(self.idLabel, 0, 1, 1, 1)
        self.label_X = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_X.setObjectName("label_X")
        self.gridLayout_4.addWidget(self.label_X, 1, 0, 1, 1)
        self.yCoorLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.yCoorLabel.setReadOnly(True)
        self.yCoorLabel.setObjectName("yCoorLabel")
        self.gridLayout_4.addWidget(self.yCoorLabel, 2, 1, 1, 1)
        self.addXCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addXCoor.setMinimumSize(QtCore.QSize(25, 20))
        self.addXCoor.setObjectName("addXCoor")
        self.gridLayout_4.addWidget(self.addXCoor, 1, 2, 1, 1)
        self.removeXCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeXCoor.setMinimumSize(QtCore.QSize(25, 20))
        self.removeXCoor.setObjectName("removeXCoor")
        self.gridLayout_4.addWidget(self.removeXCoor, 1, 3, 1, 1)
        self.addYCoor = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.addYCoor.setMinimumSize(QtCore.QSize(25, 20))
        self.addYCoor.setObjectName("addYCoor")
        self.gridLayout_4.addWidget(self.addYCoor, 2, 2, 1, 1)
        self.xCoorLabel = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.xCoorLabel.setReadOnly(True)
        self.xCoorLabel.setObjectName("xCoorLabel")
        self.gridLayout_4.addWidget(self.xCoorLabel, 1, 1, 1, 1)
        self.removeID = QtWidgets.QToolButton(self.gridLayoutWidget_4)
        self.removeID.setMinimumSize(QtCore.QSize(25, 20))
        self.removeID.setObjectName("removeID")
        self.gridLayout_4.addWidget(self.removeID, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 271, 51))
        self.groupBox.setObjectName("groupBox")
        self.openDataBTN = QtWidgets.QToolButton(self.groupBox)
        self.openDataBTN.setGeometry(QtCore.QRect(240, 20, 28, 22))
        self.openDataBTN.setMinimumSize(QtCore.QSize(28, 22))
        self.openDataBTN.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.openDataBTN.setObjectName("openDataBTN")
        self.openDataPath = QtWidgets.QLineEdit(self.groupBox)
        self.openDataPath.setGeometry(QtCore.QRect(11, 21, 221, 21))
        self.openDataPath.setObjectName("openDataPath")
        self.groupBox_10 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_10.setGeometry(QtCore.QRect(290, 390, 461, 81))
        self.groupBox_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_10)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 381, 46))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_11 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_11.setObjectName("groupBox_11")
        self.optimCriDropdown = QtWidgets.QComboBox(self.groupBox_11)
        self.optimCriDropdown.setGeometry(QtCore.QRect(10, 15, 161, 22))
        self.optimCriDropdown.setMinimumSize(QtCore.QSize(0, 22))
        self.optimCriDropdown.setObjectName("optimCriDropdown")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.optimCriDropdown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_11, 0, 2, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_12.setObjectName("groupBox_12")
        self.modelTypeDropdown = QtWidgets.QComboBox(self.groupBox_12)
        self.modelTypeDropdown.setGeometry(QtCore.QRect(10, 15, 161, 22))
        self.modelTypeDropdown.setMinimumSize(QtCore.QSize(0, 22))
        self.modelTypeDropdown.setObjectName("modelTypeDropdown")
        self.modelTypeDropdown.addItem("")
        self.gridLayout_5.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.advancedBTN = QtWidgets.QToolButton(self.groupBox_10)
        self.advancedBTN.setGeometry(QtCore.QRect(400, 30, 56, 31))
        self.advancedBTN.setObjectName("advancedBTN")
        self.runBTN = QtWidgets.QPushButton(Dialog)
        self.runBTN.setGeometry(QtCore.QRect(615, 480, 121, 76))
        self.runBTN.setFocusPolicy(QtCore.Qt.NoFocus)
        self.runBTN.setObjectName("runBTN")
        self.groupBox_13 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 475, 571, 81))
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_13)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 20, 551, 54))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.saveBetasBTN = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.saveBetasBTN.setMinimumSize(QtCore.QSize(28, 22))
        self.saveBetasBTN.setObjectName("saveBetasBTN")
        self.gridLayout_2.addWidget(self.saveBetasBTN, 1, 2, 1, 1)
        self.saveSumBTN = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.saveSumBTN.setMinimumSize(QtCore.QSize(28, 22))
        self.saveSumBTN.setObjectName("saveSumBTN")
        self.gridLayout_2.addWidget(self.saveSumBTN, 0, 2, 1, 1)
        self.betaFileSavePath = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.betaFileSavePath.setObjectName("betaFileSavePath")
        self.gridLayout_2.addWidget(self.betaFileSavePath, 1, 1, 1, 1)
        self.sumFileSavePath = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.sumFileSavePath.setReadOnly(True)
        self.sumFileSavePath.setObjectName("sumFileSavePath")
        self.gridLayout_2.addWidget(self.sumFileSavePath, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.groupBox_2.raise_()
        self.groupBox_6.raise_()
        self.groupBox_7.raise_()
        self.kernelDropdownGrou.raise_()
        self.groupBox_9.raise_()
        self.groupBox_4.raise_()
        self.groupBox.raise_()
        self.groupBox_10.raise_()
        self.runBTN.raise_()
        self.groupBox_13.raise_()
        self.gridLayoutWidget.raise_()
        self.removeY.raise_()
        self.addY.raise_()
        self.label_4.raise_()
        self.responseLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MGWR"))
        self.groupBox_2.setTitle(_translate("Dialog", "Variable List"))
        self.groupBox_6.setTitle(_translate("Dialog", "Regression Variables"))
        self.addOffset.setText(_translate("Dialog", ">"))
        self.removeOffset.setText(_translate("Dialog", "<"))
        self.label_5.setText(_translate("Dialog", "Offset"))
        self.label_4.setText(_translate("Dialog", "Y"))
        self.addY.setText(_translate("Dialog", ">"))
        self.removeY.setText(_translate("Dialog", "<"))
        self.groupBox_3.setTitle(_translate("Dialog", "Local"))
        self.removeLocal.setText(_translate("Dialog", "<"))
        self.addLocal.setText(_translate("Dialog", ">"))
        self.groupBox_7.setTitle(_translate("Dialog", "GWR Mode"))
        self.isMGWRRBTN.setText(_translate("Dialog", "MGWR"))
        self.isGWRRBTN.setText(_translate("Dialog", "GWR"))
        self.kernelDropdownGrou.setTitle(_translate("Dialog", "Spatial Kernel"))
        self.fixedBox.setItemText(0, _translate("Dialog", "Adaptive"))
        self.fixedBox.setItemText(1, _translate("Dialog", "Fixed"))
        self.shapeBox.setItemText(0, _translate("Dialog", "Bisquare"))
        self.shapeBox.setItemText(1, _translate("Dialog", "Gaussian"))
        self.shapeBox.setItemText(2, _translate("Dialog", "Exponential"))
        self.groupBox_9.setTitle(_translate("Dialog", "Bandwidth Searching"))
        self.bwDropdown.setItemText(0, _translate("Dialog", "Golden Section"))
        self.bwDropdown.setItemText(1, _translate("Dialog", "Interval Search"))
        self.bwDropdown.setItemText(2, _translate("Dialog", "Pre-defiend bandwidth"))
        self.label_6.setText(_translate("Dialog", "Pre-defined"))
        self.label_9.setText(_translate("Dialog", "Min"))
        self.label_10.setText(_translate("Dialog", "Max"))
        self.label_11.setText(_translate("Dialog", "Interval"))
        self.groupBox_4.setTitle(_translate("Dialog", "Location Variables"))
        self.isPrjCoorRBTN.setText(_translate("Dialog", "Projected"))
        self.isSphCoorRBTN.setText(_translate("Dialog", "Spherical"))
        self.removeYCoor.setText(_translate("Dialog", ">"))
        self.addID.setText(_translate("Dialog", "<"))
        self.label_Y.setText(_translate("Dialog", "Y    "))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_X.setText(_translate("Dialog", "X    "))
        self.addXCoor.setText(_translate("Dialog", "<"))
        self.removeXCoor.setText(_translate("Dialog", ">"))
        self.addYCoor.setText(_translate("Dialog", "<"))
        self.removeID.setText(_translate("Dialog", ">"))
        self.groupBox.setTitle(_translate("Dialog", "Data Files"))
        self.openDataBTN.setText(_translate("Dialog", "..."))
        self.groupBox_10.setTitle(_translate("Dialog", "Model Options"))
        self.groupBox_11.setTitle(_translate("Dialog", "Optimization Criterion"))
        self.optimCriDropdown.setItemText(0, _translate("Dialog", "AICc"))
        self.optimCriDropdown.setItemText(1, _translate("Dialog", "AIC"))
        self.optimCriDropdown.setItemText(2, _translate("Dialog", "BIC"))
        self.optimCriDropdown.setItemText(3, _translate("Dialog", "CV"))
        self.groupBox_12.setTitle(_translate("Dialog", "Model Type"))
        self.modelTypeDropdown.setItemText(0, _translate("Dialog", "Gaussian"))
        self.advancedBTN.setText(_translate("Dialog", "Advanced"))
        self.runBTN.setText(_translate("Dialog", "Run"))
        self.groupBox_13.setTitle(_translate("Dialog", "Outputs"))
        self.saveBetasBTN.setText(_translate("Dialog", "..."))
        self.saveSumBTN.setText(_translate("Dialog", "..."))
        self.label_7.setText(_translate("Dialog", "Summary File"))
        self.label_8.setText(_translate("Dialog", "Parameter Estimates"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
