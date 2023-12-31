# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reg_regbutton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.reg_regbutton_2.setGeometry(QtCore.QRect(350, 340, 75, 23))
        self.reg_regbutton_2.setObjectName("reg_regbutton_2")
        self.reg_email_line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_email_line_2.setGeometry(QtCore.QRect(300, 260, 151, 20))
        self.reg_email_line_2.setObjectName("reg_email_line_2")
        self.reg_passline_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_passline_2.setGeometry(QtCore.QRect(300, 280, 151, 20))
        self.reg_passline_2.setObjectName("reg_passline_2")
        self.reg_logine_line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_logine_line_2.setGeometry(QtCore.QRect(300, 240, 151, 20))
        self.reg_logine_line_2.setObjectName("reg_logine_line_2")
        self.reg_cancelbutton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.reg_cancelbutton_2.setGeometry(QtCore.QRect(230, 340, 75, 23))
        self.reg_cancelbutton_2.setObjectName("reg_cancelbutton_2")
        self.reg_email_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.reg_email_label_2.setGeometry(QtCore.QRect(210, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_email_label_2.setFont(font)
        self.reg_email_label_2.setObjectName("reg_email_label_2")
        self.reg_confirm_line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.reg_confirm_line_2.setGeometry(QtCore.QRect(300, 300, 151, 20))
        self.reg_confirm_line_2.setObjectName("reg_confirm_line_2")
        self.reg_login_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.reg_login_label_2.setGeometry(QtCore.QRect(210, 240, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_login_label_2.setFont(font)
        self.reg_login_label_2.setObjectName("reg_login_label_2")
        self.password_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.password_label_4.setGeometry(QtCore.QRect(210, 300, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label_4.setFont(font)
        self.password_label_4.setObjectName("password_label_4")
        self.reg_pass_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.reg_pass_label_2.setGeometry(QtCore.QRect(210, 280, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_pass_label_2.setFont(font)
        self.reg_pass_label_2.setObjectName("reg_pass_label_2")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)
        self.reg_regbutton_2.clicked.connect(self.register_clicked)
        self.reg_cancelbutton_2.clicked.connect(self.exit)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.reg_regbutton_2.setText(_translate("RegisterWindow", "Register!"))
        self.reg_email_line_2.setText(_translate("RegisterWindow", "e-mail"))
        self.reg_passline_2.setText(_translate("RegisterWindow", "password"))
        self.reg_logine_line_2.setText(_translate("RegisterWindow", "login"))
        self.reg_cancelbutton_2.setText(_translate("RegisterWindow", "Cancel"))
        self.reg_email_label_2.setText(_translate("RegisterWindow", "E-mail"))
        self.reg_confirm_line_2.setText(_translate("RegisterWindow", "password"))
        self.reg_login_label_2.setText(_translate("RegisterWindow", "Login:"))
        self.password_label_4.setText(_translate("RegisterWindow", "Password:"))
        self.reg_pass_label_2.setText(_translate("RegisterWindow", "Password:"))

    def register_clicked(self):
        register_url = 'http://127.0.0.1:8000/users/register_gui/'
        username = self.reg_logine_line_2.text()
        email = self.reg_email_line_2.text()
        password1 = self.reg_passline_2.text()
        password2 = self.reg_confirm_line_2.text()
        data = {
            'username': username,
            'email' : email,
            'password1': password1,
            'password2': password2
        }
        response = requests.post(register_url, data=data)
        if response.status_code == 201:
            QMessageBox.information(self.centralwidget.window(), "Registration Failure", "Registration successful!")
        elif response.status_code == 400:
            error_data = response.json()
            QMessageBox.information(self.centralwidget.window(), "Registration Success", f"Errors: {error_data}")
        else:
            print("Error")

    def exit(self):
        self.centralwidget.window().close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())