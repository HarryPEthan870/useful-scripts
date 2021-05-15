import random
rand = random.randint(0,100)
global i, inp
i, inp = 1, 0
while i == 1:
    inp = int(input("Enter your guess: "))
    i -= 1
    if inp == rand:
        print("You have guessed correctly!!")
        break
    elif inp > rand:
        print("Your have guessed to high!")
        i += 1
    elif inp < rand:
        print("You have guessed to low!")
        i += 1
