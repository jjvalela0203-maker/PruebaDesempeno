"""
Main module of students register
In this module the user can add, show, search, update and delete students
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
    print("6) Exit")

menu= True

while menu:
    main_menu()

    valid= True
    
    while valid:
        try:
            option=int(input("Select an option:")) #Option validations
            if 1<= option <= 6:
                valid= False
            else:
                functions.clear_screen()
                print("\n", "="*30, "MENU", "="*30)
                print("Invalid option, Please enter a valid number")
                input("Press enter to continue")
                functions.clear_screen()
        except ValueError:
            functions.clear_screen()
            print("\n", "="*30, "MENU", "="*30)
            print("Invalid option. please enter a number")
            input("Press enter to continue")
            functions.clear_screen()

        main_menu()

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
            age=int(input("Enter student age:")) #Age validations
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


    elif option == 2: #Show the list of students
        functions.clear_screen()
        print("\n", "="*30, "LIST OF STUDENTS", "="*30)
        functions.show_list(list) 


    elif option == 3: #Search a student 
        functions.clear_screen()
        if not list:
            print("\n", "="*30, "SEARCH STUDENT", "="*30)
            print("The list is empty")
            input("Press enter to continue")
            functions.clear_screen()
        else:
            functions.Search_student(list, id, name, age, program, state)

    elif option == 4: #Updata the data of a student
        functions.clear_screen()
        print("\n", "="*30, "UPDATE STUDENT", "="*30)
        if not list:
            print("The list is empty")
            input("Press enter to continue")
            functions.clear_screen()
        else:
            name=input("Enter student name:")

            age=(input("Enter new age (Enter to skip):"))
            if age == "":  # If the age is empty
                age=str(age) #The age is considered a text
                pass
            else:
                try:
                    while int(age) <= 0: #If the age is filled, consider it  as a number
                        print("Invalid age")
                        age=int(input("Enter new age (Enter to skip):"))
                except ValueError:
                        print("Invalid age")
                        age=(input("Enter new age (Enter to skip):"))

            program=input("Enter new program (Enter to skip):")
            
            state=input("Enter new state(A for active and I for inactive) (Enter to skip):").lower() #State validations
            while state != "a" and state != "i":
                print("Invalid state")
                state=input("Enter new state(A for active and I for inactive) (Enter to skip):").lower()
            
            
            new_age= age if age else None
            new_program= program if program else None
            new_state= state if state else None

            functions.update_student(list, name, new_age, new_program, new_state)

    elif option == 5: #Delete a student if its found
        functions.clear_screen()
        print("\n", "="*30, "DELETE STUDENT", "="*30)
        if not list:
            print("The list is empty")
            input("Press enter to continue")
            functions.clear_screen()
        else:    
            name=input("Enter student name:")
            functions.delete_student(list, name)

    elif option == 6: #Exit the program
        functions.clear_screen()
        print("\n", "="*30, "EXIT", "="*30)
        print("Goodbye!")
        input("Press enter to continue")
        functions.clear_screen()
        menu= False





            




