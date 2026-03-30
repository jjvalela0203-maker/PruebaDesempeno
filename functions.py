"""
Functions module
In this module are the main functions used in app.py
Like add, show, search, update and delete students
and clear screen function
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
    
    list.append(student) #Add the student to the end of the list

    print("Student added successfully")
    input("Press enter to continue")
    clear_screen

def show_list(list):
    """
    This function shows the list of students
    """

    if not list: #If the list its empty, dont show nothing
        print("The list is empty")

    else:  #On the other hand if the list conta
        for student in list:
            print("\nStudent ID:", student["id"],
                  "| Name:", student["name"],
                  "| Age:", student["age"],
                  "| Program:", student["program"],
                  "| State:", student["state"])
        
    input("Press enter to continue")
    clear_screen()

def search_name(list, name):
    """
    This function only search the name. 
    its for practical management of search
    """

    for student in list:
        if student["name"].lower() == name.lower():
            return student
    return None


def Search_student(list, id, name, age, program, state):
    """
    This function search students in the list
    For one characteristic, and print the student found info
    if no student is find, print a message of not found
    """
    submenu= True

    while submenu:
        print("\n", "="*30, "SEARCH STUDENT", "="*30)
        print("1) Search by ID")
        print("2) Search by name")
        print("3) Search by age")
        print("4) Search by program")
        print("5) Search by state")
        print("6) Back to main menu")


        selection=int(input("Select an option:"))

        if selection == 1:
            clear_screen()
            print("\n", "="*30, "SEARCH STUDENT", "="*30)
            id=int(input("Enter student ID:"))
            for student in list:
                if student["id"] == id:
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("\nStudent Found:", student)
                    input("Press enter to continue")
                    clear_screen()
                else:
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("Student not found")
                    input("Press enter to continue")
                    clear_screen()
        
        elif selection == 2:
            name=input("Enter student name:")
            for student in list:
                if student["name"].lower() == name.lower():
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("\nStudent Found:", student)
                    input("Press enter to continue")
                    clear_screen()
                else:
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("Student not found")
                    input("Press enter to continue")
                    clear_screen()
        
        elif selection == 3:
            age=int(input("Enter student age:"))
            for student in list:
                if student["age"] == age:
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("\nStudent Found:", {student})
                    input("Press enter to continue")
                    clear_screen()
                else:
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("Student not found")
                    input("Press enter to continue")
                    clear_screen()
        
        elif selection == 4:
            program=input("Enter student program:")
            for student in list:
                if student["program"].lower() == program.lower():
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("\nStudent Found:", {student})
                    input("Press enter to continue")
                    clear_screen()
                else:
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("Student not found")
                    input("Press enter to continue")
                    clear_screen()
        

        elif selection == 5:
            state=input("Enter student state(A for active and I for inactive):").lower()
            for student in list:
                if student["state"].lower() == state.lower():
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("\nStudent Found:", {student})
                    input("Press enter to continue")
                    clear_screen()
                else:
                    clear_screen()
                    print("\n", "="*30, "SEARCH STUDENT", "="*30)
                    print("Student not found")
                    input("Press enter to continue")
                    clear_screen()
        
        elif selection == 6:
            submenu= False
            clear_screen()

        else:
            print("Invalid option")
            input("Press enter to continue")
            clear_screen()

def update_student(list, name, new_age=None, new_program=None, new_state= None):
    """
    This function update the data of the students
    """
    student= search_name(list, name)

    if student is None:
        print("\n", "="*30, "UPDATE STUDENT", "="*30)
        print("Student not found")
        input("Press enter to continue")
        clear_screen()
        return

    if new_age is not None:
        student["age"]= new_age
    
    if new_program is not None:
        student["program"]= new_program
    
    if new_state is not None:
        student["state"]= new_state
    
    print("\n", "="*30, "UPDATE STUDENT", "="*30)
    print("Student data updated")
    input("Press enter to continue")
    clear_screen()


def delete_student(list, name):
    """
    This function delete a student from the list
    """
    #Search student and remove it of the list
    for i, student in enumerate(list):
        if student["name"].lower() == name.lower():
            del list[i]
            print("\nStudent deleted successfully")
            input("Press enter to continue")
            clear_screen()
            return
    
    #If the student is not found

    print("Student not found")
    input("Press enter to continue")
    clear_screen()







    

    






            
            
        



            


    

    


