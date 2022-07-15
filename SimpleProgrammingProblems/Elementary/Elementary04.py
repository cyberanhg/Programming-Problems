# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

number_n = int(input("Enter a number: "))

for i in range(1, number_n + 1):
    print(f" {i} + {number_n} = {number_n + i}")
