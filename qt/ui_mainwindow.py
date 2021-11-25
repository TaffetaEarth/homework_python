# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 418)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(450, 10, 89, 25))
        self.counter = QLabel(self.centralwidget)
        self.counter.setObjectName(u"counter")
        self.counter.setGeometry(QRect(10, 50, 531, 191))
        self.counter.setLayoutDirection(Qt.LeftToRight)
        self.counter.setAlignment(Qt.AlignCenter)
        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(10, 250, 261, 51))
        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(280, 250, 261, 51))
        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setGeometry(QRect(280, 310, 261, 51))
        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(10, 310, 261, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.counter.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u043e, \u0437\u0430\u0447\u0435\u043c \u0437\u0434\u0435\u0441\u044c \u044d\u0442\u0430 \u043a\u043d\u043e\u043f\u043a\u0430", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u043e, \u0437\u0430\u0447\u0435\u043c \u0437\u0434\u0435\u0441\u044c \u044d\u0442\u0430 \u043a\u043d\u043e\u043f\u043a\u0430", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u043e, \u0437\u0430\u0447\u0435\u043c \u0437\u0434\u0435\u0441\u044c \u044d\u0442\u0430 \u043a\u043d\u043e\u043f\u043a\u0430", None))
    # retranslateUi

