# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yusuk/DAIKICHI/MIIL/MIIL_DETECTION_A_GUI.ui',
# licensing of 'C:/Users/yusuk/DAIKICHI/MIIL/MIIL_DETECTION_A_GUI.ui' applies.
#
# Created: Sat Feb 22 17:38:30 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 473)
        MainWindow.setMinimumSize(QtCore.QSize(782, 473))
        MainWindow.setMaximumSize(QtCore.QSize(782, 473))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(10, 10, 211, 61))
        self.groupBox1.setObjectName("groupBox1")
        self.pushButton1 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton1.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton2.setEnabled(False)
        self.pushButton2.setGeometry(QtCore.QRect(110, 20, 93, 28))
        self.pushButton2.setObjectName("pushButton2")
        self.groupBox4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox4.setGeometry(QtCore.QRect(230, 80, 91, 61))
        self.groupBox4.setObjectName("groupBox4")
        self.comboBox1 = QtWidgets.QComboBox(self.groupBox4)
        self.comboBox1.setGeometry(QtCore.QRect(10, 20, 71, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.groupBox9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox9.setGeometry(QtCore.QRect(10, 220, 761, 61))
        self.groupBox9.setObjectName("groupBox9")
        self.lineEdit4 = QtWidgets.QLineEdit(self.groupBox9)
        self.lineEdit4.setEnabled(False)
        self.lineEdit4.setGeometry(QtCore.QRect(10, 20, 641, 20))
        self.lineEdit4.setObjectName("lineEdit4")
        self.pushButton6 = QtWidgets.QPushButton(self.groupBox9)
        self.pushButton6.setGeometry(QtCore.QRect(660, 20, 93, 28))
        self.pushButton6.setObjectName("pushButton6")
        self.groupBox10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox10.setGeometry(QtCore.QRect(10, 290, 761, 61))
        self.groupBox10.setObjectName("groupBox10")
        self.lineEdit5 = QtWidgets.QLineEdit(self.groupBox10)
        self.lineEdit5.setEnabled(False)
        self.lineEdit5.setGeometry(QtCore.QRect(10, 20, 641, 20))
        self.lineEdit5.setObjectName("lineEdit5")
        self.pushButton7 = QtWidgets.QPushButton(self.groupBox10)
        self.pushButton7.setGeometry(QtCore.QRect(660, 20, 93, 28))
        self.pushButton7.setObjectName("pushButton7")
        self.groupBox3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox3.setGeometry(QtCore.QRect(10, 80, 211, 61))
        self.groupBox3.setObjectName("groupBox3")
        self.pushButton4 = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton4.setGeometry(QtCore.QRect(110, 20, 93, 28))
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton3 = QtWidgets.QPushButton(self.groupBox3)
        self.pushButton3.setEnabled(True)
        self.pushButton3.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.pushButton3.setObjectName("pushButton3")
        self.groupBox8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox8.setGeometry(QtCore.QRect(10, 150, 761, 61))
        self.groupBox8.setObjectName("groupBox8")
        self.lineEdit3 = QtWidgets.QLineEdit(self.groupBox8)
        self.lineEdit3.setEnabled(False)
        self.lineEdit3.setGeometry(QtCore.QRect(10, 20, 641, 20))
        self.lineEdit3.setObjectName("lineEdit3")
        self.pushButton5 = QtWidgets.QPushButton(self.groupBox8)
        self.pushButton5.setGeometry(QtCore.QRect(660, 20, 93, 28))
        self.pushButton5.setObjectName("pushButton5")
        self.groupBox5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox5.setGeometry(QtCore.QRect(330, 80, 101, 61))
        self.groupBox5.setObjectName("groupBox5")
        self.comboBox2 = QtWidgets.QComboBox(self.groupBox5)
        self.comboBox2.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.comboBox2.setObjectName("comboBox2")
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox2.setGeometry(QtCore.QRect(230, 10, 541, 61))
        self.groupBox2.setObjectName("groupBox2")
        self.lineEdit1 = QtWidgets.QLineEdit(self.groupBox2)
        self.lineEdit1.setEnabled(True)
        self.lineEdit1.setGeometry(QtCore.QRect(260, 20, 71, 20))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.groupBox2)
        self.lineEdit2.setEnabled(True)
        self.lineEdit2.setGeometry(QtCore.QRect(360, 20, 71, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label1 = QtWidgets.QLabel(self.groupBox2)
        self.label1.setGeometry(QtCore.QRect(30, 20, 16, 20))
        self.label1.setObjectName("label1")
        self.label_2 = QtWidgets.QLabel(self.groupBox2)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 16, 20))
        self.label_2.setObjectName("label_2")
        self.checkBox1 = QtWidgets.QCheckBox(self.groupBox2)
        self.checkBox1.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.checkBox1.setText("")
        self.checkBox1.setAutoExclusive(True)
        self.checkBox1.setObjectName("checkBox1")
        self.pushButton8 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton8.setGeometry(QtCore.QRect(440, 20, 93, 28))
        self.pushButton8.setObjectName("pushButton8")
        self.label_3 = QtWidgets.QLabel(self.groupBox2)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 16, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit6 = QtWidgets.QLineEdit(self.groupBox2)
        self.lineEdit6.setEnabled(False)
        self.lineEdit6.setGeometry(QtCore.QRect(50, 20, 71, 20))
        self.lineEdit6.setObjectName("lineEdit6")
        self.label_4 = QtWidgets.QLabel(self.groupBox2)
        self.label_4.setGeometry(QtCore.QRect(340, 20, 16, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit7 = QtWidgets.QLineEdit(self.groupBox2)
        self.lineEdit7.setEnabled(False)
        self.lineEdit7.setGeometry(QtCore.QRect(150, 20, 71, 20))
        self.lineEdit7.setObjectName("lineEdit7")
        self.groupBox6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox6.setGeometry(QtCore.QRect(590, 80, 111, 61))
        self.groupBox6.setObjectName("groupBox6")
        self.comboBox3 = QtWidgets.QComboBox(self.groupBox6)
        self.comboBox3.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.comboBox3.setObjectName("comboBox3")
        self.groupBox7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox7.setGeometry(QtCore.QRect(710, 80, 61, 61))
        self.groupBox7.setObjectName("groupBox7")
        self.checkBox2 = QtWidgets.QCheckBox(self.groupBox7)
        self.checkBox2.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.checkBox2.setObjectName("checkBox2")
        self.groupBox11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox11.setGeometry(QtCore.QRect(10, 360, 761, 61))
        self.groupBox11.setObjectName("groupBox11")
        self.lineEdit8 = QtWidgets.QLineEdit(self.groupBox11)
        self.lineEdit8.setEnabled(False)
        self.lineEdit8.setGeometry(QtCore.QRect(10, 20, 641, 20))
        self.lineEdit8.setObjectName("lineEdit8")
        self.pushButton9 = QtWidgets.QPushButton(self.groupBox11)
        self.pushButton9.setGeometry(QtCore.QRect(660, 20, 93, 28))
        self.pushButton9.setObjectName("pushButton9")
        self.groupBox13 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox13.setGeometry(QtCore.QRect(440, 80, 141, 61))
        self.groupBox13.setObjectName("groupBox13")
        self.comboBox4 = QtWidgets.QComboBox(self.groupBox13)
        self.comboBox4.setGeometry(QtCore.QRect(50, 20, 81, 21))
        self.comboBox4.setObjectName("comboBox4")
        self.checkBox3 = QtWidgets.QCheckBox(self.groupBox13)
        self.checkBox3.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.checkBox3.setObjectName("checkBox3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MIIL DETECTION A", None, -1))
        self.groupBox1.setTitle(QtWidgets.QApplication.translate("MainWindow", "MODE", None, -1))
        self.pushButton1.setText(QtWidgets.QApplication.translate("MainWindow", "START", None, -1))
        self.pushButton2.setText(QtWidgets.QApplication.translate("MainWindow", "STOP", None, -1))
        self.groupBox4.setTitle(QtWidgets.QApplication.translate("MainWindow", "THRESHOLD", None, -1))
        self.groupBox9.setTitle(QtWidgets.QApplication.translate("MainWindow", "MODEL FILE", None, -1))
        self.pushButton6.setText(QtWidgets.QApplication.translate("MainWindow", "OPEN", None, -1))
        self.groupBox10.setTitle(QtWidgets.QApplication.translate("MainWindow", "WEIGHT FILE", None, -1))
        self.pushButton7.setText(QtWidgets.QApplication.translate("MainWindow", "OPEN", None, -1))
        self.groupBox3.setTitle(QtWidgets.QApplication.translate("MainWindow", "SETTING", None, -1))
        self.pushButton4.setText(QtWidgets.QApplication.translate("MainWindow", "SAVE STATE", None, -1))
        self.pushButton3.setText(QtWidgets.QApplication.translate("MainWindow", "LOAD STATE", None, -1))
        self.groupBox8.setTitle(QtWidgets.QApplication.translate("MainWindow", "PARAMETER FILE", None, -1))
        self.pushButton5.setText(QtWidgets.QApplication.translate("MainWindow", "OPEN", None, -1))
        self.groupBox5.setTitle(QtWidgets.QApplication.translate("MainWindow", "VIDEO SIZE", None, -1))
        self.groupBox2.setTitle(QtWidgets.QApplication.translate("MainWindow", "TRIM", None, -1))
        self.label1.setText(QtWidgets.QApplication.translate("MainWindow", "X :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Y :", None, -1))
        self.pushButton8.setText(QtWidgets.QApplication.translate("MainWindow", "CLEAR", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "W :", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "H :", None, -1))
        self.groupBox6.setTitle(QtWidgets.QApplication.translate("MainWindow", "CAMERA ", None, -1))
        self.groupBox7.setTitle(QtWidgets.QApplication.translate("MainWindow", "REC", None, -1))
        self.checkBox2.setText(QtWidgets.QApplication.translate("MainWindow", "ON", None, -1))
        self.groupBox11.setTitle(QtWidgets.QApplication.translate("MainWindow", "REC FILE", None, -1))
        self.pushButton9.setText(QtWidgets.QApplication.translate("MainWindow", "OPEN", None, -1))
        self.groupBox13.setTitle(QtWidgets.QApplication.translate("MainWindow", "RESIZE", None, -1))
        self.checkBox3.setText(QtWidgets.QApplication.translate("MainWindow", "ON", None, -1))

