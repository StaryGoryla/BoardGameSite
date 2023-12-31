# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 90, 631, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.home_label = QtWidgets.QLabel(self.Home)
        self.home_label.setGeometry(QtCore.QRect(140, 70, 191, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.home_label.setFont(font)
        self.home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_label.setObjectName("home_label")
        self.status_label = QtWidgets.QLabel(self.Home)
        self.status_label.setGeometry(QtCore.QRect(400, 0, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.status_label.setFont(font)
        self.status_label.setWordWrap(True)
        self.status_label.setObjectName("status_label")
        self.stackedWidget.addWidget(self.Home)
        self.Game = QtWidgets.QWidget()
        self.Game.setObjectName("Game")
        self.game_label = QtWidgets.QLabel(self.Game)
        self.game_label.setGeometry(QtCore.QRect(110, 90, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.game_label.setFont(font)
        self.game_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_label.setObjectName("game_label")
        self.channel_line = QtWidgets.QLineEdit(self.Game)
        self.channel_line.setGeometry(QtCore.QRect(320, 340, 181, 31))
        self.channel_line.setObjectName("channel_line")
        self.channelbutton = QtWidgets.QPushButton(self.Game)
        self.channelbutton.setGeometry(QtCore.QRect(510, 340, 75, 41))
        self.channelbutton.setObjectName("channelbutton")
        self.stackedWidget.addWidget(self.Game)
        self.Profile = QtWidgets.QWidget()
        self.Profile.setObjectName("Profile")
        self.profile_label = QtWidgets.QLabel(self.Profile)
        self.profile_label.setGeometry(QtCore.QRect(110, 100, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.profile_label.setFont(font)
        self.profile_label.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_label.setObjectName("profile_label")
        self.stackedWidget.addWidget(self.Profile)
        self.Stats = QtWidgets.QWidget()
        self.Stats.setObjectName("Stats")
        self.stats_label = QtWidgets.QLabel(self.Stats)
        self.stats_label.setGeometry(QtCore.QRect(100, 100, 241, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stats_label.setFont(font)
        self.stats_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stats_label.setObjectName("stats_label")
        self.stackedWidget.addWidget(self.Stats)
        self.homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.homebutton.setGeometry(QtCore.QRect(230, 10, 75, 23))
        self.homebutton.setObjectName("homebutton")
        self.statsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.statsbutton.setGeometry(QtCore.QRect(310, 40, 75, 23))
        self.statsbutton.setObjectName("statsbutton")
        self.gamebutton = QtWidgets.QPushButton(self.centralwidget)
        self.gamebutton.setGeometry(QtCore.QRect(230, 40, 75, 23))
        self.gamebutton.setObjectName("gamebutton")
        self.profilebutton = QtWidgets.QPushButton(self.centralwidget)
        self.profilebutton.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.profilebutton.setObjectName("profilebutton")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(510, 40, 91, 31))
        self.logout_button.setObjectName("logout_button")
        self.login_box = QtWidgets.QGroupBox(self.centralwidget)
        self.login_box.setGeometry(QtCore.QRect(380, 0, 251, 111))
        self.login_box.setObjectName("login_box")
        self.loginbutton = QtWidgets.QPushButton(self.login_box)
        self.loginbutton.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.loginbutton.setObjectName("loginbutton")
        self.password_line = QtWidgets.QLineEdit(self.login_box)
        self.password_line.setGeometry(QtCore.QRect(100, 40, 151, 20))
        self.password_line.setObjectName("password_line")
        self.password_label = QtWidgets.QLabel(self.login_box)
        self.password_label.setGeometry(QtCore.QRect(10, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.login_label = QtWidgets.QLabel(self.login_box)
        self.login_label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.registerbutton = QtWidgets.QPushButton(self.login_box)
        self.registerbutton.setGeometry(QtCore.QRect(120, 60, 131, 23))
        self.registerbutton.setObjectName("registerbutton")
        self.login_line = QtWidgets.QLineEdit(self.login_box)
        self.login_line.setGeometry(QtCore.QRect(100, 20, 151, 20))
        self.login_line.setObjectName("login_line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_label.setText(_translate("MainWindow", "Home page"))
        self.status_label.setText(_translate("MainWindow", "The server seems to be offliine. Please check your connection or call me +48 720 802 418"))
        self.game_label.setText(_translate("MainWindow", "Game"))
        self.channel_line.setText(_translate("MainWindow", "What channel do you want to enter?"))
        self.channelbutton.setText(_translate("MainWindow", "Enter!"))
        self.profile_label.setText(_translate("MainWindow", "Profile"))
        self.stats_label.setText(_translate("MainWindow", "Stats"))
        self.homebutton.setText(_translate("MainWindow", "Home"))
        self.statsbutton.setText(_translate("MainWindow", "Stats"))
        self.gamebutton.setText(_translate("MainWindow", "Game"))
        self.profilebutton.setText(_translate("MainWindow", "Profile"))
        self.title_label.setText(_translate("MainWindow", "Wingspan"))
        self.logout_button.setText(_translate("MainWindow", "Log out!"))
        self.login_box.setTitle(_translate("MainWindow", "GroupBox"))
        self.loginbutton.setText(_translate("MainWindow", "Sign in!"))
        self.password_line.setText(_translate("MainWindow", "password"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.login_label.setText(_translate("MainWindow", "Login:"))
        self.registerbutton.setText(_translate("MainWindow", "No account yet? Sign up!"))
        self.login_line.setText(_translate("MainWindow", "login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
