import random

user_name = input('Enter your name to play the higher/lower Game ')
print ('Welcome to the higher/lower game', user_name)

lower = int(input('Enter the lower bound: '))
upper = int(input('Enter the upper bound: '))

if (upper <= lower):
    print('The lower bound must be less than upper bound. ')
    lower = int(input('Enter the lower bound: '))
    upper = int(input('Enter the upper bound: '))

random_num = random.randint(min(lower, upper), max(lower, upper))

while (True):
    #TODO replace upper and lower with values without erroring out - OMG I was putting my .format in the wrong place SMH, works now!
    user_guess = int(input('Great, now guess a number between {} and {}: '.format(lower,upper))
    if (user_guess < random_num):
        print('Nope, too low. ')
        user_guess = input(('Guess another number: '))
    elif (user_guess > random_num):
        print('Nope, too high. ')
        user_guess = input(('Guess another number: '))
    else: (user_guess == random_num)
    print('You got it!')
    break
