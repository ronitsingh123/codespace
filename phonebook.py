def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(intput("Number: "))
        if n > 0:
            break

def meow(n):
    print("meow")

main()
