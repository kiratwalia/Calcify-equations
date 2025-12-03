print("Simple Calculator")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter operator[eg:+-*/%]: ")

if operator=="+":
    print("addition: ",num1+num2)
elif operator=="-":
    print("subtraction: ",num1-num2)
elif operator=="*":
    print("multiplication: ,num1*num2")
elif operator=="/":
     if num2==0:
         print("Invalid num2 can't be zero")
     else:
         print("division: ",num1/num2)
elif operator=="%":
    print("remainder: ",num1%num2)
else:
    print("Choose valid operator")

print("THANK YOU")

         




