import random
rand = random.randint(1,10)
guess = 0
guess = input("Guess a number 1-10. ")
while guess != rand:
    if guess > rand:
        print "You're too high."
    elif guess < rand:
        print "You're too low."
    guess = input("Guess a number 1-10. ")
print "You got it."