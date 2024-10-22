import datetime
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
#def see_task():
