first =input("Enter the First Number:")
second=input("Enter the second number:")
operator=input("enter the operator(+,-,*,/,%):")

first =int(first)
second=int(second)

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("Invalid Operator")
