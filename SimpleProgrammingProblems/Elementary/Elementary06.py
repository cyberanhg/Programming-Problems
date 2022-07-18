# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

number_n = int(input("Enter a number: "))

option = int(input("\n 1. Add \n 2. Multiply \nChoose an option: "))

if (option == 1):
    number_n += number_n
else:
    number_n *= number_n

print(f"Value is: {number_n}")
