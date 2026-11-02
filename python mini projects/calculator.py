def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: cannot divide by zero"
    else:
        return x / y

print("Select Operation : ")
print("1. ADD\n2. Subract\n3. Multiplication\n4. Division ")

choice = int(input("Enter your choice (1/2/3/4) : "))

if choice in (1, 2, 3, 4):
    num1 = float(input("\nEnter your first value : "))
    num2 = float(input("\nEnter your second value : "))

    if choice == 1:
        print(f"\n[{num1} + {num2}] = {add(num1, num2)}")
    elif choice == 2:
        print(f"\n[{num1} - {num2}] = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"\n[{num1} x {num2}] = {multiply(num1, num2)}")
    elif choice == 4:
        print(f"\n[{num1} / {num2}] = {division(num1, num2)}")
else:
    print("invalid")
