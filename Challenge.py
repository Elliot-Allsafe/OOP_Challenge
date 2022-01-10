from Mind_Behind import *
import sys

def default():
    n1 = Organs()
    name = str(input("Your Name Please:> "))
    age = int(input("Your Age Please:> "))
    n1.name = name
    n1.age = age
    print("Name : " + str(n1.name))
    print("Age : " + str(n1.age))
def af_default():
    print("Choose an Organ : ")
    print("    1. Left Eye")
    print("    2. Right Eye")
    print("    3. Heart")
    print("    4. Stomach")
    print("    5. Skin")
    print("    6. Quit")

def nun():
    default()

def fun():
    try:
        af_default()
        choice = int(input("> "))
        if choice == 1:
            n1 = left_eye()
            print("Name : " + str(n1.name))
            print("Medical Condition : " + str(n1.medical_condition))
            print("Color : " + str(n1.color))
            print("    1. Quit ")
            qu = int(input("> "))
            if qu == 1:
                fun()
            else:
                print("I can't Understand.")
                fun()
        elif choice == 2:
            n1 = right_eye()
            print("Name : " + str(n1.name))
            print("Medical Condition : " + str(n1.medical_condition))
            print("Color : " + str(n1.color))
            print("    1. Quit ")
            qu = int(input("> "))
            if qu == 1:
                fun()
            else:
                print("I can't Understand.")
                fun()
        elif choice == 3:
            n1 = Heart()
            print("Name : " + str(n1.name))
            print("Medical Condition : " + str(n1.medical_condition))
            print("    1. Quit ")
            qu = int(input("> "))
            if qu == 1:
                fun()
            else:
                print("I can't Understand.")
                fun()
        elif choice == 4:
            n1 = Stomach()
            print("Name : " + str(n1.name))
            print("Medical Condition : " + str(n1.medical_condition))
            print("Fed Status : " + str(n1.fed_status))
            print("    0. Fed ")
            print("    1. Quit ")
            qu = int(input("> "))
            if qu == 0:
                print("Client Fed Successfully.")
                n1.fed_s()
                fun()
            elif qu == 1:
                fun()
            else:
                print("I can't Understand.")
                fun()
        elif choice == 5:
            n1 = Skin()
            print("Name : " + str(n1.name))
            print("Medical Condition : " + str(n1.medical_condition))
            print("Operation Status : " + str(n1.operation_status))
            print("    0. Operation")
            print("    1. Quit")
            qu = int(input("> "))
            if qu == 0:
                print("Operation Successful.")
                n1.sk()
                fun()
            elif qu == 1:
                fun()
            else:
                print("I can't Understand.")
                fun()
        elif choice == 6:
            print("Exiting")
            sys.exit()
        else:
            print("Sorry I can't Understand.")
            sys.exit()
    except ValueError:
        print("Use your Mind.")
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting.")
        sys.exit()


nun()
fun()
