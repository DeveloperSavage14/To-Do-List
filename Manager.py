import datetime
import argparse
def add_task(task,day,month):
    
    f = open("DateList.txt", "r")
    array = f.readlines()   
    x = str(day) + "/" + str(month) + "\n"
    array.append(x)
    f.close()
    f = open("DateList.txt", "w")
    for i in array:
        f.write(i)
    f.close()


    f = open("TaskList.txt", "r")
    array2 = f.readlines()
    x = str(task) + "\n"
    array2.append(x)
    f.close()
    f = open("TaskList.txt", "w")
    for i in array2:
        f.write(i)
    f.close()
def complete_task(task):
    code = str(task) + "\n" 
    taskno = 0
    found = False
    f = open("TaskList.txt", "r")
    array2 = f.readlines()
    f.close()
    f = open("TaskList.txt", "w")
    for i in array2:
        if i == code:
            found = True
        if found == False:
            taskno += 1
    if found == True:    
        array2.remove(code)
    else:
        print("Task not found please try another task")
    for i in array2:
        f.write(i)
    f.close()


    f = open("DateList.txt", "r")
    array = f.readlines()   
    f.close()
    if found == True:
        p = array[taskno]
        del array[taskno]
    f = open("DateList.txt", "w")
    for i in array:
        f.write(i)
    f.close()
    f = open("CompTasks.txt", "a")
    current_date = datetime.date.today()
    f.write(task + "   " + str(current_date) + "\n")
    f.close
def remove_task(task):
    code = str(task) + "\n" 
    taskno = 0
    found = False
    f = open("TaskList.txt", "r")
    array2 = f.readlines()
    f.close()
    f = open("TaskList.txt", "w")
    for i in array2:
        if i == code:
            found = True
        if found == False:
            taskno += 1
    if found == True:    
        array2.remove(code)
    else:
        print("Task not found please try another task")
    for i in array2:
        f.write(i)
    f.close()


    f = open("DateList.txt", "r")
    array = f.readlines()   
    f.close()
    if found == True:
        del array[taskno]
    f = open("DateList.txt", "w")
    for i in array:
        f.write(i)
    f.close()
def see_tasks():
    f = open("DateList.txt", "r")
    array = f.readlines()   
    f.close()
    f = open("TaskList.txt", "r")
    array2 = f.readlines()
    f.close()
    for i in range(len(array)):
        temp1 = array[i]
        temp2 = array2[i]
        temp2 = temp2[:-1]
        temp1 = temp1[:-1]
        print(temp2 + "    "+ temp1)
        print()
    if len(array) == 0:
        print("No tasks left to complete")
        print("If you would like to add a task please type")
        print("add_task(your task, the day that it is due, the month it is due)")
        print("Example: add_task(Essay,21,11)")
def see_completed():
    f = open("CompTasks.txt", "r")
    arr = f.readlines()
    for i in range(len(arr)):
        temp = arr[i]
        temp = temp[:-1]
        print(temp)
        print()
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific functions with arguments")
    parser.add_argument("function_name", type=str, help="The name of the function to run")
    parser.add_argument("args", nargs="*", help="Arguments for the function")
    args = parser.parse_args()
    
    if args.function_name == "add_task":
        if len(args.args) == 3:
            add_task(args.args[0], args.args[1],args.args[2])
        else:
            print("add task requires 3 arguments")
    elif args.function_name == "remove_task":
        if len(args.args) == 1:
            remove_task(args.args[0])
        else:
            print("remove task requires 1 argument")
    elif args.function_name == "complete_task":
        if len(args.args) == 1:
            complete_task(args.args[0])
        else:
            print("complete task requires 1 argument")
    elif args.function_name == "see_tasks":
        if len(args.args) == 0:
            see_tasks()
        else:
            print("see tasks requires no arguments")
    elif args.function_name == "see_completed":
        if len(args.args) == 0:
            see_completed()
        else:
            print("see completed requires no arguments")
    else:
        print("Function not found")
