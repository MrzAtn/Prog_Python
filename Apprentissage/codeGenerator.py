import random 

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="1234567890"
other = "!"

lib = lower + upper + number + other

if __name__ == '__main__':
    for i in range(1):
        password = "".join(random.choices(population=lib, k=12))
        print(password)
