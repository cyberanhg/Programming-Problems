# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

number_n = int(input("Enter a number: "))

for i in range(1, number_n + 1):
    if i % 3 or i % 5:
        print(f" {i} + {number_n} = {number_n + i}")
