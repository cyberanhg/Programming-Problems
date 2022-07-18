# Write a program that prints a multiplication table for numbers up to 12.

for i in range(1, 12+1):
    for value in range(1, 10+1):
        print(f"{value} x {i} = {value * i}\n")
