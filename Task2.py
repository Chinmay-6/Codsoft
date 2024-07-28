#Declaration of functions
bol=True

def addition(a, b):
    print("Addition of Two Numbers: ",a + b)


def subtraction(a, b):
    print("Subtraction of Two Numbers: ",a - b)


def multiplication(a, b):
    print("Multiplication of Two Numbers",a * b)

def division(a ,b):
    if (b==0):
        print("Division Cannot be Performed")
    else:
        print("Division of two Numbers",(a/b))
#Main Program
while(bol== True) :

    print("1 for addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for exit ")
    choice = int(input("enter your choice between 1-5 :"))

    if choice in (1,2,3,4):
        num1 = int(input("Enter 1st Number"))
        num2 = int(input("Enter your Second Number"))

        if choice==1:
            addition(num1,num2)

        elif choice==2:
            subtraction(num1,num2)

        elif choice==3:
            multiplication(num1,num2)

        elif choice==4 :
            division(num1,num2)

    elif choice==5 :
            exit()
    else:
        print("Invalid Choice")



