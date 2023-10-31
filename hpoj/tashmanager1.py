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
    if (c>0 and c<8):
        if c==1:
            t=input("Enter the task:")
            a.append(t)
            print("task added succesfully!!")
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==2:
            pos=int(input("Enter the position where task is to be inserted:"))
            t=input("Enter the task:")
            a.insert(pos,t)
            print("task added succesfully!!")
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==3:
            ix=int(input("Enter the position of the task to be removed:"))
            if ix>(len(a)-1) or ix<0:
                print("Index specified not in the list")
            else:
                a.pop(ix)
                print("task popped Successfully!")
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==4:
            a.sort()
            print("tasks sorted!")
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==5:
            a.sort(reverse=True)
            print("Tasks Sorted in Reverse order !!")
            print("Tasks:\n")
            for i in a:
                print(i)
                print()
        elif c==6:
            a.clear()
            print("Tasks Manager Cleared!!!\n")
        elif c==7:
            print("Exiting from task Manager!")
            break
    else:
        print("Invalid Choice!!!\n")