# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sudokuwindow.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_Sudoku(object):
    def setupUi(self, Sudoku):
        if not Sudoku.objectName():
            Sudoku.setObjectName(u"Sudoku")
        Sudoku.resize(841, 705)
        self.centralwidget = QWidget(Sudoku)
        self.centralwidget.setObjectName(u"centralwidget")
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(740, 10, 89, 25))
        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(540, 50, 261, 51))
        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(540, 120, 261, 51))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 50, 41, 41))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(100, 50, 41, 41))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(200, 50, 41, 41))
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(150, 50, 41, 41))
        font = QFont()
        font.setFamilies([u"Z003"])
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_4.setFont(font)
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(400, 50, 41, 41))
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(300, 50, 41, 41))
        self.textEdit_7 = QTextEdit(self.centralwidget)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(350, 50, 41, 41))
        self.textEdit_8 = QTextEdit(self.centralwidget)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(250, 50, 41, 41))
        self.textEdit_9 = QTextEdit(self.centralwidget)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(450, 50, 41, 41))
        self.textEdit_10 = QTextEdit(self.centralwidget)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(200, 100, 41, 41))
        self.textEdit_11 = QTextEdit(self.centralwidget)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setGeometry(QRect(300, 100, 41, 41))
        self.textEdit_12 = QTextEdit(self.centralwidget)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(100, 100, 41, 41))
        self.textEdit_13 = QTextEdit(self.centralwidget)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setGeometry(QRect(350, 100, 41, 41))
        self.textEdit_14 = QTextEdit(self.centralwidget)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setGeometry(QRect(150, 100, 41, 41))
        self.textEdit_15 = QTextEdit(self.centralwidget)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setGeometry(QRect(400, 100, 41, 41))
        self.textEdit_16 = QTextEdit(self.centralwidget)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setGeometry(QRect(250, 100, 41, 41))
        self.textEdit_17 = QTextEdit(self.centralwidget)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setGeometry(QRect(450, 100, 41, 41))
        self.textEdit_18 = QTextEdit(self.centralwidget)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setGeometry(QRect(50, 100, 41, 41))
        self.textEdit_19 = QTextEdit(self.centralwidget)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setGeometry(QRect(200, 150, 41, 41))
        self.textEdit_20 = QTextEdit(self.centralwidget)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setGeometry(QRect(300, 150, 41, 41))
        self.textEdit_21 = QTextEdit(self.centralwidget)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setGeometry(QRect(100, 150, 41, 41))
        self.textEdit_22 = QTextEdit(self.centralwidget)
        self.textEdit_22.setObjectName(u"textEdit_22")
        self.textEdit_22.setGeometry(QRect(350, 150, 41, 41))
        self.textEdit_23 = QTextEdit(self.centralwidget)
        self.textEdit_23.setObjectName(u"textEdit_23")
        self.textEdit_23.setGeometry(QRect(150, 150, 41, 41))
        self.textEdit_24 = QTextEdit(self.centralwidget)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setGeometry(QRect(400, 150, 41, 41))
        self.textEdit_25 = QTextEdit(self.centralwidget)
        self.textEdit_25.setObjectName(u"textEdit_25")
        self.textEdit_25.setGeometry(QRect(250, 150, 41, 41))
        self.textEdit_26 = QTextEdit(self.centralwidget)
        self.textEdit_26.setObjectName(u"textEdit_26")
        self.textEdit_26.setGeometry(QRect(450, 150, 41, 41))
        self.textEdit_27 = QTextEdit(self.centralwidget)
        self.textEdit_27.setObjectName(u"textEdit_27")
        self.textEdit_27.setGeometry(QRect(50, 150, 41, 41))
        self.textEdit_28 = QTextEdit(self.centralwidget)
        self.textEdit_28.setObjectName(u"textEdit_28")
        self.textEdit_28.setGeometry(QRect(200, 200, 41, 41))
        self.textEdit_29 = QTextEdit(self.centralwidget)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setGeometry(QRect(300, 200, 41, 41))
        self.textEdit_30 = QTextEdit(self.centralwidget)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setGeometry(QRect(100, 200, 41, 41))
        self.textEdit_31 = QTextEdit(self.centralwidget)
        self.textEdit_31.setObjectName(u"textEdit_31")
        self.textEdit_31.setGeometry(QRect(350, 200, 41, 41))
        self.textEdit_32 = QTextEdit(self.centralwidget)
        self.textEdit_32.setObjectName(u"textEdit_32")
        self.textEdit_32.setGeometry(QRect(150, 200, 41, 41))
        self.textEdit_33 = QTextEdit(self.centralwidget)
        self.textEdit_33.setObjectName(u"textEdit_33")
        self.textEdit_33.setGeometry(QRect(400, 200, 41, 41))
        self.textEdit_34 = QTextEdit(self.centralwidget)
        self.textEdit_34.setObjectName(u"textEdit_34")
        self.textEdit_34.setGeometry(QRect(250, 200, 41, 41))
        self.textEdit_35 = QTextEdit(self.centralwidget)
        self.textEdit_35.setObjectName(u"textEdit_35")
        self.textEdit_35.setGeometry(QRect(450, 200, 41, 41))
        self.textEdit_36 = QTextEdit(self.centralwidget)
        self.textEdit_36.setObjectName(u"textEdit_36")
        self.textEdit_36.setGeometry(QRect(50, 200, 41, 41))
        self.textEdit_37 = QTextEdit(self.centralwidget)
        self.textEdit_37.setObjectName(u"textEdit_37")
        self.textEdit_37.setGeometry(QRect(200, 250, 41, 41))
        self.textEdit_38 = QTextEdit(self.centralwidget)
        self.textEdit_38.setObjectName(u"textEdit_38")
        self.textEdit_38.setGeometry(QRect(300, 250, 41, 41))
        self.textEdit_39 = QTextEdit(self.centralwidget)
        self.textEdit_39.setObjectName(u"textEdit_39")
        self.textEdit_39.setGeometry(QRect(100, 250, 41, 41))
        self.textEdit_40 = QTextEdit(self.centralwidget)
        self.textEdit_40.setObjectName(u"textEdit_40")
        self.textEdit_40.setGeometry(QRect(350, 250, 41, 41))
        self.textEdit_41 = QTextEdit(self.centralwidget)
        self.textEdit_41.setObjectName(u"textEdit_41")
        self.textEdit_41.setGeometry(QRect(150, 250, 41, 41))
        self.textEdit_42 = QTextEdit(self.centralwidget)
        self.textEdit_42.setObjectName(u"textEdit_42")
        self.textEdit_42.setGeometry(QRect(400, 250, 41, 41))
        self.textEdit_43 = QTextEdit(self.centralwidget)
        self.textEdit_43.setObjectName(u"textEdit_43")
        self.textEdit_43.setGeometry(QRect(250, 250, 41, 41))
        self.textEdit_44 = QTextEdit(self.centralwidget)
        self.textEdit_44.setObjectName(u"textEdit_44")
        self.textEdit_44.setGeometry(QRect(450, 250, 41, 41))
        self.textEdit_45 = QTextEdit(self.centralwidget)
        self.textEdit_45.setObjectName(u"textEdit_45")
        self.textEdit_45.setGeometry(QRect(50, 250, 41, 41))
        self.textEdit_46 = QTextEdit(self.centralwidget)
        self.textEdit_46.setObjectName(u"textEdit_46")
        self.textEdit_46.setGeometry(QRect(200, 300, 41, 41))
        self.textEdit_47 = QTextEdit(self.centralwidget)
        self.textEdit_47.setObjectName(u"textEdit_47")
        self.textEdit_47.setGeometry(QRect(300, 300, 41, 41))
        self.textEdit_48 = QTextEdit(self.centralwidget)
        self.textEdit_48.setObjectName(u"textEdit_48")
        self.textEdit_48.setGeometry(QRect(100, 300, 41, 41))
        self.textEdit_49 = QTextEdit(self.centralwidget)
        self.textEdit_49.setObjectName(u"textEdit_49")
        self.textEdit_49.setGeometry(QRect(350, 300, 41, 41))
        self.textEdit_50 = QTextEdit(self.centralwidget)
        self.textEdit_50.setObjectName(u"textEdit_50")
        self.textEdit_50.setGeometry(QRect(150, 300, 41, 41))
        self.textEdit_51 = QTextEdit(self.centralwidget)
        self.textEdit_51.setObjectName(u"textEdit_51")
        self.textEdit_51.setGeometry(QRect(400, 300, 41, 41))
        self.textEdit_52 = QTextEdit(self.centralwidget)
        self.textEdit_52.setObjectName(u"textEdit_52")
        self.textEdit_52.setGeometry(QRect(250, 300, 41, 41))
        self.textEdit_53 = QTextEdit(self.centralwidget)
        self.textEdit_53.setObjectName(u"textEdit_53")
        self.textEdit_53.setGeometry(QRect(450, 300, 41, 41))
        self.textEdit_54 = QTextEdit(self.centralwidget)
        self.textEdit_54.setObjectName(u"textEdit_54")
        self.textEdit_54.setGeometry(QRect(50, 300, 41, 41))
        self.textEdit_55 = QTextEdit(self.centralwidget)
        self.textEdit_55.setObjectName(u"textEdit_55")
        self.textEdit_55.setGeometry(QRect(200, 350, 41, 41))
        self.textEdit_56 = QTextEdit(self.centralwidget)
        self.textEdit_56.setObjectName(u"textEdit_56")
        self.textEdit_56.setGeometry(QRect(300, 350, 41, 41))
        self.textEdit_57 = QTextEdit(self.centralwidget)
        self.textEdit_57.setObjectName(u"textEdit_57")
        self.textEdit_57.setGeometry(QRect(100, 350, 41, 41))
        self.textEdit_58 = QTextEdit(self.centralwidget)
        self.textEdit_58.setObjectName(u"textEdit_58")
        self.textEdit_58.setGeometry(QRect(350, 350, 41, 41))
        self.textEdit_59 = QTextEdit(self.centralwidget)
        self.textEdit_59.setObjectName(u"textEdit_59")
        self.textEdit_59.setGeometry(QRect(150, 350, 41, 41))
        self.textEdit_60 = QTextEdit(self.centralwidget)
        self.textEdit_60.setObjectName(u"textEdit_60")
        self.textEdit_60.setGeometry(QRect(400, 350, 41, 41))
        self.textEdit_61 = QTextEdit(self.centralwidget)
        self.textEdit_61.setObjectName(u"textEdit_61")
        self.textEdit_61.setGeometry(QRect(250, 350, 41, 41))
        self.textEdit_62 = QTextEdit(self.centralwidget)
        self.textEdit_62.setObjectName(u"textEdit_62")
        self.textEdit_62.setGeometry(QRect(450, 350, 41, 41))
        self.textEdit_63 = QTextEdit(self.centralwidget)
        self.textEdit_63.setObjectName(u"textEdit_63")
        self.textEdit_63.setGeometry(QRect(50, 350, 41, 41))
        self.textEdit_64 = QTextEdit(self.centralwidget)
        self.textEdit_64.setObjectName(u"textEdit_64")
        self.textEdit_64.setGeometry(QRect(200, 400, 41, 41))
        self.textEdit_65 = QTextEdit(self.centralwidget)
        self.textEdit_65.setObjectName(u"textEdit_65")
        self.textEdit_65.setGeometry(QRect(300, 400, 41, 41))
        self.textEdit_66 = QTextEdit(self.centralwidget)
        self.textEdit_66.setObjectName(u"textEdit_66")
        self.textEdit_66.setGeometry(QRect(100, 400, 41, 41))
        self.textEdit_67 = QTextEdit(self.centralwidget)
        self.textEdit_67.setObjectName(u"textEdit_67")
        self.textEdit_67.setGeometry(QRect(350, 400, 41, 41))
        self.textEdit_68 = QTextEdit(self.centralwidget)
        self.textEdit_68.setObjectName(u"textEdit_68")
        self.textEdit_68.setGeometry(QRect(150, 400, 41, 41))
        self.textEdit_69 = QTextEdit(self.centralwidget)
        self.textEdit_69.setObjectName(u"textEdit_69")
        self.textEdit_69.setGeometry(QRect(400, 400, 41, 41))
        self.textEdit_70 = QTextEdit(self.centralwidget)
        self.textEdit_70.setObjectName(u"textEdit_70")
        self.textEdit_70.setGeometry(QRect(250, 400, 41, 41))
        self.textEdit_71 = QTextEdit(self.centralwidget)
        self.textEdit_71.setObjectName(u"textEdit_71")
        self.textEdit_71.setGeometry(QRect(450, 400, 41, 41))
        self.textEdit_72 = QTextEdit(self.centralwidget)
        self.textEdit_72.setObjectName(u"textEdit_72")
        self.textEdit_72.setGeometry(QRect(50, 400, 41, 41))
        self.textEdit_73 = QTextEdit(self.centralwidget)
        self.textEdit_73.setObjectName(u"textEdit_73")
        self.textEdit_73.setGeometry(QRect(200, 450, 41, 41))
        self.textEdit_74 = QTextEdit(self.centralwidget)
        self.textEdit_74.setObjectName(u"textEdit_74")
        self.textEdit_74.setGeometry(QRect(300, 450, 41, 41))
        self.textEdit_75 = QTextEdit(self.centralwidget)
        self.textEdit_75.setObjectName(u"textEdit_75")
        self.textEdit_75.setGeometry(QRect(100, 450, 41, 41))
        self.textEdit_76 = QTextEdit(self.centralwidget)
        self.textEdit_76.setObjectName(u"textEdit_76")
        self.textEdit_76.setGeometry(QRect(350, 450, 41, 41))
        self.textEdit_77 = QTextEdit(self.centralwidget)
        self.textEdit_77.setObjectName(u"textEdit_77")
        self.textEdit_77.setGeometry(QRect(150, 450, 41, 41))
        self.textEdit_78 = QTextEdit(self.centralwidget)
        self.textEdit_78.setObjectName(u"textEdit_78")
        self.textEdit_78.setGeometry(QRect(400, 450, 41, 41))
        self.textEdit_79 = QTextEdit(self.centralwidget)
        self.textEdit_79.setObjectName(u"textEdit_79")
        self.textEdit_79.setGeometry(QRect(250, 450, 41, 41))
        self.textEdit_80 = QTextEdit(self.centralwidget)
        self.textEdit_80.setObjectName(u"textEdit_80")
        self.textEdit_80.setGeometry(QRect(450, 450, 41, 41))
        self.textEdit_81 = QTextEdit(self.centralwidget)
        self.textEdit_81.setObjectName(u"textEdit_81")
        self.textEdit_81.setGeometry(QRect(50, 450, 41, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(580, 290, 141, 111))
        Sudoku.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Sudoku)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 841, 22))
        Sudoku.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Sudoku)
        self.statusbar.setObjectName(u"statusbar")
        Sudoku.setStatusBar(self.statusbar)

        self.retranslateUi(Sudoku)

        QMetaObject.connectSlotsByName(Sudoku)
    # setupUi

    def retranslateUi(self, Sudoku):
        Sudoku.setWindowTitle(QCoreApplication.translate("Sudoku", u"Sudoku", None))
        self.exit.setText(QCoreApplication.translate("Sudoku", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.button_1.setText(QCoreApplication.translate("Sudoku", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u0443\u0434\u043e\u043a\u0443", None))
        self.button_3.setText(QCoreApplication.translate("Sudoku", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.textEdit.setHtml(QCoreApplication.translate("Sudoku", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("Sudoku", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Z003'; font-size:11pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-weight:400; font-style:normal;\">3</span></p></body></html>", None))
        self.label.setText("")
    # retranslateUi

