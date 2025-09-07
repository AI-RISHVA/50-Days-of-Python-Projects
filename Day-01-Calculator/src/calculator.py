print("select operation:")
print("1 - add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")

x=int(input("Select Operation:"))

if(x in [1,2,3,4]):
    n1=float(input("ENTER FIRST NUMBER: "))
    n2=float(input("ENTER SECOND NUMBER: "))
    if(x==1):
        result = n1+n2
    elif(x==2):
        result = n1-n2
    elif(x==3):
        result = n1*n2
    elif(x==4):
        result = n1/n2  #result  float number -> /, result int number ->  //
else:
    print("invalid peration entered.")
print("The result of the operation is {}" .format(result))