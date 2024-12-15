#getting data function
def getdata():
    a=0
    for i in range(n):
        a=str(input("enter marks if student is absent put 'ab' : "))
        markList.append(a)
    print(markList)
    
    print("\n1--> avrage of the marks.")
    print("2--> no. of absent students.")
    print("3--> maximum marks.")
    print("4--> minimum marks.")
    print("5--> maximum frequency.")
    print("6--> exit.")

#menu function
def menu():
    num=int(input("enter number to access the data : "))
    if num==1:
        avg()
    elif num==2:
        abs()    
    elif num==3:
        max()  
    elif num==4:
        min()
    elif num==5:
        freq()  
    elif num==6:
        def back():
            return 0
    elif num>6:
        print("enter valid number")  
        menu() 

#average function
def avg():
    total=0
    count=0
    average=0
    for i in range(n):
        if(markList[i]!='ab'):
            total=total+int(markList[i])
            count=count+1
    
    average=total/count
    print(markList)
    print("average of marks is : ",average)
    menu()
    
#absent function
def abs():
    count=0
    for i in range(n):
        if(markList[i]=="ab"):
            count=count+1
    print(markList)
    print("No. of absent students are : ",count)  
    menu()      

#maximum function
def max():
    mx=0
    for i in range(n):
        if(markList[i]!="ab" and int(markList[i])>mx):
            mx=int(markList[i])

    print(markList)
    print("maximum marks is : ",mx)
    menu()

#minimum function
def min():
    mini=100
    for i in range(n):
        if(markList[i]!="ab" and int(markList[i])<mini ):
            mini=int(markList[i])
    
    print(markList)
    print("minimum marks is : ",mini)
    menu()

#frequency function
def freq():
    a=0
    grtNo=0
    present=[]
    present1=[]

    for i in range(n):
        if(markList[i]!='ab'):
           a=int(markList[i])
           present.append(a)

    for j in range(len(present)):
        count=0
        for k in range(len(present)): 
            if(present[j]==present[k]):
                count=count+1
        present1.append(count)  
        if(int(present1[j])>grtNo):
            grtNo=j

    print(markList)
    print("max frequency number is : ",present[grtNo])     
    print("max frequency is : ",present1[grtNo]) 
    menu()

#main function
n=int(input("enter no. of students : "))
markList=[]

getdata()
menu()