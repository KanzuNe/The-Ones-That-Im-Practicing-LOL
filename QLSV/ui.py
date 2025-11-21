# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import csv
import os

# -------------------------
# Student class
# -------------------------
class Student:
    final_list = []

    def __init__(self, msv, hovaten, gpa):
        self.msv = msv
        self.hovaten = hovaten
        self.gpa = gpa

    def __str__(self):
        return f"Ma Sinh Vien: {self.msv}, Ho va Ten: {self.hovaten}, GPA: {self.gpa}"

# -------------------------
# CSV functions
# -------------------------
CSV_FILE = "ds_sv.csv"

def load_ds():
    Student.final_list.clear()
    if not os.path.exists(CSV_FILE):
        return
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                msv, hovaten, gpa = line.split(",")
                Student.final_list.append(Student(msv, hovaten, gpa))

def save_ds():
    with open(CSV_FILE, "w", encoding="utf-8") as f:
        for sv in Student.final_list:
            f.write(f"{sv.msv},{sv.hovaten},{sv.gpa}\n")


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.list_student = Student.final_list

    
    def update_table(self):
        self.table.setRowCount(len(self.list_student))
        for index, student in enumerate(self.list_student):
            self.table.setItem(index, 0, QTableWidgetItem(student.msv))
            self.table.setItem(index, 1, QTableWidgetItem(student.hovaten))
            self.table.setItem(index, 2, QTableWidgetItem(student.gpa))

    
    def add_student(self):
        msv = self.line_msv.text().strip()
        hovaten = self.line_ten.text().strip()
        gpa = self.line_gpa.text().strip()
        if msv and hovaten and gpa:
            Student.final_list.append(Student(msv, hovaten, gpa))
            save_ds()
            self.update_table()
            self.clear_fields()


    def edit_student(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            student = Student.final_list[selected_row]
            student.msv = self.line_msv.text().strip()
            student.hovaten = self.line_ten.text().strip()
            student.gpa = self.line_gpa.text().strip()
            save_ds()
            self.update_table()
            self.clear_fields()


    def delete_student(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            Student.final_list.pop(selected_row)
            save_ds()
            self.update_table()
            self.clear_fields()

   
    def load_student_to_fields(self, row, column):
        if row >= 0 and row < len(Student.final_list):
            student = Student.final_list[row]
            self.line_msv.setText(student.msv)
            self.line_ten.setText(student.hovaten)
            self.line_gpa.setText(student.gpa)

    def tim_gpa(self):
        self.sorted_list = sorted(Student.final_list, key=lambda sv: float(sv.gpa))
        self.line_gpamax.setText(self.sorted_list[-1].gpa)


   
    def clear_fields(self):
        self.line_msv.clear()
        self.line_ten.clear()
        self.line_gpa.clear()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 721, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        #layout dien
        self.layout_dien = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layout_dien.setContentsMargins(0, 0, 0, 0)
        self.layout_dien.setObjectName("layout_dien")
        self.line_gpamax = QtWidgets.QLineEdit(self.formLayoutWidget)
        #line
        self.line_gpamax.setObjectName("line_gpamax")
        self.layout_dien.setWidget(3,QtWidgets.QFormLayout.FieldRole, self.line_gpamax)
        self.line_msv = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_msv.setObjectName("line_msv")
        self.layout_dien.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_msv)
        self.line_ten = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_ten.setObjectName("line_ten")
        self.layout_dien.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_ten)
        #label

        self.label_msv = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_msv.setFont(font)
        self.label_msv.setObjectName("label_msv")
        self.layout_dien.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_msv)
        self.label_ten = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_ten.setFont(font)
        self.label_ten.setObjectName("label_ten")
        self.layout_dien.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_ten)
        self.label_gpa = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_gpa.setFont(font)
        self.label_gpa.setObjectName("label_gpa")
        self.layout_dien.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_gpa)
        self.label_gpamax = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_gpamax.setFont(font)
        self.label_gpamax.setObjectName("label_gpamax")
        self.layout_dien.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_gpamax)
        self.line_gpa = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_gpa.setMinimumSize(QtCore.QSize(10, 10))
        self.line_gpa.setBaseSize(QtCore.QSize(16, 16))
        self.line_gpa.setObjectName("line_gpa")
        self.layout_dien.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_gpa)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 150, 731, 113))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.layout_button = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.layout_button.setContentsMargins(0, 0, 0, 0)
        self.layout_button.setObjectName("layout_button")
        self.button_gpamax = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_gpamax.setFont(font)
        self.button_gpamax.setObjectName("button_gpa")
        self.layout_button.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.button_gpamax)
        self.button_them = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_them.setFont(font)
        self.button_them.setObjectName("button_them")
        self.layout_button.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.button_them)
        self.button_sua = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_sua.setFont(font)
        self.button_sua.setObjectName("button_sua")
        self.layout_button.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.button_sua)
        self.button_xoa = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_xoa.setFont(font)
        self.button_xoa.setObjectName("button_xoa")
        self.layout_button.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.button_xoa)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(30, 280, 731, 281))
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setDefaultSectionSize(250)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons
        self.button_them.clicked.connect(self.add_student)
        self.button_sua.clicked.connect(self.edit_student)
        self.button_xoa.clicked.connect(self.delete_student)
        self.table.cellClicked.connect(self.load_student_to_fields)
        self.button_gpamax.clicked.connect(self.tim_gpa)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Manager"))
        self.label_msv.setText(_translate("MainWindow", "Ma Sinh Vien"))
        self.label_ten.setText(_translate("MainWindow", "Ten Sinh Vien"))
        self.label_gpa.setText(_translate("MainWindow", "GPA"))
        self.label_gpamax.setText(_translate("MainWindow", "GPA Cao Nhat"))
        self.button_them.setText(_translate("MainWindow", "Them Sinh Vien"))
        self.button_sua.setText(_translate("MainWindow", "Sua Sinh Vien"))
        self.button_xoa.setText(_translate("MainWindow", "Xoa Sinh Vien"))
        self.button_gpamax.setText(_translate("MainWindow", "GPA Cao Nhat"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ma Sinh Vien"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ten Sinh Vien"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "GPA"))


if __name__ == "__main__":
    load_ds()  
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.update_table()  
    MainWindow.show()
    sys.exit(app.exec_())
