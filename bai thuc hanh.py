import os
import subprocess
import csv

class Student:
    current_List =[]
    final_list =[]
    def __init__(self, msv, hovaten, gpa):
        self.msv = msv
        self.hovaten = hovaten
        self.gpa = gpa
    def __str__(self):
        return(f"Ma Sinh Vien: {self.msv}, Ho va Ten: {self.hovaten}, GPA : {self.gpa}")
   
def load_ds():
        with open("ds_sv.csv", "r") as f:
            try:
                for line in f:
                    msv, hovaten,gpa = line.split(",")
                    sv = Student(msv, hovaten, gpa)
                    Student.final_list.append(sv)
            except:
                pass
    
def save_ds():
        with open("ds_sv.csv", "a") as f:
            for sv in Student.current_List:
                f.write(f"{sv.msv},{sv.hovaten},{sv.gpa}\n")
        return
    


while True:
    Student.final_list.clear()
    load_ds()
    print("1.Them sinh Vien")
    print("2.Sua Sinh Vien")
    print("3.Xoa Sinh Vien")
    print("4.Liet Ke Sinh Vien")
    print("5. Tim Kiem Sinh Vien")
    print("6.Sap xep sinh vien")
    choice = (input("Nhap Muc Muon Chon: "))
    print("\n")

    if choice == "1":
        print("Currently in Them Sinh Vien ")
        msv = input("Nhap msv ").strip()
        hovaten = input("Nhap ten sv ").strip()
        gpa = input("Nhap Gpa Sinh vien ").strip()
        sv = Student(msv, hovaten,gpa )
        Student.current_List.append(sv)
        save_ds()
        Student.current_List.clear()


    if choice == "2":
        found = False
        inp = input("Vui Long Sua Theo Ma Sinh Vien: ").strip()
        for sv in Student.final_list:
            if inp == sv.msv:
                found = True
                sv.msv = input("Nhap msv ").strip()
                sv.hovaten = input("Nhap ten sv ").strip()
                sv.gpa = input("Nhap Gpa Sinh vien ").strip()
                print("Da Cap Nhat Thanh Cong")
                
        if found == False:
            print("Khong co sinh vien nao nhu vay")

        with open("ds_sv.csv", "w") as f:
            for sv in Student.final_list:
                f.write(f"{sv.msv},{sv.hovaten},{sv.gpa}\n")
            

        pass
    if choice == "3":
        found = False
        inp = input("Vui Long Nhap MSV Can Xoa: ").strip()
        for sv in Student.final_list:
            if inp == sv.msv:
                found = True
                Student.final_list.remove(sv)
        if found == False:
            print("Khong co sinh vien nao nhu vay")

        with open("ds_sv.csv", "w") as f:
            for sv in Student.final_list:
                f.write(f"{sv.msv},{sv.hovaten},{sv.gpa}\n")
        pass
    if choice == "4":
        for something in Student.final_list:
            print(something)
        pass
    if choice == "5":
        stt = input("Nhap 0 theo ten, Nhap 1 de tim GPA MAX MIN ")
        if stt == "0":
            inp = input("Nhap tu khoa: ")
            for sv in Student.final_list:
                if inp.strip().lower() in sv.hovaten.lower():
                    print(sv)
        if stt == "1":
            if not Student.final_list:
                print("Danh sach sinh vien rong!")
            else:
                sorted_list = sorted(Student.final_list, key=lambda sv: float(sv.gpa))
                print("Sinh vien co GPA thap nhat:")
                print(sorted_list[0])
                print("Sinh vien co GPA cao nhat:")
                print(sorted_list[-1])
        pass
    if choice == "6":
        pass
