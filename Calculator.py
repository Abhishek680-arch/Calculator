num1=int(input("Enter a first number:"))
num2=int(input("Enter a second number:"))
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multi(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

print("Select the given option as Given\n"
      "1.Addition\n"
      "2.Subtarction\n"
      "3.Multiplication\n"
      "4.Division")

Select=int(input("Please Select the option as Given in the list "))

if Select== 1:
    print(num1 ,"+",num2,"=",
    add(num1,num2))

elif Select ==2:
    print(num1,"-",num2,"=",
    sub(num1,num2))

elif Select ==3:
    print(num1,"*",num2,"=",
    multi(num1,num2))
elif Select ==4:
    print(num1,"/",num2,"=",
    div(num1,num2))
else:
    print("Invalid option you have to selected please the check the list......")
