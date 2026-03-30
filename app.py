"""
"""
import os
import functions

list=[]

def main_menu():
    """
    """
    logo=r"""
     __ _             _            _           __            _     _            
    / _\ |_ _   _  __| | ___ _ __ | |_ ___    /__\ ___  __ _(_)___| |_ ___ _ __ 
    \ \| __| | | |/ _` |/ _ \ '_ \| __/ __|  / \/// _ \/ _` | / __| __/ _ \ '__|
    _\ \ |_| |_| | (_| |  __/ | | | |_\__ \ / _  \  __/ (_| | \__ \ ||  __/ |   
    \__/\__|\__,_|\__,_|\___|_| |_|\__|___/ \/ \_/\___|\__, |_|___/\__\___|_|   
                                                       |___/                    """
    
    print(logo)
    print("\n", "="*30, "MENU", "="*30)
    print("1) Add student")
    print("2) Show list of students")
    print("3) Search student")
    print("4) Update student info")
    print("5) Delete student")
    print("6) Save list")
    print("7) Load list")
    print("8) Exit")

menu= True

while menu:
    main_menu()

    valid= True
    
    while valid:
        try:
            option=int(input("Select an option:"))
            if 1<= option <= 6:
                valid= False
            else:
                functions.clear_screen()
                print("\n", "="*30, "MENU", "="*30)
                print("Invalid option, Please enter a valid number")
                input("Press enter to continue")
                functions.clear_screen()
        except ValueError:
            print("\n", "="*30, "MENU", "="*30)
            print("Invalid option. please enter a number")
            input("Press enter to continue")
            functions.clear_screen()

    if option == 1:
        functions.clear_screen()
        
        print("\n", "="*30, "ADD STUDENT", "="*30)
        
        #The program ask for the data of the student
        
        try:
            id=int(input("Enter student ID:"))
            if id < 0:
                print("Invalid ID")
                id=int(input("Enter student ID:"))
        except ValueError:
            print("Invalid ID")
            id=int(input("Enter student ID:"))
        
        name=input("Enter student name:")
        
        try:
            age=int(input("Enter student age:"))
            while age <= 0:
                print("Invalid age")
                age=int(input("Enter student age:"))
        except ValueError:
            print("Invalid age")
            age=int(input("Enter student age:"))
        
        program=input("Enter student program:")
        
        state=input("Enter student state(A for active and I for inactive):").lower()
        while state != "a" and state != "i":
            print("Invalid state")
            state= input("Enter student state(A for active and I for inactive):").lower()

        functions.add_student(list, id, name, age, program, state)

        functions.clear_screen()


    elif option == 2:
        functions.clear_screen()
        print("\n", "="*30, "LIST OF STUDENTS", "="*30)
        functions.show_list(list)


    elif option == 3:
        functions.clear_screen()
        functions.Search_student(list, id, name, age, program, state)

    elif option == 4:
        functions.clear_screen()
        print("\n", "="*30, "UPDATE STUDENT", "="*30)
        
        student=input("Enter student name:")

        try:
            new_name=input("Enter new student name (Enter to skip):")
            
            new_age=int(input("Enter new student age (Enter to skip):"))
            while new_age <= 0:
                print("Invalid age")
                new_age

            new_program=input("Enter new student program (Enter to skip):")

            new_state=input("Enter new student state(A for active and I for inactive) (Enter to skip):").lower()
            while new_state != "a" and new_state != "i":
                print("Invalid state")
                new_state=input("Enter new student state(A for active and I for inactive) (Enter to skip):").lower()
        
        except ValueError:
            print("Invalid data")
            input("Press enter to continue")
            functions.clear_screen()
            
    elif option == 5:
        functions.clear_screen()
        print("\n", "="*30, "DELETE STUDENT", "="*30)

    elif option == 6:
        functions.clear_screen()
        print("\n", "="*30, "SAVE LIST", "="*30)
    
    elif option == 7:
        functions.clear_screen()
        print("\n", "="*30, "LOAD LIST", "="*30)

    elif option == 8:
        functions.clear_screen()
        print("\n", "="*30, "EXIT", "="*30)
        print("Goodbye!")
        input("Press enter to continue")
        functions.clear_screen()
        menu= False





            




