from print_color import print
tasks:list[str] = []

# Main Title of the app 
print("Welcome to the To-Do-List app created by Hassan RJ\n")

# Main while loop of the app
while True:
    print("""Please choose a operation to do:
    1. Add Task
    2. Show Task
    3. Delete Task
    4. Exit
     """)
    # Taking user input to choose the operation
    user_input:str = input("Enter your choice: ")
    
    # Checking the user input and performing the operation
    if user_input not in ['1', '2', '3', '4']:
        print(" ")
        print("Invalid input Please Enter a valid number", tag='failure', tag_color='red', color='magenta')
        print(" ")
        
    # Checking if the user input is not a digit
    if not user_input.isdigit():
        print(" ")
        print("Invalid input Please Enter a valid number", tag='failure', tag_color='red', color='magenta')
        print(" ")

    # Performing the add task operation based on the user input
    if user_input == '1':
      while True:
        print(" ")
        task_input = str(input("Enter your task to add: ")) # taking input from the user
        tasks.append(task_input) # adding the task to the list
        print(" ") # Printing the success message
        print("Task successfully added to the list", tag='success', tag_color='green', color='white')
        print(" ")
        # Asking the user if they want to add more items
        want_to_add_more = str(input("Do you want to add more items? ( 'y' / 'n' )': "))
        if want_to_add_more.lower() == 'n':
          break

    # Performing the show task operation based on the user input
    if user_input == '2':
      if tasks: # Checking if the list is not empty
        print(" ")
        print("Your To-do list: ")
        # Looping through the list and printing the tasks
        for i in range(0, len(tasks)): 
          print(f"{i}. {tasks[i]}", color='green')
        print(" ") 
      else:
        print(" ")  # Printing the error message if the list is empty
        print("Your To-Do List is empty Please add item to the list first ", color='red')
        print(" ")
      
        
    # Performing the delete task operation based on the user input
    if user_input == '3':
        if tasks:  # Checking if the list is not empty
            print("\n Your To-do list: ") # Printing the list items
            for i in range(0, len(tasks)): 
                print(f"{i}. {tasks[i]}", color='green') 
            print(" ")
            
            input_to_delete_task = input("Enter the number of the item: ") 
            
            try: # usgin try and except block to check if the input index is present in the list
                if not input_to_delete_task.isdigit(): # Checking if the input for index is not a digit
                    print(" ")
                    print("Invalid input Please Enter a valid number", tag='failure', tag_color='red', color='magenta')
                    print(" ")
                else: # Deleting the task from the list based on the index provided by the user
                    tasks.remove(tasks[int(input_to_delete_task)])
                    print(" ")
                    print("Task successfully deleted from the list", tag='success', tag_color='green', color='white')
                    print(" ")
            except IndexError: # Handling the index error
                print(" ")  
                print("Item does not in the list", color='red')
                print(" ")
        else:
            print(" ")  
            print("Your To-Do List is empty Please add item to the list first ", color='red')
            print(" ")





    if user_input == '4':
      print("Thanks for playing", color='green')
      print("Credits: Hassan RJ", color='green')
      break
