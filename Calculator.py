def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("Please select the operation which you want to perform \n" 
    "1. add\n"
    "2. sub\n"
    "3. mul\n"
    "4. div\n")

select = int(input("Select the operation (1-4):"))


x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

if select ==1:
    print(x,"+",y,"=",add(x,y))

elif select==2:
    print(x,"-",y,"=",sub(x,y))

elif select==3:
    print(x,"*",y,"=",mul(x,y))

elif select==4:
    print(x,"/",y,"=",sub(x,y))
    
else:
    print("invalid input")
