print("Welcome to Task Manager\n")
print("""Enter 1 to add a Task at the end
Enter 2 to insert a Task at specific position
Enter 3 to remove a Task
Enter 4 clear Tasks
Enter 5 to exit
""")

a=[]
while(True):
    c=int(input("Enter your choice:"))
    if (c>0 and c<6):
        if c==1:
            t=input("Enter the task:")
            a.append(t)
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==2:
            pos=int(input("Enter the position where task is to be inserted:"))
            t=input("Enter the task:")
            a.insert(pos,t)
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==3:
            rm=input("Enter the task to be removed:")
            if rm in a:
                a.remove(rm)
            else:
                print("Task not Recorded!!\n")
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==4:
            a.clear()
            print("Tasks Manager Cleared!!!\n")

        else:
            print("Exiting from task Manager!")
            break
    else:
        print("Invalid Choice!!!\n")
        break
