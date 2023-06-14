people = {
       "Carter": "+29299292929",
       "David": "004040403030"
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")