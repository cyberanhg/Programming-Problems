# Modify the previous program such that only the users Alice and Bob are greeted with their names.

name = input("What is your name? ")

if(name == "Alice" or name == "Bob"):
    print(f"Hi {name} !")
else:
    print("...")
