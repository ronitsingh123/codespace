import sys

names = ["Ron", "Harry", "Hermoine"]

for n in names:
    name = input("Name: ")
    if n == name:
        print("Found")
        sys.exit(0)
print("Not found")
sys.exit(1)
