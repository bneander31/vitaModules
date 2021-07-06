#
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = num1 + num2
# result1 = int(num1) + int(num2)
# result2 = float(num1) + float(num2)
#
# print(result)
# print(result2)

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
