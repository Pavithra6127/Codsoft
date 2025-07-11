
#TASK -2 - CALCULATOR

num1=int(input("Enter A Number:"))
num2=int(input("Enter A Number:"))
operator=input("Enter A Operator(+,-,*,/,%):")

if operator=="+":
    sum=num1+num2
    print("The Sum Of the two numbers is:",sum)
    
elif operator=="-":
    difference=num1-num2
    print("The difference Of the two numbers is:",difference)

elif operator=="*":
    product=num1*num2
    print("The product Of the two numbers is:",product)

elif operator=="/":
    quotient=num1/num2
    print("The quotient Of the two numbers is:",quotient)

elif operator=="%":
    remainder=num1%num2
    print("The remainder Of the two numbers is:",remainder)

