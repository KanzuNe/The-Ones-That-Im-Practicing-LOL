import os 
import subprocess

sv1= dict(name= "", grade = "", gpa = "")
sv2=dict(name= "", grade = "", gpa = "")
sv3=dict(name= "", grade = "", gpa = "")
sv4=dict(name= "", grade = "", gpa = "")



choice = 1
while choice !="0":
    print("1.Them sinh Vien")
    print("2.Sua Sinh Vien")
    print("3.Xoa Sinh Vien")
    print("4.Liet Ke Sinh Vien")
    print("5. Tim Kiem Sinh Vien")
    print("6.Sap xep sinh vien")
    choice =(input("Nhap Muc Muon Chon: "))
    if choice == "1":
            print("Currently in Them Sinh Vien")
            if sv1["name"] == "":
                name1 = input("Nhap ten sinh vien 1:  ")
                sv1["name"] = name1
                grade1 = input("Nhap khoa sinh vien 1: ")
                sv1["grade"]= grade1
                gpa1 = input("Nhap gpa sinh vien 1: ")
                sv1["gpa"]= gpa1
                print(f"Đã thêm thành công sinh viên 1:{sv1['name']}, {sv1['grade']}, {sv1['gpa']}")

            elif sv2["name"] == "":
                name2 = input("Nhap ten sinh vien 2:  ")
                sv2["name"] = name2
                grade2 = input("Nhap khoa sinh vien 2: ")
                sv2["grade"]= grade2
                gpa2 = input("Nhap gpa sinh vien 2: ")
                sv2["gpa"]= gpa2
                print(f"Đã thêm thành công sinh viên 2:{sv2['name']}, {sv2['grade']}, {sv2['gpa']}")
            elif sv3["name"] == "":
                name3 = input("Nhap ten sinh vien 3:  ")
                sv3["name"] = name3
                grade3 = input("Nhap khoa sinh vien 3: ")
                sv3["grade"]= grade3
                gpa3 = input("Nhap gpa sinh vien 3: ")
                sv3["gpa"]= gpa3
                print(f"Đã thêm thành công sinh viên 3:{sv3['name']}, {sv3['grade']}, {sv3['gpa']}")
            elif sv4["name"] == "":
                name4 = input("Nhap ten sinh vien 4:  ")
                sv4["name"] = name4
                grade4 = input("Nhap khoa sinh vien 4: ")
                sv4["grade"]= grade4
                gpa4 = input("Nhap gpa sinh vien 4: ")
                sv4["gpa"]= gpa4
                print(f"Đã thêm thành công sinh viên 4:{sv4['name']}, {sv4['grade']}, {sv4['gpa']}")
            input("Ấn nút bất kỳ để tiếp")
            pass
    elif choice == "2":
            print("Currenly in Sua Sinh Vien")
            stt = int(input("Nhap stt sinh vien can sua: "))
            if stt ==1:
                name1 = input("Nhap ten sinh vien 1:  ")
                sv1["name"] = name1
                grade1 = input("Nhap khoa sinh vien 1: ")
                sv1["grade"]= grade1
                gpa1 = input("Nhap gpa sinh vien 1: ")
                sv1["gpa"]= gpa1
                print(f"Đã sửa thành công sinh viên 1:{sv1['name']}, {sv1['grade']}, {sv1['gpa']}")
            if stt == 2:
                name2 = input("Nhap ten sinh vien 2:  ")
                sv2["name"] = name2
                grade2 = input("Nhap khoa sinh vien 2: ")
                sv2["grade"]= grade2
                gpa2 = input("Nhap gpa sinh vien 2: ")
                sv2["gpa"]= gpa2
                print(f"Đã sửa thành công sinh viên 2:{sv2['name']}, {sv2['grade']}, {sv2['gpa']}")
            if stt == 3:
                sv3["name"] = ""
                name3 = input("Nhap ten sinh vien 3:  ")
                sv3["name"] = name3
                grade3 = input("Nhap khoa sinh vien 3: ")
                sv3["grade"]= grade3
                gpa3 = input("Nhap gpa sinh vien 3: ")
                sv3["gpa"]= gpa3
                print(f"Đã sửa thành công sinh viên 3:{sv3['name']}, {sv3['grade']}, {sv3['gpa']}")
            if stt == 4:
                name4 = input("Nhap ten sinh vien 4:  ")
                sv4["name"] = name4
                grade4 = input("Nhap khoa sinh vien 4: ")
                sv4["grade"]= grade4
                gpa4 = input("Nhap gpa sinh vien 4: ")
                sv4["gpa"]= gpa4
                print(f"Đã sửa thành công sinh viên 4:{sv4['name']}, {sv4['grade']}, {sv4['gpa']}")
            input("Ấn nút bất kỳ để tiếp")
            pass    
    elif choice == "3":
            print("Currently in Xoa Sinh Vien")
            inp= int(input("Nhap stt sinh vien muon xoa: "))
            if inp == 1:
                for k in sv1:
                    sv1[k] = ""
                print("Đã xoá thành công!")
            elif inp == 2:
                for k in sv2:
                    sv2[k] = ""
                print("Đã xoá thành công!")
            elif inp ==3:
                for k in sv3:
                    sv3[k] = ""
                print("Đã xoá thành công!")
            elif inp ==4:
                for k in sv4:
                    sv4[k] = ""
            input("Ấn nút bất kỳ để tiếp")
            pass
    elif choice == "4":
            print("Currently in Liet Ke Sinh Vien")
            print("\nThông tin sinh viên 1: ")
            for k,v in sv1.items():
                print(f"{k.upper()}: {v}")
            print("\nThông tin sinh viên 2: ")
            for k,v in sv2.items():
                print(f"{k.upper()}: {v}")
            print("\nThông tin sinh viên 3: ")
            for k,v in sv3.items():
                print(f"{k.upper()}: {v}")
            print("\nThông tin sinh viên 4:")
            for k,v in sv4.items():
                print(f"{k.upper()}: {v}")
            input("Ấn nút bất kỳ để tiếp")
            pass
    elif choice == "5":
            print("Currently in Tim Kiem Sinh Vien")
            stt = int(input("Nhap lựa chọn, 0 theo tên, 1 theo khoa: "))
            if stt == 0:
                choice1 = input("Nhập tên sinh viên: ")
                if choice1.lower() == sv1["name".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("\nThông tin sinh viên 1: ")
                    for k,v in sv1.items():
                        print(f"{k.upper()}: {v}")
                elif choice1.lower() == sv2["name".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("\nThông tin sinh viên 2: ")
                    for k,v in sv2.items():
                        print(f"{k.upper()}: {v}")
                elif choice1.lower() == sv3["name".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("\nThông tin sinh viên 3: ")
                    for k,v in sv3.items():
                        print(f"{k.upper()}: {v}")
                elif choice1.lower() == sv4["name".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("\nThông tin sinh viên 4: ")
                    for k,v in sv4.items():
                        print(f"{k.upper()}: {v}")
                    
            elif stt == 1:
                choice1 = input("Nhập khoa sinh viên: ")
                if choice1.lower() == sv1["grade".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("Thông tin sinh viên 1: \n")
                    for k,v in sv1.items():
                        print(f"{k.upper()}: {v}")
                elif choice1.lower() == sv2["grade".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("Thông tin sinh viên 2: \n")
                    for k,v in sv2.items():
                        print(f"{k.upper()}: {v}")
                elif choice1.lower() == sv3["grade".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("Thông tin sinh viên 3: \n")
                    for k,v in sv3.items():
                        print(f"{k.upper()}: {v}")
                elif choice1.lower() == sv4["grade".lower()]:
                    print("Đã tìm thấy sinh viên!")
                    print("Thông tin sinh viên 4: \n")
                    for k,v in sv4.items():
                        print(f"{k.upper()}: {v}")
            input("Ấn nút bất kỳ để tiếp")
            pass
    elif choice == "6":
            print("Currently in Sap Xep Sinh Vien")
            stt = int(input("Nhập kiểu sắp xếp gpa, 0 for tăng dần, 1 for giảm dần: "))
            students = [("sv1", sv1.copy()), ("sv2", sv2.copy()), ("sv3", sv3.copy()), ("sv4", sv4.copy())]
            #Fix logic sắp xếp
            if stt == 0:
                sorted_stu = sorted(students, key=lambda stt_sv: float(stt_sv[1]["gpa"]))
                print("Đã sắp xếp sinh viên theo GPA tăng dần!")
            
            elif stt == 1:
                sorted_stu = sorted(students, key=lambda stt_sv: float(stt_sv[1]["gpa"]), reverse=True)
                print("Đã sắp xếp sinh viên theo GPA giảm dần!")
            #Clear trước khi uploda data mới  
            sv1.clear()
            sv2.clear()
            sv3.clear()
            sv4.clear()
            #update copy ver của dict vào org dict
            sv1.update(sorted_stu[0][1])
           
            sv2.update(sorted_stu[1][1])
          
            sv3.update(sorted_stu[2][1])
        
            sv4.update(sorted_stu[3][1])
            input("Ấn nút bất kỳ để tiếp")
            pass
    
    elif choice == "0":
        break
    else: 
        print("Sai cú pháp, nhập lại!")

    os.system('cls')

    

