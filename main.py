# main.py SCRIPT from TO-DO-LIST project.

#======================================#
#|*************VARIABLES**************|#
#======================================#

current_list = {}

welcome_message = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ◢◣  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-  ◢◣ 
|||| ******************TO-DO-LIST****************** ||||
|||| ---------------------------------------------- ||||
|||| *******************0G3NES1S******************* ||||
|||| ---------------------------------------------- ||||
|||| ***************CURRENT-COMMANDS*************** ||||
|||| *****/*?add*/*?remove*/*?list*/*?modify*/***** ||||
|||| ---------------------------------------------- |||| 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

#======================================#
#|**************CLASSES***************|#
#======================================#

class build_task:
    def __init__(self, task, completed):
        self.task = task 
        self.completed = completed

#======================================#
#|*************FUNCTIONS**************|#
#======================================#

def addTask_(task, completed):
    global current_list
    current_task = build_task(task, completed)
    list_length = len(current_list)
    current_list[f"Task:{list_length}"] = current_task
    print(f"\nTask:{list_length} Added succesfully!\n")
    return

def removeTask_(task_id):
    global current_list
    del current_list[f"Task:{task_id}"]
    print(f"\nTask:{task_id} Successfuly removed!\n")
    return

def listTask_():
    global current_list
    for key, value in current_list.items():
        print(f"{key} = TASK: {value.task} / COMPLETED: {value.completed}")
    print("\n")

def modifyTask_P1_(new_task, task_id): # Property 1 (task.task)
    # just changes the 'task' value from the task
    # to the selected new task
    global current_list
    current_list[f"Task:{task_id}"].task = new_task
    print(f"\nTask:{task_id} task value changed to a new task!\n")
    return

def modifyTask_P2_(task_id): # Property 2 (task.completed)
    # changes the value 'completed' of the respective
    # task depending on if it's false or true
    global current_list
    if current_list[f"Task:{task_id}"].completed == True:
        current_list[f"Task:{task_id}"].completed = False
        print(f"\nTask:{task_id} completed value changed to incompleted! (false)\n")
        return
    else:
        current_list[f"Task:{task_id}"].completed = True
        print(f"\nTask:{task_id} completed value changed to completed! (true)\n")
        return


#======================================#
#|***************GLOBAL***************|#
#======================================#

print(welcome_message)

#======================================#
#|****************MAIN****************|#
#======================================#

while True:    
    user_command = input() 

    # Command that adds a task
    # in the list of tasks 
    if user_command == "?add":
        print("\nSELECTED MODE: ADD TASK\nWhat are you thinking to do now, User?\n")
        task = input()
        print("\nTask is completed?\n")
        completed = input()
        if completed != "True" and completed != "true": 
            completed = False
        else:
            completed = True
        addTask_(task, completed)
        continue

    # Command that removes a task
    # in the list of tasks 
    elif user_command == "?remove":
        print("\nSELECTED MODE: REMOVE TASK\nWhat are you thinking to do now, User?\n")
        listTask_()
        print("\nSelect task to remove. User. (type the ID)\n")
        task_id = input()
        if current_list[f"Task:{task_id}"]:
            removeTask_(task_id)
            continue
        else:
            print(f"\nTask:{task_id} Does not exist. I'm so sorry User.\n")
            continue

    # Command that prints the entire
    # list of tasks added by the
    # User
    elif user_command == "?list":
        print(f"\nHere is the current list User!\n")
        listTask_()

    # Command that modifies a selected
    # task in the list.

    elif user_command == "?modify":
        print("\nSELECTED MODE: MODIFY TASK\nWhat are you thinking to do now, User?\n")
        for key, value in current_list.items():
            print(f"{key} = TASK: {value.task} / COMPLETED: {value.completed}")
        print("\nSelect task to modify. User. (type the ID)\n")
        task_id = input()
        if current_list[f"Task:{task_id}"]:
            print("\nSelect value to modify User. task / completed ?\n")
            response = input()
            if response == "task":
                print("\nType new task, User!\n")
                new_task = input()
                modifyTask_P1_(new_task, task_id)
                continue
            if response == "completed":
                modifyTask_P2_(task_id)
                continue
            else:
                print("\nSorry User. That's not a valid value.\n")
                continue
        else:
            print("\nSorry User. That's not a valid task.\n")
            continue
    else:
        print("\nSorry User. That's not a valid command.\n")
        continue
