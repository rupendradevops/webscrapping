def add_without_plus_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = add_without_plus_operator(num1, num2)
print("Sum:", result)