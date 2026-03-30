"""
"""
import os

def clear_screen():
    """
    This function cleans the screen.
    And confirms the SO to use the correct command
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add_student(list, id, name, age, program, state):
    """
    This function allow to the user to add a new student to the list
    """

    student= {"id": id,
               "name": name,
               "age": age,
               "program": program,
               "state":state}
    
    list.append(student)

    print("Student added successfully")
    input("Press enter to continue")
    clear_screen

def show_list(list):
    """
    This function shows the list of students
    """

    if not list: #If the list its empty, dont show nothing
        print("The list is empty")
        input("Press enter to continue")
        clear_screen

    else:  #On the other hand if the list conta
        for student in list:
            print("\nStudent ID:", student["id"],
                  "Name:", student["name"],
                  "Age:", student["age"],
                  "Program:", student["program"],
                  "State:", student["state"])
        
    input("Press enter to continue")
    clear_screen()
            


    

    


