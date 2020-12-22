from tkinter import messagebox
import tkinter as tk

from PyQt5 import QtCore, QtGui, QtWidgets

from dropdown_content import provides_dropdown_data
from functions import connecting_nbp_api, extracting_data_nbp_reply, calculate_result


class Ui_MainWindow(object):

    def __init__(self):
        """imports drop down list content"""
        self.comboBox_data = provides_dropdown_data()
        self.layout_settings = ("background: transparent;\n"
                                "border-style: outset;\n"
                                "border-radius: 10px;\n"
                                "border-width: 1px;\n"
                                "border-color: white;\n"
                                "color: white")

    def sets_text(self, text):
        self.text_setting = f"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">{text}</span></p></body></html>"
        return self.text_setting

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 576)
        MainWindow.setMinimumSize(QtCore.QSize(800, 576))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 576))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphics/icon.png"), # HERE INSERT THE NAME OF THE FOLDER WITH THE GRAPHIC "icon.png"
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background: url(C:/Path/to/a/file/background3.PNG)")  # HERE INSERT THE PATH TO THE FILE "background3.PNG"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(250, 554))
        self.groupBox.setStyleSheet("background: transparent;\n"
                                    "border-style: outset")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background: transparent")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: transparent")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: transparent")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(self.layout_settings)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(self.layout_settings)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: transparent")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: transparent;\n"
                                      "border-style: outset;\n"
                                      "border-radius: 10px;\n"
                                      "border-width: 1px;\n"
                                      "border-color: gold;\n"
                                      "color: gold")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setStyleSheet(self.layout_settings)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setStyleSheet(self.layout_settings)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(self.layout_settings)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setStyleSheet(self.layout_settings)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 5, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_4)

        '''assigns drop down list - from init'''
        self.comboBox.addItems(self.comboBox_data)
        self.comboBox_2.addItems(self.comboBox_data)

        ''' "CALCULATE" button connect to the function "calculate_button_launch" and passes the variables'''
        self.pushButton.clicked.connect(self.connecting_with_functions)

    def connecting_with_functions(self):
        """takes data from interface windows"""
        currency_from = self.comboBox.currentText()
        currency_to = self.comboBox_2.currentText()
        value = self.lineEdit_2.text()

        """takes only currency abbreviation"""
        currency_a = currency_from.split(" ")[0]
        currency_b = currency_to.split(" ")[0]

        """connects to NBP API"""
        nbp_list = connecting_nbp_api()
        if nbp_list == "ERROR1":
            return self.error_informant(
                'The application cannot connect to the database.\nPlease check internet connection.')

        """extract date and exchange rates"""
        date = str(extracting_data_nbp_reply(nbp_list, 'effectiveDate'))
        if date == "ERROR2":  # appears if there is mistake in expression 'effectiveDate'
            return self.error_informant('FATAL ERROR.\nIncorrect assignment to "date".')
        if date == "ERROR2.2":
            return self.error_informant("FATAL ERROR.\nDatabase is corrupted.")

        ex_rate_currency_a = extracting_data_nbp_reply(nbp_list, currency_a)
        if ex_rate_currency_a == "ERROR2":
            return self.error_informant("Please check window 'Currency from'.\n"
                                        "It seems that window is empty.\n"
                                        "\n"
                                        "If not, then FATAL ERROR.\nDatabase is corrupted.")
        if ex_rate_currency_a == "ERROR2.2":
            return self.error_informant("FATAL ERROR.\nDatabase is corrupted.")

        ex_rate_currency_b = extracting_data_nbp_reply(nbp_list, currency_b)
        if ex_rate_currency_b == "ERROR2":
            return self.error_informant("Please check window 'Currency to'.\n"
                                        "It seems that window is empty.\n"
                                        "\n"
                                        "If not, then FATAL ERROR.\nDatabase is corrupted.")
        if ex_rate_currency_b == "ERROR2.2":
            return self.error_informant("FATAL ERROR.\nDatabase is corrupted.")

        """calculate the result"""
        result_and_ratio = calculate_result(
            ex_rate_currency_a, ex_rate_currency_b, value)
        if result_and_ratio == "ERROR3":
            return self.error_informant('Value is incorrect. \n'
                                        '\n'
                                        'Please ensure, that value is a number,\n'
                                        'TIP: if there is "," please replace it with ".".\n'
                                        '\n'
                                        'Otherwise, there is FATAL ERROR with currency.')
        if result_and_ratio == "ERROR4":
            return self.error_informant("Second exchange rate ('Currency to') is equal to 0.\n"
                                        "Cannot divide by zero.")
        result = str(result_and_ratio[0])
        ratio = str(round(result_and_ratio[1], 6))

        '''updates lineEdits'''
        self.lineEdit_3.setText(result)
        self.lineEdit_5.setText(
            f'1 {self.comboBox.currentText().split(" ")[0]} = {ratio} {self.comboBox_2.currentText().split(" ")[0]}')
        self.lineEdit_4.setText(
            f'According to the average NBP rate of the day: {date}')

    def error_informant(self, text):
        root = tk.Tk()
        root.withdraw()
        root.iconbitmap(
            r'C:\Path\to\a\file\icon_1.ico')  # HERE INSERT THE PATH TO THE FILE "icon_1.ico"
        tk.messagebox.showerror("Error", f'{text}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Currency Converter"))
        self.label_4.setText(_translate(
            "MainWindow", self.sets_text("Result:")))
        self.label_3.setText(_translate(
            "MainWindow", self.sets_text("Value:")))
        self.label.setText(_translate(
            "MainWindow", self.sets_text("Currency from:")))
        self.label_2.setText(_translate(
            "MainWindow", self.sets_text("Currency to:")))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
