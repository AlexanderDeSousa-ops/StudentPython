student_list = []
import sys
import sqlite3

class Student :
    def __init__(self , name, lastN, studID, age, dep) :
        self.name = name
        self.lastN = lastN
        self.studID = studID
        self.age = age
        self.dep = dep

def student_manaegemnt() :
    print("")
    print("     MENU")
    print("option 1 : Add a student")
    print("option 2 : Display the student(s)")
    print("option 3 : Edit student")
    print("option 4 : Exit application")
    option = input("Enter : ").strip()
    #learned not
    while (option.isdigit() == False or (int(option) < 1) or (int(option) > 4 )):
        print("     MENU")
        print("option 1 : Add a student")
        print("option 2 : Display the student(s)")
        print("option 3 : Edit student")
        print("option 4 : Exit application")
        option = input("Enter : ").strip()
    if(int(option) == 1 ):
        add_student()
    elif(int(option) == 2):
        display_student()
    elif(int(option) == 3):
        modify_student()
    else :
        print("bye bye ")
        connection = sqlite3.connect("db_st.db")
        cursor = connection.cursor()
        for st in student_list:
            cursor.execute("INSERT INTO students VALUES(?,?,?,?,?)", (st.studID,st.name,st.lastN,st.age,st.dep))
            connection.commit()
        connection.close()
        sys.exit()
        

def add_student():
    name_Student = input("Enter the student's first name: ").strip()
    last_Student = input("Enter their last name: ")
    studid_Student = input("Enter student ID: ").strip()
    age_Student = input("Enter their age: ").strip()
    dep_Student = input("Enter their department: ").strip()

    new_Student = Student(name_Student, last_Student, studid_Student, age_Student, dep_Student)
    student_list.append(new_Student)

    print(f"{name_Student} {last_Student} has been added.")
    student_manaegemnt()

def display_student():
    if len(student_list) == 0:
        print("there is no students in system")
    else :
        
        for i in range(0, len(student_list)):
            print("")
            print(f"{student_list[i].name} {student_list[i].lastN} | ID: {student_list[i].studID} | Age: {student_list[i].age} | Department: {student_list[i].dep}")

    student_manaegemnt()

def modify_student():
    print()
    student_manaegemnt()




student_manaegemnt()